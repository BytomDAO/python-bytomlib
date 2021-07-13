# coding:utf-8


from pybtmsdk import BytomAPI
from pybtmsdk.transaction import decode_raw_tx, encode_raw_tx
from pybtmsdk.signature import generate_signatures_use_mnemonic

url = 'http://0.0.0.0:9888'
access_token = 'YOUR_ACCESS_TOKEN'

api = BytomAPI(url=url)

#print(api.create_key("alice", "123456", "en"))

# print(api.update_key_alias("24a877a92463a87f849215195052a9e4715a5bfaa6aa509df90e99c85f482652b7bcd4bd7c5de6884efc044505fda598ded64f9ed7657331da44e9631bb53f10",
#                            "abcde", return_dict=True))

print(api.update_key_alias("24a877a92463a87f849215195052a9e4715a5bfaa6aa509df90e99c85f482652b7bcd4bd7c5de6884efc044505fda598ded64f9ed7657331da44e9631bb53f10",
                           "abcde", return_dict=True))




