# coding:utf-8
import time

from pybtmsdk import BytomAPI
from pybtmsdk.transaction import decode_raw_tx, encode_raw_tx
from pybtmsdk.signature import generate_signatures_use_mnemonic

# url = 'http://139.224.216.240:9887'
url = 'http://127.0.0.1:9888'
access_token = 'YOUR_ACCESS_TOKEN'

api = BytomAPI(url=url)

asset_id = "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"
address = "sm1qfgrgle0ljfxs0zlprf5q02zs9v3zdrcv6tmuvx"
actions = [
    {
        "account_id": "1SA0QDN500A02",
        "amount": 400000,
        "asset_id": asset_id,
        "type": "spend_account"
    },
    # {
    #   "account_id": "1QEPIO7OG0A02",
    #   "amount": 300000,
    #   "asset_id": asset_id,
    #   "type": "spend_account"
    # },
    {
        "amount": 30000,
        "asset_id": asset_id,
        "address": address,
        "type": "control_address"
    }
]

for i in range(1000):
    template = api.build_transaction(base_transaction=None, actions=actions, ttl=10, time_range=int(time.time()),
                                     return_dict=True)
    print("template: " + str(template))

    raw_transaction = template["raw_transaction"]
    decoded_tx = decode_raw_tx(raw_transaction, "solonet")
    print("decoded_tx: " + str(decoded_tx))

    encode_transaction = encode_raw_tx(decoded_tx)
    print("encode_transaction: " + encode_transaction)

    if raw_transaction != encode_transaction:
        print("Error: raw_transaction:{}, template:{}".format(raw_transaction, encode_transaction))
        break
    else:
        print("ok i:{} raw_transaction:{}".format(i, raw_transaction))
    time.sleep(3)
    break
