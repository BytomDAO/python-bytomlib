# coding:utf-8


from pybtmsdk import BytomAPI
from pybtmsdk.transaction import decode_raw_tx, encode_raw_tx
from pybtmsdk.signature import generate_signatures_use_mnemonic

url = 'http://0.0.0.0:9888'
access_token = 'YOUR_ACCESS_TOKEN'

api = BytomAPI(url=url)

print(api.create_key("alice", "123456", "en"))
