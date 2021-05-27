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
    spend_bytes = b'entryid:output1:' + innerhash_bytes
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
    spend_bytes = b'entryid:voteoutput1:' + innerhash_bytes
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
    output_id_hexstr = sha3_256(b'entryid:output1:' + innerhash_bytes).hexdigest()
    return output_id_hexstr


def get_vote_output_id(prepare_output_id_hexstr):
    innerhash_bytes = sha3_256(bytes.fromhex(prepare_output_id_hexstr)).digest()
    output_id_hexstr = sha3_256(b'entryid:voteoutput1:' + innerhash_bytes).hexdigest()
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
                "asset_definition": "",
                "asset_id": "",
                "input_id": "",
                "issuance_program": "",
                "type": "",
                "witness_arguments": []
            }
            tx_input['type'] = "issue"
            nonth_length, length = get_uvarint(raw_transaction_str[offset:offset + 18])
            offset = offset + 2 * length
            nonce = raw_transaction_str[offset:offset + nonth_length * 2]
            offset += nonth_length * 2
            nonce_hash_hexstr = sha3_256(bytes.fromhex(nonce)).hexdigest()
            tx_input['asset_id'] = raw_transaction_str[offset:offset + 64]
            offset += 64
            tx_input['amount'], length = get_uvarint(raw_transaction_str[offset:offset + 18])
            offset = offset + 2 * length
            source_positon, length = get_uvarint(raw_transaction_str[offset:offset + 18])
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
                #"spend_commitment_suffix": "",
                #"witness_suffix": "",
            }
            tx_input['type'] = "spend"
            spend_commitment_length, length = get_uvarint(raw_transaction_str[offset:offset + 18])
            offset = offset + 2 * length
            source_id = raw_transaction_str[offset:offset + 64]
            offset += 64
            tx_input['asset_id'] = raw_transaction_str[offset:offset + 64]
            offset += 64
            tx_input['amount'], length = get_uvarint(raw_transaction_str[offset:offset + 18])
            offset = offset + 2 * length
            tx['fee'] += tx_input['amount']
            source_positon, length = get_uvarint(raw_transaction_str[offset:offset + 18])
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
                tx_input["state_data"].append(offset)

            witness_length, length = get_uvarint(raw_transaction_str[offset:offset + 18])
            offset = offset + 2 * length
            witness_arguments_amount, length = get_uvarint(raw_transaction_str[offset:offset + 18])
            offset = offset + 2 * length
            if witness_arguments_amount == 1:
                offset = offset + 2
                tx_input['witness_arguments'] = None
            else:
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
                "asset_definition": {},
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
            offset += 64
            tx_input['asset_id'] = raw_transaction_str[offset:offset + 64]
            offset += 64
            tx_input['amount'], length = get_uvarint(raw_transaction_str[offset:offset + 18])
            offset = offset + 2 * length
            tx['fee'] += tx_input['amount']
            source_positon, length = get_uvarint(raw_transaction_str[offset:offset + 18])
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
                tx_input["state_data"].append(offset)

            x_pub_length, length = get_uvarint(raw_transaction_str[offset:offset + 18])
            xpub_str = raw_transaction_str[offset: offset + length * 2 + x_pub_length * 2]
            offset = offset + 2 * length
            tx_input["vote"] = raw_transaction_str[offset: offset + x_pub_length * 2]
            offset = offset + 2 * x_pub_length

            witness_length, length = get_uvarint(raw_transaction_str[offset:offset + 18])
            offset = offset + 2 * length
            witness_arguments_amount, length = get_uvarint(raw_transaction_str[offset:offset + 18])
            offset = offset + 2 * length
            if witness_arguments_amount == 1:
                offset = offset + 2
                tx_input['witness_arguments'] = None
            else:
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

    # print("fuck:", "prepare_mux_hexstr", prepare_mux_hexstr)
    input_mux_hexstr = prepare_mux_hexstr
    tx_output_amount, length = get_uvarint(raw_transaction_str[offset:offset + 18])
    offset = offset + 2 * length
    prepare_tx_id_hexstr += (tx_output_amount).to_bytes((tx_output_amount.bit_length() + 7) // 8, 'little').hex()
    for i in range(tx_output_amount):
        tx_output = {
            "address": "",
            "amount": 0,
            "asset_definition": {},
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

    if tx_input['type'] == "coinbase":
        tx['fee'] = 0
    tx['tx_id'] = get_tx_id(prepare_tx_id_hexstr)

    for i in range(len(tx["inputs"])):
        tx["inputs"][i]["sign_data"] = sig_hash(tx["inputs"][i]["input_id"], tx['tx_id'])
        if "witness_arguments" in tx["inputs"][i].keys() and len(tx["inputs"][i]["witness_arguments"]) == 0:
            tx["inputs"][i]["witness_arguments"] = None
    return tx


def sig_hash(hash_id, tx_id):
    return sha3_256(bytes.fromhex(hash_id + tx_id)).hexdigest()

