# coding:utf-8


from pybtmsdk import BytomAPI
from pybtmsdk.transaction import decode_raw_tx
from pybtmsdk.signature import generate_signatures_use_mnemonic

url = 'http://139.224.216.240:9887'
access_token = 'YOUR_ACCESS_TOKEN'

api = BytomAPI(url=url)

# ret = api.wallet_info(return_dict=True)
# print(ret)

# ret = api.wallet_info(return_json=True)
# print(ret)


asset_id = "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"
address = "sm1q3wfltg8llv9w3r4g9nusx5xw7mcq34ehqwguud"
actions = [
    {
      "account_id": "1QCDJ6T3G0A04",
      "amount": 400000,
      "asset_id": asset_id,
      "type": "spend_account"
    },
    {
      "account_id": "1QCDJ6T3G0A04",
      "amount": 300000,
      "asset_id": asset_id,
      "type": "spend_account"
    },
    {
      "amount": 30000,
      "asset_id": asset_id,
      "address": address,
      "type": "control_address"
    }
]

# sm1q3wfltg8llv9w3r4g9nusx5xw7mcq34ehqwguud bycoin派生路径
# sm1q27ujth2eech6xvaxwzcr8axqkjcmzqfh6t705j 实际的地址

# print(api.list_balances(account_id="1QCDJ6T3G0A04", account_alias="ipqhjjybj"))
# print(api.list_balances(account_id="1QB26RD800A02", account_alias="test"))


template = api.build_transaction(base_transaction=None, actions=actions, ttl=10, time_range=1521625823, return_dict=True)
print("template: " + str(template))
decoded_tx = api.decode_raw_transaction(template["raw_transaction"], return_dict=True)
print("decoded_tx: " + str(decoded_tx))

mnemonic_str = "head verb dose torch divert bulb abstract shaft fatal pet accident else"
# from pybtmsdk.receiver import get_new_address
# from pybtmsdk.key import get_child_xprv, get_xpub, get_seed, get_root_xprv

# private_key = get_root_xprv(get_seed(mnemonic_str))
# address = get_new_address(xpub_hexstr=get_xpub(private_key), account_index_int=1, address_index_int=1, change_bool=True, network_str="solonet")
# print("address", address["address"])

basic_signed = generate_signatures_use_mnemonic([mnemonic_str], template, decoded_tx)
print("basic_signed: " + str(basic_signed))
print(type(basic_signed))
result = api.sign_transaction(password="12345", transaction=basic_signed, return_dict=True)
print("result raw_transaction: " + str(result))

# result = api.sign_transaction(password="12345", transaction=template, return_dict=True)
# print("result raw_transaction: " + str(result))

##############
## decode test
# raw_transaction = "07018e050101e101035dfad5195a0c8e3b590b86a3c0a95e7529565888508aecca96e9aeda633002f409fe9791d71b67ee62515e08723c061b5ccb952a80d804417c8aeedf7f633c524a92c30f03010c7370656e6450726f6772616d01097374617465446174618001616635393430303661343038333764396630323864616162623664353839646630623931333864616566616435363833653532333363323634363237393231373239346138643533326536303836336263663139363632356133356662386365656666613363303936313065623932646366623635356139343766313332363917020a617267756d656e7473310a617267756d656e747332010101ca018001616635393430303661343038333764396630323864616162623664353839646630623931333864616566616435363833653532333363323634363237393231373239346138643533326536303836336263663139363632356133356662386365656666613363303936313065623932646366623635356139343766313332363981756fdab39a17163b0ce582ee4ee256fb4d1e156c692b997d608a42ecb38d47e80701195465737453657269616c697a6174696f6e54784f7574707574010973746174654461746100"
# print(raw_transaction)

# decoded_tx = api.decode_raw_transaction(raw_transaction, return_dict=True)
# print("decoded_tx 0: " + str(decoded_tx))

# print(decode_raw_tx(raw_transaction, "solonet"))


# decoded_tx = api.decode_raw_transaction("07018e0502015f015dfad5195a0c8e3b590b86a3c0a95e7529565888508aecca96e9aeda633002f410ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff92c30f03010c7370656e6450726f6772616d010973746174654461746117020a617267756d656e7473330a617267756d656e747334015f015dfad5195a0c8e3b590b86a3c0a95e7529565888508aecca96e9aeda633002f409ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff92c30f03010c7370656e6450726f6772616d010973746174654461746117020a617267756d656e7473330a617267756d656e74733401010034a69849e11add96ac7053aad22ba2349a4abf5feb0475a0afcadff4e128be76cf92c30f010474727565010973746174654461746100", return_dict=True)
# print("decoded_tx 1: " + str(decoded_tx))


# decoded_tx = api.decode_raw_transaction("07018e0502015f015dfad5195a0c8e3b590b86a3c0a95e7529565888508aecca96e9aeda633002f410ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff92c30f03010c7370656e6450726f6772616d010973746174654461746117020a617267756d656e7473330a617267756d656e747334015f015dfad5195a0c8e3b590b86a3c0a95e7529565888508aecca96e9aeda633002f409ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff92c30f03010c7370656e6450726f6772616d010973746174654461746117020a617267756d656e7473330a617267756d656e74733401010034a69849e11add96ac7053aad22ba2349a4abf5feb0475a0afcadff4e128be76cf92c30f010474727565010973746174654461746100", return_dict=True)
# print("decoded_tx 2: " + str(decoded_tx))


# decoded_tx = api.decode_raw_transaction("07010001012b00030a0908916133a0d64d1d973b631e226ef95338ad4a536b95635f32f0d04708a6f2a26380a094a58d1d090001010101030102030101002a000000000000000000000000000000000000000000000000000000000000000080a094a58d1d0101010000", return_dict=True)
# print("decoded_tx 3: " + str(decoded_tx))


# decoded_tx = api.decode_raw_transaction("07010001010b02096172626974726172790002010034ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff92c30f010474727565010973746174654461746100010035ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff92c30f010566616c7365010973746174654461746100", return_dict=True)
# print("decoded_tx 4: " + str(decoded_tx))

# decoded_tx = api.decode_raw_transaction("07018e0502012a00056e6f6e6365a69849e11add96ac7053aad22ba2349a4abf5feb0475a0afcadff4e128be76cf92c30f380f6173736574446566696e6974696f6e010f69737375616e636550726f6772616d020a617267756d656e7473310a617267756d656e747332015f015dfad5195a0c8e3b590b86a3c0a95e7529565888508aecca96e9aeda633002f409ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff92c30f03010c7370656e6450726f6772616d010973746174654461746117020a617267756d656e7473330a617267756d656e74733401010034a69849e11add96ac7053aad22ba2349a4abf5feb0475a0afcadff4e128be76cf92c30f010474727565010973746174654461746100", return_dict=True)
# print("decoded_tx 5: " + str(decoded_tx))

# vote
# decoded_tx = api.decode_raw_transaction("07018e050101e101035dfad5195a0c8e3b590b86a3c0a95e7529565888508aecca96e9aeda633002f409fe9791d71b67ee62515e08723c061b5ccb952a80d804417c8aeedf7f633c524a92c30f03010c7370656e6450726f6772616d01097374617465446174618001616635393430303661343038333764396630323864616162623664353839646630623931333864616566616435363833653532333363323634363237393231373239346138643533326536303836336263663139363632356133356662386365656666613363303936313065623932646366623635356139343766313332363917020a617267756d656e7473310a617267756d656e747332010101ca018001616635393430303661343038333764396630323864616162623664353839646630623931333864616566616435363833653532333363323634363237393231373239346138643533326536303836336263663139363632356133356662386365656666613363303936313065623932646366623635356139343766313332363981756fdab39a17163b0ce582ee4ee256fb4d1e156c692b997d608a42ecb38d47e80701195465737453657269616c697a6174696f6e54784f7574707574010973746174654461746100", return_dict=True)
# print("decoded_tx 6: " + str(decoded_tx))
