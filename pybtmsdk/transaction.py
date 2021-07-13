import requests
import json
from _pysha3 import sha3_256
from pybtmsdk.receiver import get_address

# submit_transaction broadcast raw transaction
# raw_transaction_str is signed transaction,
# test data 1:
#   raw_transaction_hexstr: 070100010160015e5dfc352f9247985e92b2688a9a0a0e3e45a52f633c7d2c35cf6485fc1f03a89cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8094ebdc030101160014052620b86a6d5e07311d5019dffa3864ccc8a6bd630240988348a301c86563eb16105cc0c7e12e8cd1fbc7e9031933dac05a32d2a696bc77b83f25a99a4a9458d976c5327b8004918545a3fde567f28d805f741db54e0b20e87ca3acdebdcad9a1d0f2caecf8ce0dbfc73d060807a210c6f225488347961402013dffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff80b6f7f302011600147950bb5fcfb1c3fe14198c14ebd4ad85bb69bbc500013cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8084af5f011600141d8e1c2d71843f41e2131d7fd6df8b47e2cf56b900
#   submit_url: https://blockmeta.com/api/wisdom/broadcast-transaction
# test data 2:
#   raw_transaction_hexstr: 07010001015f015d2f4a8f10afbc0448779fadd916a3f1b8518ffe0b7d20fdf470d8e9b4993ef2b4ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc0d8883200011600144a594e3e4cbbd87629476e7ee24c1637df66c0b76302406fd39079681118840fd6fd66cdff769f2d05d8520312e9dd559dc23c36a3cb3921e47cba233d5d2267eb0f128a908d1bab877e172e880d3f36dc6a5e5826540c202854e5c181f5a862edd190e413d75937549758ef4902e1475aac52623f0a239302013cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc09dd81001160014f63f68597df5c88a92e04229e0fd08a3584ade3b00013cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff80e1eb1701160014664f28ec6ab8826a028658dc0d0d1f94c6e20fa300
#   submit_url: https://blockmeta.com/api/v2/broadcast-transaction
# def submit_transaction(raw_transaction_hexstr, submit_url):
#     raw_transaction_dict = {
#         "transaction": raw_transaction_hexstr
#     }
#     raw_transaction_json = json.dumps(raw_transaction_dict)
#     headers = {
#         "content-type": "application/json",
#         "accept": "application/json"
#     }
#     response = requests.post(submit_url, headers=headers, data=raw_transaction_json)
#     return response.text[:-1]


# def decode_raw_transaction(raw_transaction_str):
#     raw_transaction_dict = {
#         "raw_transaction": raw_transaction_str
#     }
#     raw_transaction_json = json.dumps(raw_transaction_dict)
#     headers = {
#         "content-type": "application/json",
#         "accept": "application/json"
#     }
#     url = 'http://127.0.0.1:9888/decode-raw-transaction'
#     response = requests.post(url, headers=headers, data=raw_transaction_json)
#     return {
#         "response": response.text[:-1]
#     }


def get_uvarint(uvarint_str):
    uvarint_bytes = bytes.fromhex(uvarint_str)
    x, s, i = 0, 0, 0
    while True:
        b = uvarint_bytes[i]
        if b < 0x80:
            if i > 9 or i == 9 and b > 1:
                return "overflow"
            return x | int(b) << s, i + 1
        x |= int(b & 0x7f) << s
        s += 7
        i += 1


'''
get_spend_output_id create tx_input spend output id
test data 1:
  source_id_hexstr: 28b7b53d8dc90006bf97e0a4eaae2a72ec3d869873188698b694beaf20789f21
  asset_id_hexstr: ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
  amount_int: 41250000000
  source_position_int: 0
  vmversion_int: 1
  control_program_hexstr: 00149335b1cbd4a77b78e33315a0ed10a95b12e7ca48
  spend_output_id_hexstr: f229ec6f403d586dc87aa2546bbe64c5f7b5f46eb13c6ee4823d03bc88a7cf17
'''


def get_spend_output_id(source_id_hexstr, asset_id_hexstr, amount_int, source_position_int, vmversion_int, control_program_hexstr, for_spend_id_state_hexstr):
    amount_hexstr = amount_int.to_bytes(8, byteorder='little').hex()
    source_position_hexstr = source_position_int.to_bytes(8, byteorder='little').hex()
    vmversion_hexstr = vmversion_int.to_bytes(8, byteorder='little').hex()
    cp_length_int = len(control_program_hexstr) // 2
    cp_length_hexstr = cp_length_int.to_bytes((cp_length_int.bit_length() + 7) // 8, byteorder='little').hex()
    sc_hexstr = source_id_hexstr + asset_id_hexstr + amount_hexstr + source_position_hexstr + vmversion_hexstr + cp_length_hexstr +  control_program_hexstr + for_spend_id_state_hexstr
    innerhash_bytes = sha3_256(bytes.fromhex(sc_hexstr)).digest()
    spend_bytes = b'entryid:originalOutput1:' + innerhash_bytes
    spend_output_id_hexstr = sha3_256(spend_bytes).hexdigest()
    return spend_output_id_hexstr


def get_vote_spend_output_id(source_id_hexstr, asset_id_hexstr, amount_int, source_position_int, vmversion_int, control_program_hexstr, xpub_str, for_vote_id_state_hexstr):
    amount_hexstr = amount_int.to_bytes(8, byteorder='little').hex()
    source_position_hexstr = source_position_int.to_bytes(8, byteorder='little').hex()
    vmversion_hexstr = vmversion_int.to_bytes(8, byteorder='little').hex()
    cp_length_int = len(control_program_hexstr) // 2
    cp_length_hexstr = cp_length_int.to_bytes((cp_length_int.bit_length() + 7) // 8, byteorder='little').hex()
    sc_hexstr = source_id_hexstr + asset_id_hexstr + amount_hexstr + source_position_hexstr + vmversion_hexstr + cp_length_hexstr +  control_program_hexstr + xpub_str + for_vote_id_state_hexstr
    innerhash_bytes = sha3_256(bytes.fromhex(sc_hexstr)).digest()
    spend_bytes = b'entryid:voteOutput1:' + innerhash_bytes
    spend_output_id_hexstr = sha3_256(spend_bytes).hexdigest()
    return spend_output_id_hexstr


'''
get_input_id create tx input_id
test data 1:
    spend_output_id_hexstr: f229ec6f403d586dc87aa2546bbe64c5f7b5f46eb13c6ee4823d03bc88a7cf17
    input_id_hexstr: 6e3f378ed844b143a335e306f4ba26746157589c87e8fc8cba6463c566c56768
'''


def get_input_id(spend_output_id_hexstr):
    innerhash_bytes = sha3_256(bytes.fromhex(spend_output_id_hexstr)).digest()
    input_id_hexstr = sha3_256(b'entryid:spend1:' + innerhash_bytes).hexdigest()
    return input_id_hexstr


def get_vote_input_id(vote_output_id_hexstr):
    innerhash_bytes = sha3_256(bytes.fromhex(vote_output_id_hexstr)).digest()
    input_id_hexstr = sha3_256(b'entryid:vetoInput1:' + innerhash_bytes).hexdigest()
    return input_id_hexstr


def get_mux_id(prepare_mux_hexstr):
    innerhash_bytes = sha3_256(bytes.fromhex(prepare_mux_hexstr)).digest()
    mux_id_hexstr = sha3_256(b'entryid:mux1:' + innerhash_bytes).hexdigest()
    return mux_id_hexstr


def get_output_id(prepare_output_id_hexstr):
    innerhash_bytes = sha3_256(bytes.fromhex(prepare_output_id_hexstr)).digest()
    output_id_hexstr = sha3_256(b'entryid:originalOutput1:' + innerhash_bytes).hexdigest()
    return output_id_hexstr


def get_vote_output_id(prepare_output_id_hexstr):
    innerhash_bytes = sha3_256(bytes.fromhex(prepare_output_id_hexstr)).digest()
    output_id_hexstr = sha3_256(b'entryid:voteOutput1:' + innerhash_bytes).hexdigest()
    return output_id_hexstr


def get_tx_id(prepare_tx_id_hexstr):
    innerhash_bytes = sha3_256(bytes.fromhex(prepare_tx_id_hexstr)).digest()
    tx_id_hexstr = sha3_256(b'entryid:txheader:' + innerhash_bytes).hexdigest()
    return tx_id_hexstr


def get_issue_input_id(prepare_issue_hexstr):
    innerhash_bytes = sha3_256(bytes.fromhex(prepare_issue_hexstr)).digest()
    tx_id_hexstr = sha3_256(b'entryid:issuance1:' + innerhash_bytes).hexdigest()
    return tx_id_hexstr


def get_coinbase_input_id(prepare_coinbase_input_id_hexstr):
    innerhash_bytes = sha3_256(bytes.fromhex(prepare_coinbase_input_id_hexstr)).digest()
    coinbase_input_id_hexstr = sha3_256(b'entryid:coinbase1:' + innerhash_bytes).hexdigest()
    return coinbase_input_id_hexstr


'''
decode_raw_tx decode raw transaction
testdata 1:
    raw_transaction_str: 070100010161015f28b7b53d8dc90006bf97e0a4eaae2a72ec3d869873188698b694beaf20789f21ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8099c4d5990100011600149335b1cbd4a77b78e33315a0ed10a95b12e7ca48630240897e2d9d24a3b5faaed0579dee7597b401491595675f897504f8945b29d836235bd2fca72a3ad0cae814628973ebcd142d9d6cc92d0b2571b69e5370a98a340c208cb7fb3086f58db9a31401b99e8c658be66134fb9034de1d5c462679270b090702013effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff80f9f8bc98010116001406ce4b689ba026ffd3a7ca65d1d059546d4b78a000013dffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff80c6868f01011600147929ef91997c827bebf60fa608f876ea27523c4700
    network_str: solonet
    transaction: 
{
  "fee": 20000000,
  "inputs": [
    {
      "address": "sm1qjv6mrj755aah3cenzksw6y9ftvfw0jjgk0l2mw",
      "amount": 41250000000,
      "asset_definition": {},
      "asset_id": "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff",
      "control_program": "00149335b1cbd4a77b78e33315a0ed10a95b12e7ca48",
      "input_id": "6e3f378ed844b143a335e306f4ba26746157589c87e8fc8cba6463c566c56768",
      "spent_output_id": "f229ec6f403d586dc87aa2546bbe64c5f7b5f46eb13c6ee4823d03bc88a7cf17",
      "type": "spend",
      "witness_arguments": [
        "897e2d9d24a3b5faaed0579dee7597b401491595675f897504f8945b29d836235bd2fca72a3ad0cae814628973ebcd142d9d6cc92d0b2571b69e5370a98a340c",
        "8cb7fb3086f58db9a31401b99e8c658be66134fb9034de1d5c462679270b0907"
      ]
    }
  ],
  "outputs": [
    {
      "address": "sm1qqm8yk6ym5qn0l5a8efjar5ze23k5k79qnvtslj",
      "amount": 40930000000,
      "asset_definition": {},
      "asset_id": "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff",
      "control_program": "001406ce4b689ba026ffd3a7ca65d1d059546d4b78a0",
      "id": "74c73266730d3c6ea32e8667ef9b867068736b84be240fe9fef205fa68bb7b95",
      "position": 0,
      "type": "control"
    },
    {
      "address": "sm1q0y57lyve0jp8h6lkp7nq37rkagn4y0z8hvh6kq",
      "amount": 300000000,
      "asset_definition": {},
      "asset_id": "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff",
      "control_program": "00147929ef91997c827bebf60fa608f876ea27523c47",
      "id": "f115a833d0c302a5006032858a7ed3987f0feb2daf2a9f849384950e4766af51",
      "position": 1,
      "type": "control"
    }
  ],
  "size": 333,
  "time_range": 0,
  "tx_id": "814a73dd57bae67c604f9cbc696cbc42035577423408cb9267136ed971e2bf63",
  "version": 1
}
'''


def decode_raw_tx(raw_transaction_str, network_str):
    tx = {
        "fee": 0,
        "inputs": [],
        "outputs": [],
        "size": 0,
        "time_range": 0,
        "tx_id": "",
        "version": 0
    }
    tx['fee'] = 0
    tx['size'] = len(raw_transaction_str) // 2
    offset = 2
    tx['version'], length = get_uvarint(raw_transaction_str[offset:offset + 18])
    offset = offset + 2 * length
    tx['time_range'], length = get_uvarint(raw_transaction_str[offset:offset + 18])
    offset = offset + 2 * length
    tx_input_amount, length = get_uvarint(raw_transaction_str[offset:offset + 8])
    offset = offset + 2 * length
    prepare_mux_hexstr = (tx_input_amount).to_bytes((tx_input_amount.bit_length() + 7) // 8, 'little').hex()
    prepare_tx_id_hexstr = (tx['version']).to_bytes(8, 'little').hex() + (tx['time_range']).to_bytes(8, 'little').hex()
    for index in range(tx_input_amount):
        asset_version, length = get_uvarint(raw_transaction_str[offset:offset + 18])
        offset = offset + 2 * length
        serialization_length, length = get_uvarint(raw_transaction_str[offset:offset + 18])
        offset = offset + 2 * length
        input_type = int(raw_transaction_str[offset:offset + 2], 16)
        offset += 2
        if input_type == 0:  # issue
            tx_input = {
                "amount": 0,
                "asset_definition": {},
                "asset_id": "",
                "input_id": "",
                "issuance_program": "",
                "type": "",
                "witness_arguments": [],
                "nonce": "",
                "source_position": -1,
            }
            tx_input['type'] = "issue"
            nonce_length, length = get_uvarint(raw_transaction_str[offset:offset + 18])
            offset = offset + 2 * length
            nonce = raw_transaction_str[offset:offset + nonce_length * 2]
            tx_input["nonce"] = nonce
            offset += nonce_length * 2
            nonce_hash_hexstr = sha3_256(bytes.fromhex(nonce)).hexdigest()
            tx_input['asset_id'] = raw_transaction_str[offset:offset + 64]
            offset += 64
            tx_input['amount'], length = get_uvarint(raw_transaction_str[offset:offset + 18])
            offset = offset + 2 * length
            source_positon, length = get_uvarint(raw_transaction_str[offset:offset + 18])
            tx_input["source_positon"] = int(source_positon)
            offset = offset + 2 * length
            asset_definition_size, length = get_uvarint(raw_transaction_str[offset:offset + 18])
            offset = offset + 2 * length
            tx_input['asset_definition'] = bytes.fromhex(
                raw_transaction_str[offset:offset + 2 * asset_definition_size]).decode()
            offset = offset + 2 * asset_definition_size
            vm_version, length = get_uvarint(raw_transaction_str[offset:offset + 18])
            offset = offset + 2 * length
            issuance_program_length, length = get_uvarint(raw_transaction_str[offset:offset + 18])
            offset = offset + 2 * length
            tx_input['issuance_program'] = raw_transaction_str[offset:offset + 2 * issuance_program_length]
            offset = offset + 2 * issuance_program_length
            witness_arguments_amount, length = get_uvarint(raw_transaction_str[offset:offset + 18])
            offset = offset + 2 * length
            for _ in range(witness_arguments_amount):
                argument_length, length = get_uvarint(raw_transaction_str[offset:offset + 18])
                offset = offset + 2 * length
                argument = raw_transaction_str[offset:offset + 2 * argument_length]
                offset = offset + 2 * argument_length
                tx_input['witness_arguments'].append(argument)

            prepare_issue_hexstr = nonce_hash_hexstr + \
                                   tx_input['asset_id'] + (tx_input['amount']).to_bytes(8, byteorder='little').hex()
            tx_input['input_id'] = get_issue_input_id(prepare_issue_hexstr)
            tx['inputs'].append(tx_input)
            prepare_mux_hexstr += tx_input['input_id'] + tx_input['asset_id'] \
                                  + (tx_input['amount']).to_bytes(8, byteorder='little').hex() + '0000000000000000'
            if index + 1 == tx_input_amount:
                prepare_mux_hexstr += '0100000000000000' + '0151'  # add program
            mux_id_hexstr = get_mux_id(prepare_mux_hexstr)
        elif input_type == 1:  # spend
            tx_input = {
                "address": "",
                "amount": 0,
                "asset_definition": {},
                "asset_id": "",
                "control_program": "",
                "input_id": "",
                "spent_output_id": "",
                "type": "",
                "state_data": [],
                "witness_arguments": [],
                "source_id": "",
                "source_positon": -1
                #"spend_commitment_suffix": "",
                #"witness_suffix": "",
            }
            tx_input['type'] = "spend"
            spend_commitment_length, length = get_uvarint(raw_transaction_str[offset:offset + 18])
            offset = offset + 2 * length
            source_id = raw_transaction_str[offset:offset + 64]
            tx_input["source_id"] = source_id
            offset += 64
            tx_input['asset_id'] = raw_transaction_str[offset:offset + 64]
            offset += 64
            tx_input['amount'], length = get_uvarint(raw_transaction_str[offset:offset + 18])
            offset = offset + 2 * length
            tx['fee'] += tx_input['amount']
            source_positon, length = get_uvarint(raw_transaction_str[offset:offset + 18])
            tx_input["source_positon"] = int(source_positon)
            offset = offset + 2 * length
            vmversion, length = get_uvarint(raw_transaction_str[offset:offset + 18])
            offset = offset + 2 * length
            control_program_length, length = get_uvarint(raw_transaction_str[offset:offset + 18])
            offset = offset + 2 * length
            tx_input['control_program'] = raw_transaction_str[offset:offset + 2 * control_program_length]
            offset = offset + 2 * control_program_length
            tx_input['address'] = get_address(tx_input['control_program'], network_str)
            len_state_num, length = get_uvarint(raw_transaction_str[offset:offset + 18])
            for_spend_id_state_hexstr = raw_transaction_str[offset:offset + length * 2]
            offset = offset + 2 * length
            for nn in range(len_state_num):
                state_data_length, length = get_uvarint(raw_transaction_str[offset:offset + 64])
                for_spend_id_state_hexstr = for_spend_id_state_hexstr + raw_transaction_str[offset:offset + 2 * length]
                offset = offset + 2 * length
                state_data = raw_transaction_str[offset:offset + 2 * state_data_length]
                for_spend_id_state_hexstr = for_spend_id_state_hexstr + raw_transaction_str[
                                                                        offset:offset + 2 * state_data_length]
                offset = offset + 2 * state_data_length
                tx_input["state_data"].append(state_data)

            witness_length, length = get_uvarint(raw_transaction_str[offset:offset + 18])
            offset = offset + 2 * length
            witness_arguments_amount, length = get_uvarint(raw_transaction_str[offset:offset + 18])
            offset = offset + 2 * length

            for _ in range(witness_arguments_amount):
                argument_length, length = get_uvarint(raw_transaction_str[offset:offset + 18])
                offset = offset + 2 * length
                argument = raw_transaction_str[offset:offset + 2 * argument_length]
                offset = offset + 2 * argument_length
                tx_input['witness_arguments'].append(argument)
            tx_input['spent_output_id'] = get_spend_output_id(source_id, tx_input['asset_id'], tx_input['amount'],
                                                              source_positon, vmversion, tx_input['control_program'],
                                                              for_spend_id_state_hexstr)
            tx_input['input_id'] = get_input_id(tx_input['spent_output_id'])
            tx['inputs'].append(tx_input)
            prepare_mux_hexstr += tx_input['input_id'] + tx_input['asset_id'] \
                                  + (tx_input['amount']).to_bytes(8, byteorder='little').hex() + '0000000000000000'
            if index + 1 == tx_input_amount:
                prepare_mux_hexstr += '0100000000000000' + '0151'  # add program

            mux_id_hexstr = get_mux_id(prepare_mux_hexstr)
        elif input_type == 2:  # coinbase
            tx_input = {
                "amount": 0,
                "arbitrary": "",
                "asset_id": "0000000000000000000000000000000000000000000000000000000000000000",
                "input_id": "",
                "type": "",
                "commitment_suffix": "",
                #"witness_suffix": []
            }
            tx_input['type'] = "coinbase"
            arbitrary_length, length = get_uvarint(raw_transaction_str[offset:offset + 18])
            prepare_coinbase_input_id_hexstr = raw_transaction_str[offset:offset + 2 * length]
            offset = offset + 2 * length
            tx_input['arbitrary'] = raw_transaction_str[offset:offset + 2 * arbitrary_length]
            prepare_coinbase_input_id_hexstr += tx_input['arbitrary']
            offset = offset + 2 * arbitrary_length
            tx_input['input_id'] = get_coinbase_input_id(prepare_coinbase_input_id_hexstr)
            offset = offset + 2
            tx['inputs'].append(tx_input)
            prepare_mux_hexstr += tx_input['input_id'] + 'ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff'

        elif input_type == 3:  # vote
            tx_input = {
                "amount": 0,
                "source_positon": -1,
                "control_program": "",
                "asset_id": "",
                "input_id": "",
                "type": "",
                "state_data": [],
                "veto_commitment_suffix": "",
                "witness_arguments": [],
                "vote": "",
            }
            tx_input['type'] = "vote"
            vote_comment_length, length = get_uvarint(raw_transaction_str[offset:offset + 18])
            offset = offset + 2 * length
            source_id = raw_transaction_str[offset:offset + 64]
            tx_input["source_id"] = source_id
            offset += 64
            tx_input['asset_id'] = raw_transaction_str[offset:offset + 64]
            offset += 64
            tx_input['amount'], length = get_uvarint(raw_transaction_str[offset:offset + 18])
            offset = offset + 2 * length
            tx['fee'] += tx_input['amount']
            source_positon, length = get_uvarint(raw_transaction_str[offset:offset + 18])
            tx_input["source_positon"] = int(source_positon)
            offset = offset + 2 * length
            vmversion, length = get_uvarint(raw_transaction_str[offset:offset + 18])
            offset = offset + 2 * length
            vote_program_length, length = get_uvarint(raw_transaction_str[offset:offset + 18])
            offset = offset + 2 * length
            tx_input['control_program'] = raw_transaction_str[offset:offset + 2 * vote_program_length]
            offset = offset + 2 * vote_program_length
            tx_input['address'] = get_address(tx_input['control_program'], network_str)

            len_state_num, length = get_uvarint(raw_transaction_str[offset:offset + 18])
            for_vote_id_state_hexstr = raw_transaction_str[offset:offset + length * 2]
            offset = offset + 2 * length
            for nn in range(len_state_num):
                state_data_length, length = get_uvarint(raw_transaction_str[offset:offset + 64])
                for_vote_id_state_hexstr = for_vote_id_state_hexstr + raw_transaction_str[offset:offset + 2 * length]
                offset = offset + 2 * length
                state_data = raw_transaction_str[offset:offset + 2 * state_data_length]
                for_vote_id_state_hexstr = for_vote_id_state_hexstr + raw_transaction_str[
                                                                      offset:offset + 2 * state_data_length]
                offset = offset + 2 * state_data_length
                tx_input["state_data"].append(state_data)

            x_pub_length, length = get_uvarint(raw_transaction_str[offset:offset + 18])
            xpub_str = raw_transaction_str[offset: offset + length * 2 + x_pub_length * 2]
            offset = offset + 2 * length
            tx_input["vote"] = raw_transaction_str[offset: offset + x_pub_length * 2]
            offset = offset + 2 * x_pub_length

            witness_length, length = get_uvarint(raw_transaction_str[offset:offset + 18])
            offset = offset + 2 * length
            witness_arguments_amount, length = get_uvarint(raw_transaction_str[offset:offset + 18])
            offset = offset + 2 * length
            
            for _ in range(witness_arguments_amount):
                argument_length, length = get_uvarint(raw_transaction_str[offset:offset + 18])
                offset = offset + 2 * length
                argument = raw_transaction_str[offset:offset + 2 * argument_length]
                offset = offset + 2 * argument_length
                tx_input['witness_arguments'].append(argument)

            tx_input['vote_output_id'] = get_vote_spend_output_id(source_id, tx_input['asset_id'], tx_input['amount'],
                                                                  source_positon, vmversion,
                                                                  tx_input['control_program'], xpub_str,
                                                                  for_vote_id_state_hexstr)
            tx_input['input_id'] = get_vote_input_id(tx_input['vote_output_id'])
            tx['inputs'].append(tx_input)
            prepare_mux_hexstr += tx_input['input_id'] + tx_input['asset_id'] \
                                  + (tx_input['amount']).to_bytes(8, byteorder='little').hex() + '0000000000000000'
            if index + 1 == tx_input_amount:
                prepare_mux_hexstr += '0100000000000000' + '0151'  # add program

            mux_id_hexstr = get_mux_id(prepare_mux_hexstr)

    input_mux_hexstr = prepare_mux_hexstr
    tx_output_amount, length = get_uvarint(raw_transaction_str[offset:offset + 18])
    offset = offset + 2 * length
    prepare_tx_id_hexstr += (tx_output_amount).to_bytes((tx_output_amount.bit_length() + 7) // 8, 'little').hex()
    for i in range(tx_output_amount):
        tx_output = {
            "address": "",
            "amount": 0,
            "asset_id": "",
            "control_program": "",
            "id": "",
            "position": 0,
            "state_data": [],
            "type": "",
            #"commitment_suffix": "",
            #"witness_suffix": ""
        }
        tx_output['position'] = i
        asset_version, length = get_uvarint(raw_transaction_str[offset:offset + 18])
        offset = offset + 2 * length
        output_type, length = get_uvarint(raw_transaction_str[offset:offset + 18])
        offset = offset + 2 * length

        serialization_length, length = get_uvarint(raw_transaction_str[offset:offset + 18])

        offset = offset + 2 * length

        tx_output['type'] = 'control'
        xpub_hex_str = ""
        if output_type == 1:  # vote
            output_xpub_length, length = get_uvarint(raw_transaction_str[offset:offset + 18])
            xpub_hex_str = raw_transaction_str[offset: offset + 2 * length + 2 * output_xpub_length]
            offset = offset + 2 * length
            tx_output["vote"] = raw_transaction_str[offset: offset + output_xpub_length * 2]
            offset = offset + 2 * output_xpub_length
            tx_output['type'] = 'vote'

        tx_output['asset_id'] = raw_transaction_str[offset:offset + 64]
        offset = offset + 64
        tx_output['amount'], length = get_uvarint(raw_transaction_str[offset:offset + 18])
        offset = offset + 2 * length
        if tx_input['type'] == "coinbase":
            # prepare_mux_hexstr = prepare_mux_hexstr + (tx_output['amount']).to_bytes(8, byteorder='little').hex() + '0000000000000000' + '0100000000000000' + '0151'
            prepare_mux_hexstr = input_mux_hexstr + (tx_output['amount']).to_bytes(8,
                                                                                   byteorder='little').hex() + '0000000000000000' + '0100000000000000' + '0151'
            mux_id_hexstr = get_mux_id(prepare_mux_hexstr)

        if tx_output['asset_id'] == 'ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff':
            tx['fee'] -= tx_output['amount']

        version, length = get_uvarint(raw_transaction_str[offset:offset + 18])
        offset = offset + 2 * length
        control_program_length, length = get_uvarint(raw_transaction_str[offset:offset + 18])
        offset = offset + 2 * length
        tx_output['control_program'] = raw_transaction_str[offset:offset + 2 * control_program_length]
        offset = offset + 2 * control_program_length

        prepare_output_id_hexstr = mux_id_hexstr + tx_output['asset_id'] + (tx_output['amount']) \
            .to_bytes(8, byteorder='little').hex() + (i).to_bytes(8, byteorder='little').hex() + '0100000000000000' + (
                                       control_program_length).to_bytes(
            (control_program_length.bit_length() + 7) // 8, 'little').hex() + tx_output['control_program']
        if output_type == 1:
            prepare_output_id_hexstr = prepare_output_id_hexstr + xpub_hex_str

        nelts, length = get_uvarint(raw_transaction_str[offset:offset + 18])
        prepare_output_id_hexstr += raw_transaction_str[offset:offset + 2 * length]
        offset = offset + 2 * length
        if nelts > 0:
            for j in range(nelts):
                ll_data, length = get_uvarint(raw_transaction_str[offset:offset + 18])
                prepare_output_id_hexstr += raw_transaction_str[offset:offset + 2 * length]
                offset = offset + 2 * length
                s = raw_transaction_str[offset:offset + ll_data * 2]
                tx_output["state_data"].append(s)
                prepare_output_id_hexstr += raw_transaction_str[offset:offset + 2 * ll_data]
                offset = offset + 2 * ll_data

        tx_output['address'] = get_address(tx_output['control_program'], network_str)
        _, length = get_uvarint(raw_transaction_str[offset:offset + 18])
        offset = offset + 2 * length

        if output_type == 1:  # vote
            tx_output['id'] = get_vote_output_id(prepare_output_id_hexstr)
        else:
            tx_output['id'] = get_output_id(prepare_output_id_hexstr)

        prepare_tx_id_hexstr += tx_output['id']
        
        tx['outputs'].append(tx_output)

    if tx_input['type'] in ["coinbase", "vote"]:
        tx['fee'] = 0
    tx['tx_id'] = get_tx_id(prepare_tx_id_hexstr)

    for i in range(len(tx["inputs"])):
        tx["inputs"][i]["sign_data"] = sig_hash(tx["inputs"][i]["input_id"], tx['tx_id'])
        if "witness_arguments" in tx["inputs"][i].keys() and len(tx["inputs"][i]["witness_arguments"]) == 0:
            tx["inputs"][i]["witness_arguments"] = None
    return tx


def sig_hash(hash_id, tx_id):
    return sha3_256(bytes.fromhex(hash_id + tx_id)).hexdigest()


def byte(x):
    ret = []
    while x > 1:
        ret.append(str(x % 2))
        x = x >> 1
    ret.append(str(x))
    ret.reverse()
    s = ''.join(ret)
    if len(s) >= 8:
        return s[-8:]
    else:
        return "".join((["0"] * (8-len(s)))) + s


hex_dic = {}
base = [str(x) for x in range(10)] + [ chr(x) for x in range(ord('a'),ord('a')+6)]
for i in range(len(base)):
    hex_dic[i] = base[i]


def dec2hex(x):
    a = int(x[0]) * 8 + int(x[1]) * 4 + int(x[2]) * 2 + int(x[3])
    b = int(x[4]) * 8 + int(x[5]) * 4 + int(x[6]) * 2 + int(x[7])

    return hex_dic[a] + hex_dic[b]


def convert(x):
    val = byte(x)
    val = "1" + val[1:]
    return dec2hex(val)


def put_uvarint(x):
    i = 0
    s = ""
    while x >= 0x80:
        s += str(convert(x))
        x = x >> 7
        i = i + 1

    s += dec2hex(byte(x))
    return s

def int_byte(v):
    if v % 2 == 0:
        return int(v / 2)
    else:
        return int((v + 1) / 2)

def write_var_str(s):
    if s is None:
        s = ""
    return ''.join([put_uvarint(int_byte(len(s))), s])

def write_extensible_string(s):
    if s is None:
        s = ""
    return ''.join([put_uvarint(int_byte(len(s))), s])

def write_var_list(arr_str):
    if arr_str is None:
        arr_str = []
    ret = []
    ret.append(put_uvarint(len(arr_str)))
    for i in range(len(arr_str)):
        ret.append(write_var_str(arr_str[i]))
    return ''.join(ret)


def write_spend_dic(input_dic):
    arr = []
    arr.append(input_dic["source_id"])
    arr.append(input_dic["asset_id"])
    arr.append(put_uvarint(input_dic["amount"]))
    arr.append(put_uvarint(input_dic["source_positon"]))
    arr.append("01")       # vm version
    arr.append(write_var_str(input_dic["control_program"]))
    arr.append(write_var_list(input_dic["state_data"]))

    return write_extensible_string(''.join(arr))


def write_vote_dic(input_dic):
    arr = []
    arr.append(input_dic["source_id"])
    arr.append(input_dic["asset_id"])
    arr.append(put_uvarint(input_dic["amount"]))
    arr.append(put_uvarint(input_dic["source_positon"]))
    arr.append("01")
    arr.append(write_var_str(input_dic["control_program"]))
    arr.append(write_var_list(input_dic["state_data"]))

    msg = write_extensible_string(''.join(arr))
    msg += write_var_str(input_dic["vote"])
    return msg 


def write_serialize_input_commitment(input_dic):
    arr = []

    if input_dic["type"] == "issue":
        arr.append("00")    # issue type
        arr.append(write_var_str(input_dic["nonce"]))
        arr.append(input_dic["asset_id"])
        arr.append(put_uvarint(input_dic["amount"]))
        
    elif input_dic["type"] == "spend":
        arr.append("01")    # spend type
        arr.append(write_spend_dic(input_dic))

    elif input_dic["type"] == "coinbase":
        arr.append("02")    # coinbase type
        arr.append(write_var_str(input_dic["arbitrary"]))

    elif input_dic["type"] == "vote":
        
        arr.append("03") # vote flag
        arr.append(write_vote_dic(input_dic))

    return ''.join(arr)

def write_serialize_input_witness(input_dic):
    arr = []

    if input_dic["type"] == "issue":
        #arr.append(write_var_str(input_dic["asset_definition"]))
        arr.append(write_var_str(stringToHexString(input_dic["asset_definition"])))
        arr.append("01")    # vm_version
        arr.append(write_var_str(input_dic["issuance_program"]))
        arr.append(write_var_list(input_dic["witness_arguments"]))

    elif input_dic["type"] == "spend":
        arr.append(write_var_list(input_dic["witness_arguments"]))

    elif input_dic["type"] == "coinbase":
        pass
    elif input_dic["type"] == "vote":
        arr.append(write_var_list(input_dic["witness_arguments"]))

    return ''.join(arr)

def bytesToHexString(bs):
    return ''.join(['%02X' % b for b in bs])

def stringToHexString(s):
    bs = bytes(s,encoding='utf8')
    return bytesToHexString(bs)

# def write_output(output_dic):
#     arr = []
#     return ''.join(arr)

def write_serialize_output_commitment(output_dic):
    arr = []

    if output_dic["type"] == "vote":
        arr.append(write_var_str(output_dic["vote"]))
        arr.append(output_dic["asset_id"])
        arr.append(put_uvarint(output_dic["amount"]))
        arr.append("01")        # vm version
        arr.append(write_var_str(output_dic["control_program"]))
        arr.append(write_var_list(output_dic["state_data"]))

    else:
        arr.append(output_dic["asset_id"])
        arr.append(put_uvarint(output_dic["amount"]))
        arr.append("01")        # vm version
        arr.append(write_var_str(output_dic["control_program"]))
        arr.append(write_var_list(output_dic["state_data"]))

    return ''.join(arr)


def encode_raw_tx(tx):
    arr = []
    arr.append("07")    # serflags
    arr.append("01")    # versions
    arr.append(put_uvarint(tx["time_range"]))
    arr.append(put_uvarint(len(tx["inputs"])))
    for i in range(len(tx["inputs"])):
        arr.append("01")  # asset version

        arr.append(write_extensible_string(write_serialize_input_commitment(tx["inputs"][i])))
        arr.append(write_extensible_string(write_serialize_input_witness(tx["inputs"][i])))
    
    arr.append(put_uvarint(len(tx["outputs"])))
    for i in range(len(tx["outputs"])):
        output_dic = tx["outputs"][i]

        arr.append("01")  # asset version
        if output_dic["type"] == "vote":
            arr.append("01")       # 投票output

        else:
            arr.append("00")       # 正常output type
            
        arr.append(write_extensible_string(write_serialize_output_commitment(output_dic)))

        arr.append("00")    # outputWitness

    return ''.join(arr)


