# coding:utf-8

import time

from pybtmsdk import BytomAPI
from pybtmsdk.transaction import decode_raw_tx, encode_raw_tx
from pybtmsdk.signature import generate_signatures_use_mnemonic

url = 'http://0.0.0.0:9888'
url = 'http://47.101.140.15:9888'
access_token = 'YOUR_ACCESS_TOKEN'

api = BytomAPI(url=url)

print(api.chain_status())

'''
{"status":"success","data":{"current_height":124499,"current_hash":"ac85913c881956eb3827f73eb49f14b4e3587c58a660a48d1826b8f31246057f","finalized_height":124300,"finalized_hash":"668dc002d7a854f2833f6fe10c2576822be571fa5f3bb6c86dfa0dc63f59a44f","justified_height":124400,"justified_hash":"a557180b79791687c91c4b1c2d35b909010e7a220f03935a5be5b9894f58bdd9"}}
'''

print(api.list_contracts())

'''
{"status":"success","data":[]}
'''

# print(api.create_key("alice", "123456", "en"))
'''
{'status': 'success', 'data': {'alias': 'alice', 'xpub': '30f51840c620cb510067f62d64e8b7a3914ba4a6147ec886ec4c8067eeabc9142ad80e22d164eebf701adb001bc2928111c0ae1963e810e0f7b731b1e716ce58', 'file': '/Users/szh/bytom/solonet/keystore/UTC--2021-07-13T08-34-57.071898000Z--81aa9568-cb6a-49b5-a4b6-b6cffd72df2f', 'mnemonic': 'engage hobby light arrow basket boost dolphin squeeze cost virus twice fever'}}
Object(alias='alice', xpub='30f51840c620cb510067f62d64e8b7a3914ba4a6147ec886ec4c8067eeabc9142ad80e22d164eebf701adb001bc2928111c0ae1963e810e0f7b731b1e716ce58', file='/Users/szh/bytom/solonet/keystore/UTC--2021-07-13T08-34-57.071898000Z--81aa9568-cb6a-49b5-a4b6-b6cffd72df2f', mnemonic='engage hobby light arrow basket boost dolphin squeeze cost virus twice fever')
'''
# print(api.update_key_alias("24a877a92463a87f849215195052a9e4715a5bfaa6aa509df90e99c85f482652b7bcd4bd7c5de6884efc044505fda598ded64f9ed7657331da44e9631bb53f10",
#                            "abcde", return_dict=True))

# print(api.update_key_alias("24a877a92463a87f849215195052a9e4715a5bfaa6aa509df90e99c85f482652b7bcd4bd7c5de6884efc044505fda598ded64f9ed7657331da44e9631bb53f10",
#                            "abcde", return_dict=True))
#


# print(api.list_keys(return_dict=True))
'''
{'status': 'success', 'data': [{'alias': 'ipqhjjybj', 'xpub': 'e8f60df830801929b5486b7270d3be928f3e20441585864738630b53b72dba82b0d0d5036a93cef482aa5873d310f98caea5dc35c6f162648715c81dfee554ea', 'file': '/Users/szh/bytom/solonet/keystore/UTC--2021-07-13T06-17-27.033237000Z--aef9f6a5-716a-41b7-81e6-3d79aef5b9ff'}, {'alias': 'ipqhjjybj2', 'xpub': 'e812f8a13637d4fd8729dab0fb1fc58691400a79a48f793fa2f15d925953d824f4e9d5d2f97270a008985939c607bb4f22650b7a26b64f13d4f116eda4656c23', 'file': '/Users/szh/bytom/solonet/keystore/UTC--2021-07-13T06-19-42.055673000Z--7ec9a1ad-4b66-4aca-b234-789543df0110'}, {'alias': 'abcde', 'xpub': '24a877a92463a87f849215195052a9e4715a5bfaa6aa509df90e99c85f482652b7bcd4bd7c5de6884efc044505fda598ded64f9ed7657331da44e9631bb53f10', 'file': '/Users/szh/bytom/solonet/keystore/UTC--2021-07-13T06-51-09.045419000Z--3a51cad5-84fe-4a07-a7ad-76b5a22f2c06'}]}
[{'alias': 'ipqhjjybj', 'xpub': 'e8f60df830801929b5486b7270d3be928f3e20441585864738630b53b72dba82b0d0d5036a93cef482aa5873d310f98caea5dc35c6f162648715c81dfee554ea', 'file': '/Users/szh/bytom/solonet/keystore/UTC--2021-07-13T06-17-27.033237000Z--aef9f6a5-716a-41b7-81e6-3d79aef5b9ff'}, {'alias': 'ipqhjjybj2', 'xpub': 'e812f8a13637d4fd8729dab0fb1fc58691400a79a48f793fa2f15d925953d824f4e9d5d2f97270a008985939c607bb4f22650b7a26b64f13d4f116eda4656c23', 'file': '/Users/szh/bytom/solonet/keystore/UTC--2021-07-13T06-19-42.055673000Z--7ec9a1ad-4b66-4aca-b234-789543df0110'}, {'alias': 'abcde', 'xpub': '24a877a92463a87f849215195052a9e4715a5bfaa6aa509df90e99c85f482652b7bcd4bd7c5de6884efc044505fda598ded64f9ed7657331da44e9631bb53f10', 'file': '/Users/szh/bytom/solonet/keystore/UTC--2021-07-13T06-51-09.045419000Z--3a51cad5-84fe-4a07-a7ad-76b5a22f2c06'}]
'''

# print(api.delete_key(xpub="24a877a92463a87f849215195052a9e4715a5bfaa6aa509df90e99c85f482652b7bcd4bd7c5de6884efc044505fda598ded64f9ed7657331da44e9631bb53f10", password="123456", return_dict=True))
'''
{'status': 'success'}
{}
'''

# print(api.check_key_password(xpub="30f51840c620cb510067f62d64e8b7a3914ba4a6147ec886ec4c8067eeabc9142ad80e22d164eebf701adb001bc2928111c0ae1963e810e0f7b731b1e716ce58", password="12345", return_dict=True))
'''
{'status': 'success', 'data': {'check_result': False}}
{'check_result': False}
'''

# print(api.reset_key_password(xpub="30f51840c620cb510067f62d64e8b7a3914ba4a6147ec886ec4c8067eeabc9142ad80e22d164eebf701adb001bc2928111c0ae1963e810e0f7b731b1e716ce58", old_password="12345", new_password="123456"))
'''
{'status': 'success', 'data': {'changed': False}}
Object(changed=False)
'''

# print(api.create_account(root_xpubs=["f6a16704f745a168642712060e6c5a69866147e21ec2447ae628f87d756bb68cc9b91405ad0a95f004090e864fde472f62ba97053ea109837bc89d63a64040d5"], alias="abc", quorum=1, return_dict=True))
'''
{'status': 'success', 'data': {'id': '1SA5RPG0G0A02', 'alias': 'abc', 'xpubs': ['f6a16704f745a168642712060e6c5a69866147e21ec2447ae628f87d756bb68cc9b91405ad0a95f004090e864fde472f62ba97053ea109837bc89d63a64040d5'], 'quorum': 1, 'key_index': 1, 'derive_rule': 1}}
{'id': '1SA5RPG0G0A02', 'alias': 'abc', 'xpubs': ['f6a16704f745a168642712060e6c5a69866147e21ec2447ae628f87d756bb68cc9b91405ad0a95f004090e864fde472f62ba97053ea109837bc89d63a64040d5'], 'quorum': 1, 'key_index': 1, 'derive_rule': 1}
'''

# print(api.update_account_alias(account_id="1SA5RPG0G0A02", account_alias="abc", new_alias="abcd"))
'''
{'status': 'success'}
None
'''

# print(api.list_accounts(id="1SA5RPG0G0A02", alias="abcd"))
'''
{'status': 'success', 'data': [{'id': '1SA5RPG0G0A02', 'alias': 'abcd', 'xpubs': ['f6a16704f745a168642712060e6c5a69866147e21ec2447ae628f87d756bb68cc9b91405ad0a95f004090e864fde472f62ba97053ea109837bc89d63a64040d5'], 'quorum': 1, 'key_index': 1, 'derive_rule': 1}]}
[Object(id='1SA5RPG0G0A02', alias='abcd', xpubs=['f6a16704f745a168642712060e6c5a69866147e21ec2447ae628f87d756bb68cc9b91405ad0a95f004090e864fde472f62ba97053ea109837bc89d63a64040d5'], quorum=1, key_index=1, derive_rule=1)]
'''

# print(api.delete_account(account_id="1SA5RPG0G0A02", account_alias="abcd"))
'''
{'status': 'success'}
None
'''

# print(api.create_account_receiver(account_alias="abc", account_id="1SA7BVVQG0A02"))
'''
{'status': 'success', 'data': {'control_program': '0014462adc0c3aa6ad7b12e110b03477acded3455aa3', 'address': 'sm1qgc4dcrp656khkyhpzzcrgaavmmf52k4r5mdkmv'}}
Object(control_program='0014462adc0c3aa6ad7b12e110b03477acded3455aa3', address='sm1qgc4dcrp656khkyhpzzcrgaavmmf52k4r5mdkmv')
'''

# print(api.list_addresses(account_id="1SA7BVVQG0A02", account_alias="abc"))
'''
{'status': 'success', 'data': [{'account_alias': 'abc', 'account_id': '1SA7BVVQG0A02', 'address': 'sm1qgc4dcrp656khkyhpzzcrgaavmmf52k4r5mdkmv', 'control_program': '0014462adc0c3aa6ad7b12e110b03477acded3455aa3', 'change': False, 'key_index': 1}]}
[Object(account_alias='abc', account_id='1SA7BVVQG0A02', address='sm1qgc4dcrp656khkyhpzzcrgaavmmf52k4r5mdkmv', control_program='0014462adc0c3aa6ad7b12e110b03477acded3455aa3', change=False, key_index=1)]
'''

# print(api.validate_address(address="sm1qgc4dcrp656khkyhpzzcrgaavmmf52k4r5mdkmv"))
'''
{'status': 'success', 'data': {'valid': True, 'is_local': True}}
Object(valid=True, is_local=True)
'''

# print(api.list_pubkeys(account_alias="abc", account_id="1SA7BVVQG0A02"))
'''
{'status': 'success', 'data': {'root_xpub': 'f6a16704f745a168642712060e6c5a69866147e21ec2447ae628f87d756bb68cc9b91405ad0a95f004090e864fde472f62ba97053ea109837bc89d63a64040d5', 'pubkey_infos': [{'pubkey': 'fba4ca68b0cf7c261900d5c3665b123b4c3fb9286594e3417a337e03a7deb9ae', 'derivation_path': ['2c000000', '99000000', '02000000', '00000000', '01000000']}]}}
Object(root_xpub='f6a16704f745a168642712060e6c5a69866147e21ec2447ae628f87d756bb68cc9b91405ad0a95f004090e864fde472f62ba97053ea109837bc89d63a64040d5', pubkey_infos=[Object(pubkey='fba4ca68b0cf7c261900d5c3665b123b4c3fb9286594e3417a337e03a7deb9ae', derivation_path=['2c000000', '99000000', '02000000', '00000000', '01000000'])])
'''

# print(api.get_mining_address())
'''
{'status': 'success', 'data': {'mining_address': 'sm1qfgrgle0ljfxs0zlprf5q02zs9v3zdrcv6tmuvx'}}
Object(mining_address='sm1qfgrgle0ljfxs0zlprf5q02zs9v3zdrcv6tmuvx')
'''

# print(api.set_mining_address("sm1qfgrgle0ljfxs0zlprf5q02zs9v3zdrcv6tmuvx"))
'''
{'status': 'success', 'data': {'mining_address': 'sm1qfgrgle0ljfxs0zlprf5q02zs9v3zdrcv6tmuvx'}}
Object(mining_address='sm1qfgrgle0ljfxs0zlprf5q02zs9v3zdrcv6tmuvx')
'''

# print(api.create_asset(alias="btc", root_xpubs=["f6a16704f745a168642712060e6c5a69866147e21ec2447ae628f87d756bb68cc9b91405ad0a95f004090e864fde472f62ba97053ea109837bc89d63a64040d5"],
#                        quorum=1, definition={}, limit_height=100, issuance_program="0014462adc0c3aa6ad7b12e110b03477acded3455aa3"))

'''
{'status': 'success', 'data': {'type': '', 'xpubs': None, 'quorum': 0, 'key_index': 0, 'derive_rule': 0, 'id': '8854fadf7eab02a2a0e38232395e8ca7065eeaa6c7729350724265953d7623bf', 'alias': 'BTC', 'vm_version': 1, 'issue_program': '0014462adc0c3aa6ad7b12e110b03477acded3455aa3', 'raw_definition_byte': '7b7d', 'definition': {}, 'limit_height': 0}}
Object(type='', xpubs=None, quorum=0, key_index=0, derive_rule=0, id='8854fadf7eab02a2a0e38232395e8ca7065eeaa6c7729350724265953d7623bf', alias='BTC', vm_version=1, issue_program='0014462adc0c3aa6ad7b12e110b03477acded3455aa3', raw_definition_byte='7b7d', definition=Object(), limit_height=0)
'''

# print(api.get_asset(id="8854fadf7eab02a2a0e38232395e8ca7065eeaa6c7729350724265953d7623bf"))
'''
{'status': 'success', 'data': {'type': '', 'xpubs': None, 'quorum': 0, 'key_index': 0, 'derive_rule': 0, 'id': '8854fadf7eab02a2a0e38232395e8ca7065eeaa6c7729350724265953d7623bf', 'alias': 'BTC', 'vm_version': 1, 'issue_program': '0014462adc0c3aa6ad7b12e110b03477acded3455aa3', 'raw_definition_byte': '7b7d', 'definition': {}, 'limit_height': 0}}
Object(type='', xpubs=None, quorum=0, key_index=0, derive_rule=0, id='8854fadf7eab02a2a0e38232395e8ca7065eeaa6c7729350724265953d7623bf', alias='BTC', vm_version=1, issue_program='0014462adc0c3aa6ad7b12e110b03477acded3455aa3', raw_definition_byte='7b7d', definition=Object(), limit_height=0)
'''

# print(api.list_assets())
'''
{'status': 'success', 'data': [{'type': 'internal', 'xpubs': None, 'quorum': 0, 'key_index': 0, 'derive_rule': 0, 'id': 'ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff', 'alias': 'BTM', 'vm_version': 1, 'issue_program': '', 'raw_definition_byte': '7b0a202022646563696d616c73223a20382c0a2020226465736372697074696f6e223a20224279746f6d204f6666696369616c204973737565222c0a2020226e616d65223a202242544d222c0a20202273796d626f6c223a202242544d220a7d', 'definition': {'decimals': 8, 'description': 'Bytom Official Issue', 'name': 'BTM', 'symbol': 'BTM'}, 'limit_height': 0}, {'type': '', 'xpubs': None, 'quorum': 0, 'key_index': 0, 'derive_rule': 0, 'id': '8854fadf7eab02a2a0e38232395e8ca7065eeaa6c7729350724265953d7623bf', 'alias': 'BTC', 'vm_version': 1, 'issue_program': '0014462adc0c3aa6ad7b12e110b03477acded3455aa3', 'raw_definition_byte': '7b7d', 'definition': {}, 'limit_height': 0}]}
[Object(type='internal', xpubs=None, quorum=0, key_index=0, derive_rule=0, id='ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff', alias='BTM', vm_version=1, issue_program='', raw_definition_byte='7b0a202022646563696d616c73223a20382c0a2020226465736372697074696f6e223a20224279746f6d204f6666696369616c204973737565222c0a2020226e616d65223a202242544d222c0a20202273796d626f6c223a202242544d220a7d', definition=Object(decimals=8, description='Bytom Official Issue', name='BTM', symbol='BTM'), limit_height=0), Object(type='', xpubs=None, quorum=0, key_index=0, derive_rule=0, id='8854fadf7eab02a2a0e38232395e8ca7065eeaa6c7729350724265953d7623bf', alias='BTC', vm_version=1, issue_program='0014462adc0c3aa6ad7b12e110b03477acded3455aa3', raw_definition_byte='7b7d', definition=Object(), limit_height=0)]
'''

# print(api.update_asset_alias(id="8854fadf7eab02a2a0e38232395e8ca7065eeaa6c7729350724265953d7623bf", alias="BTCD"))
'''
{'status': 'success'}
None
'''

# print(api.list_balances(account_id="1SA0QDN500A02", account_alias="ipqhjjybj"))
'''
{'status': 'success', 'data': []}
[]
{'status': 'success', 'data': [{'account_id': '1SA0QDN500A02', 'account_alias': 'ipqhjjybj', 'asset_alias': 'BTM', 'asset_id': 'ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff', 'amount': 114155250800, 'asset_definition': {'decimals': 8, 'description': 'Bytom Official Issue', 'name': 'BTM', 'symbol': 'BTM'}}]}
[Object(account_id='1SA0QDN500A02', account_alias='ipqhjjybj', asset_alias='BTM', asset_id='ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff', amount=114155250800, asset_definition=Object(decimals=8, description='Bytom Official Issue', name='BTM', symbol='BTM'))]
'''

# id="", unconfirmed="", smart_contract="",
# print(api.list_unspent_outputs(account_id="1SA0QDN500A02", account_alias="ipqhjjybj"))
'''
{'status': 'success', 'data': [{'account_alias': 'ipqhjjybj', 'id': 'bbb7a8db617b1c5aaed1384123e76fad3a708301143b11836f545db7b351762d', 'asset_id': 'ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff', 'asset_alias': 'BTM', 'amount': 28538812700, 'account_id': '1SA0QDN500A02', 'address': 'sm1qfgrgle0ljfxs0zlprf5q02zs9v3zdrcv6tmuvx', 'control_program_index': 2, 'program': '00144a068fe5ff924d078be11a6807a8502b22268f0c', 'source_id': '088f6fb47aee1c1922158a513ee84d485a4042afa05c81001a6444c475fe9de1', 'source_pos': 0, 'valid_height': 201, 'change': False, 'derive_rule': 0}, {'account_alias': 'ipqhjjybj', 'id': '761f3474a74ec730d7dcb02c8ef608dd16dfde800cfca5f323040d9411c2096e', 'asset_id': 'ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff', 'asset_alias': 'BTM', 'amount': 28538812700, 'account_id': '1SA0QDN500A02', 'address': 'sm1qfgrgle0ljfxs0zlprf5q02zs9v3zdrcv6tmuvx', 'control_program_index': 2, 'program': '00144a068fe5ff924d078be11a6807a8502b22268f0c', 'source_id': 'c0daf9b0c070cb6e8e9b19b05e1971f34f32daf8ef281c1736fa0a5a09270e4f', 'source_pos': 0, 'valid_height': 401, 'change': False, 'derive_rule': 0}, {'account_alias': 'ipqhjjybj', 'id': '59edf3d053e1e38d2a291e6c93d76363c542fb0198e8bf4f6f4ec585c0eb365e', 'asset_id': 'ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff', 'asset_alias': 'BTM', 'amount': 28538812700, 'account_id': '1SA0QDN500A02', 'address': 'sm1qfgrgle0ljfxs0zlprf5q02zs9v3zdrcv6tmuvx', 'control_program_index': 2, 'program': '00144a068fe5ff924d078be11a6807a8502b22268f0c', 'source_id': 'e0fd1b060c12b675f40ce56b9f4c40ffd909fdbabb28f5eb69774e8acd8994da', 'source_pos': 0, 'valid_height': 501, 'change': False, 'derive_rule': 0}, {'account_alias': 'ipqhjjybj', 'id': '1ebafbdb9200f8030cf102ea997d359cafd25fb0aca2c79785d7e812771cf2c9', 'asset_id': 'ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff', 'asset_alias': 'BTM', 'amount': 28538812700, 'account_id': '1SA0QDN500A02', 'address': 'sm1qfgrgle0ljfxs0zlprf5q02zs9v3zdrcv6tmuvx', 'control_program_index': 2, 'program': '00144a068fe5ff924d078be11a6807a8502b22268f0c', 'source_id': 'e7f8a61047a82a4623616fc6dfe34cf01feff3c8279d99d88cb1485b0c42d21b', 'source_pos': 0, 'valid_height': 301, 'change': False, 'derive_rule': 0}]}
[Object(account_alias='ipqhjjybj', id='bbb7a8db617b1c5aaed1384123e76fad3a708301143b11836f545db7b351762d', asset_id='ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff', asset_alias='BTM', amount=28538812700, account_id='1SA0QDN500A02', address='sm1qfgrgle0ljfxs0zlprf5q02zs9v3zdrcv6tmuvx', control_program_index=2, program='00144a068fe5ff924d078be11a6807a8502b22268f0c', source_id='088f6fb47aee1c1922158a513ee84d485a4042afa05c81001a6444c475fe9de1', source_pos=0, valid_height=201, change=False, derive_rule=0), Object(account_alias='ipqhjjybj', id='761f3474a74ec730d7dcb02c8ef608dd16dfde800cfca5f323040d9411c2096e', asset_id='ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff', asset_alias='BTM', amount=28538812700, account_id='1SA0QDN500A02', address='sm1qfgrgle0ljfxs0zlprf5q02zs9v3zdrcv6tmuvx', control_program_index=2, program='00144a068fe5ff924d078be11a6807a8502b22268f0c', source_id='c0daf9b0c070cb6e8e9b19b05e1971f34f32daf8ef281c1736fa0a5a09270e4f', source_pos=0, valid_height=401, change=False, derive_rule=0), Object(account_alias='ipqhjjybj', id='59edf3d053e1e38d2a291e6c93d76363c542fb0198e8bf4f6f4ec585c0eb365e', asset_id='ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff', asset_alias='BTM', amount=28538812700, account_id='1SA0QDN500A02', address='sm1qfgrgle0ljfxs0zlprf5q02zs9v3zdrcv6tmuvx', control_program_index=2, program='00144a068fe5ff924d078be11a6807a8502b22268f0c', source_id='e0fd1b060c12b675f40ce56b9f4c40ffd909fdbabb28f5eb69774e8acd8994da', source_pos=0, valid_height=501, change=False, derive_rule=0), Object(account_alias='ipqhjjybj', id='1ebafbdb9200f8030cf102ea997d359cafd25fb0aca2c79785d7e812771cf2c9', asset_id='ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff', asset_alias='BTM', amount=28538812700, account_id='1SA0QDN500A02', address='sm1qfgrgle0ljfxs0zlprf5q02zs9v3zdrcv6tmuvx', control_program_index=2, program='00144a068fe5ff924d078be11a6807a8502b22268f0c', source_id='e7f8a61047a82a4623616fc6dfe34cf01feff3c8279d99d88cb1485b0c42d21b', source_pos=0, valid_height=301, change=False, derive_rule=0)]
'''

# print(api.list_account_votes(account_id="1SA0QDN500A02", account_alias="ipqhjjybj"))
'''
{'status': 'success', 'data': []}
[]
'''

# print(api.backup_wallet())
'''
{'status': 'success', 'data': {'account_image': {'slices': [{'account': {'type': 'account', 'xpubs': ['e8f60df830801929b5486b7270d3be928f3e20441585864738630b53b72dba82b0d0d5036a93cef482aa5873d310f98caea5dc35c6f162648715c81dfee554ea'], 'quorum': 1, 'key_index': 1, 'derive_rule': 1, 'id': '1SA0QDN500A02', 'alias': 'ipqhjjybj'}, 'contract_index': 0}, {'account': {'type': 'account', 'xpubs': ['e812f8a13637d4fd8729dab0fb1fc58691400a79a48f793fa2f15d925953d824f4e9d5d2f97270a008985939c607bb4f22650b7a26b64f13d4f116eda4656c23'], 'quorum': 1, 'key_index': 1, 'derive_rule': 1, 'id': '1SA0SFK500A04', 'alias': 'ipqhjjybj2'}, 'contract_index': 0}, {'account': {'type': 'account', 'xpubs': ['f6a16704f745a168642712060e6c5a69866147e21ec2447ae628f87d756bb68cc9b91405ad0a95f004090e864fde472f62ba97053ea109837bc89d63a64040d5'], 'quorum': 1, 'key_index': 2, 'derive_rule': 1, 'id': '1SA7BVVQG0A02', 'alias': 'abc'}, 'contract_index': 0}]}, 'asset_image': {'assets': [{'id': '8854fadf7eab02a2a0e38232395e8ca7065eeaa6c7729350724265953d7623bf', 'alias': 'BTCD', 'vm_version': 1, 'issue_program': '0014462adc0c3aa6ad7b12e110b03477acded3455aa3', 'raw_definition_byte': '7b7d', 'definition': {}}]}, 'key_images': {'xkeys': [{'crypto': {'cipher': 'aes-128-ctr', 'ciphertext': '8485c70d91b719e21167799718c56a4ebc8a8ef2c35f02e81bbf27f41989c61d7b5cef657a49495444ccdaaf38de164635cfd4a9a9cd079fbc546209aba50e3f', 'cipherparams': {'iv': '6e66df610f2e8280e238be0c37cd8177'}, 'kdf': 'scrypt', 'kdfparams': {'dklen': 32, 'n': 4096, 'p': 6, 'r': 8, 'salt': '8591609750fa6e8200f66a27ae436d163f877a2f7a74efca890139068058faf1'}, 'mac': 'd5a95b41c17d30c8224faf3fe21ddcb3c4c5ab080435faed47b7b7ff6ee97516'}, 'id': 'aef9f6a5-716a-41b7-81e6-3d79aef5b9ff', 'type': 'bytom_kd', 'version': 1, 'alias': 'ipqhjjybj', 'xpub': 'e8f60df830801929b5486b7270d3be928f3e20441585864738630b53b72dba82b0d0d5036a93cef482aa5873d310f98caea5dc35c6f162648715c81dfee554ea'}, {'crypto': {'cipher': 'aes-128-ctr', 'ciphertext': 'e5715918f432ac32df903c6b02fa4ba0895b8ae3a5d59e49be0d714d2f9d09292e6afe92187ad6e40012273dc2b3049cd30e69e82e08998ed87bbdf314e57e20', 'cipherparams': {'iv': '36526fd8d421c542066823d3a9e987ec'}, 'kdf': 'scrypt', 'kdfparams': {'dklen': 32, 'n': 4096, 'p': 6, 'r': 8, 'salt': '32252a26bf33d83755a315d638c69152a9262f8e036ea457a704e6d945f676b7'}, 'mac': 'fc86e57545313a83fdd0d2c0dd1b35ebbcfbc85cfb1a2c4618946dc2000c307b'}, 'id': '7ec9a1ad-4b66-4aca-b234-789543df0110', 'type': 'bytom_kd', 'version': 1, 'alias': 'ipqhjjybj2', 'xpub': 'e812f8a13637d4fd8729dab0fb1fc58691400a79a48f793fa2f15d925953d824f4e9d5d2f97270a008985939c607bb4f22650b7a26b64f13d4f116eda4656c23'}, {'crypto': {'cipher': 'aes-128-ctr', 'ciphertext': '5206060b2b453ab6371e21d5ce6f6072af14359878794484b71acec5c6927dfb645f8100e8fdafcdd4903ddf32874422acbf207d3c3a9891e26d4d90e151378e', 'cipherparams': {'iv': 'f4dfa487989569d26556cbb7640ac77a'}, 'kdf': 'scrypt', 'kdfparams': {'dklen': 32, 'n': 4096, 'p': 6, 'r': 8, 'salt': '4fe773c408100d8145bf50f7e6e73e31025876b5cce8baae1f34db6ee94f6612'}, 'mac': '7cbe4773b08220f97352d53d751a70fcb0fa00df0b864f89bd06305c340655a7'}, 'id': '81aa9568-cb6a-49b5-a4b6-b6cffd72df2f', 'type': 'bytom_kd', 'version': 1, 'alias': 'alice', 'xpub': '30f51840c620cb510067f62d64e8b7a3914ba4a6147ec886ec4c8067eeabc9142ad80e22d164eebf701adb001bc2928111c0ae1963e810e0f7b731b1e716ce58'}]}}}
Object(account_image=Object(slices=[Object(account=Object(type='account', xpubs=['e8f60df830801929b5486b7270d3be928f3e20441585864738630b53b72dba82b0d0d5036a93cef482aa5873d310f98caea5dc35c6f162648715c81dfee554ea'], quorum=1, key_index=1, derive_rule=1, id='1SA0QDN500A02', alias='ipqhjjybj'), contract_index=0), Object(account=Object(type='account', xpubs=['e812f8a13637d4fd8729dab0fb1fc58691400a79a48f793fa2f15d925953d824f4e9d5d2f97270a008985939c607bb4f22650b7a26b64f13d4f116eda4656c23'], quorum=1, key_index=1, derive_rule=1, id='1SA0SFK500A04', alias='ipqhjjybj2'), contract_index=0), Object(account=Object(type='account', xpubs=['f6a16704f745a168642712060e6c5a69866147e21ec2447ae628f87d756bb68cc9b91405ad0a95f004090e864fde472f62ba97053ea109837bc89d63a64040d5'], quorum=1, key_index=2, derive_rule=1, id='1SA7BVVQG0A02', alias='abc'), contract_index=0)]), asset_image=Object(assets=[Object(id='8854fadf7eab02a2a0e38232395e8ca7065eeaa6c7729350724265953d7623bf', alias='BTCD', vm_version=1, issue_program='0014462adc0c3aa6ad7b12e110b03477acded3455aa3', raw_definition_byte='7b7d', definition=Object())]), key_images=Object(xkeys=[Object(crypto=Object(cipher='aes-128-ctr', ciphertext='8485c70d91b719e21167799718c56a4ebc8a8ef2c35f02e81bbf27f41989c61d7b5cef657a49495444ccdaaf38de164635cfd4a9a9cd079fbc546209aba50e3f', cipherparams=Object(iv='6e66df610f2e8280e238be0c37cd8177'), kdf='scrypt', kdfparams=Object(dklen=32, n=4096, p=6, r=8, salt='8591609750fa6e8200f66a27ae436d163f877a2f7a74efca890139068058faf1'), mac='d5a95b41c17d30c8224faf3fe21ddcb3c4c5ab080435faed47b7b7ff6ee97516'), id='aef9f6a5-716a-41b7-81e6-3d79aef5b9ff', type='bytom_kd', version=1, alias='ipqhjjybj', xpub='e8f60df830801929b5486b7270d3be928f3e20441585864738630b53b72dba82b0d0d5036a93cef482aa5873d310f98caea5dc35c6f162648715c81dfee554ea'), Object(crypto=Object(cipher='aes-128-ctr', ciphertext='e5715918f432ac32df903c6b02fa4ba0895b8ae3a5d59e49be0d714d2f9d09292e6afe92187ad6e40012273dc2b3049cd30e69e82e08998ed87bbdf314e57e20', cipherparams=Object(iv='36526fd8d421c542066823d3a9e987ec'), kdf='scrypt', kdfparams=Object(dklen=32, n=4096, p=6, r=8, salt='32252a26bf33d83755a315d638c69152a9262f8e036ea457a704e6d945f676b7'), mac='fc86e57545313a83fdd0d2c0dd1b35ebbcfbc85cfb1a2c4618946dc2000c307b'), id='7ec9a1ad-4b66-4aca-b234-789543df0110', type='bytom_kd', version=1, alias='ipqhjjybj2', xpub='e812f8a13637d4fd8729dab0fb1fc58691400a79a48f793fa2f15d925953d824f4e9d5d2f97270a008985939c607bb4f22650b7a26b64f13d4f116eda4656c23'), Object(crypto=Object(cipher='aes-128-ctr', ciphertext='5206060b2b453ab6371e21d5ce6f6072af14359878794484b71acec5c6927dfb645f8100e8fdafcdd4903ddf32874422acbf207d3c3a9891e26d4d90e151378e', cipherparams=Object(iv='f4dfa487989569d26556cbb7640ac77a'), kdf='scrypt', kdfparams=Object(dklen=32, n=4096, p=6, r=8, salt='4fe773c408100d8145bf50f7e6e73e31025876b5cce8baae1f34db6ee94f6612'), mac='7cbe4773b08220f97352d53d751a70fcb0fa00df0b864f89bd06305c340655a7'), id='81aa9568-cb6a-49b5-a4b6-b6cffd72df2f', type='bytom_kd', version=1, alias='alice', xpub='30f51840c620cb510067f62d64e8b7a3914ba4a6147ec886ec4c8067eeabc9142ad80e22d164eebf701adb001bc2928111c0ae1963e810e0f7b731b1e716ce58')]))
'''

# print(api.restore_wallet(account_image="", "asset_image", "key_images"))

# print(api.rescan_wallet())
'''
{'status': 'success'}
None
'''

# print(api.wallet_info())
'''
{'status': 'success', 'data': {'best_block_height': 432, 'wallet_height': 432}}
Object(best_block_height=432, wallet_height=432)
'''

# print(api.recovery_wallet(xpubs=['e8f60df830801929b5486b7270d3be928f3e20441585864738630b53b72dba82b0d0d5036a93cef482aa5873d310f98caea5dc35c6f162648715c81dfee554ea']))
'''
{'status': 'success'}
None
'''

# print(api.sign_message(address="sm1qfgrgle0ljfxs0zlprf5q02zs9v3zdrcv6tmuvx", message="abcd", password="86458043"))
'''
{'status': 'success', 'data': {'signature': '91d27b6e5e7c4a1844a80899e4bea179a6a02d9e1a29a371c892fc5fa4b2e08ed1f5b05dd08cad3a870c239614365e7ec3efc3ec08db1c24270db7b53dcdae09', 'derived_xpub': 'e464d86eedccec8887681416accf8361254007e9c75819cc9f9a0f44f8be376ebbf8f3bb3e26e97d636c6aa3f8eb0c790b845240113ceb16503bd2c8349d82b3'}}
Object(signature='91d27b6e5e7c4a1844a80899e4bea179a6a02d9e1a29a371c892fc5fa4b2e08ed1f5b05dd08cad3a870c239614365e7ec3efc3ec08db1c24270db7b53dcdae09', derived_xpub='e464d86eedccec8887681416accf8361254007e9c75819cc9f9a0f44f8be376ebbf8f3bb3e26e97d636c6aa3f8eb0c790b845240113ceb16503bd2c8349d82b3')
'''

# print(api.decode_program(program="0014462adc0c3aa6ad7b12e110b03477acded3455aa3"))
'''
{'status': 'success', 'data': {'instructions': 'DUP \nHASH160 \nDATA_20 462adc0c3aa6ad7b12e110b03477acded3455aa3\nEQUALVERIFY \nTXSIGHASH \nSWAP \nCHECKSIG \n'}}
Object(instructions='DUP \nHASH160 \nDATA_20 462adc0c3aa6ad7b12e110b03477acded3455aa3\nEQUALVERIFY \nTXSIGHASH \nSWAP \nCHECKSIG \n')
'''

# print(api.get_transaction(tx_id="f52c3e16747879471514df2dbfec7063d4bf34c0fd08ec094e0ba7a5e707bb2b"))
'''
{'status': 'success', 'data': {'tx_id': 'f52c3e16747879471514df2dbfec7063d4bf34c0fd08ec094e0ba7a5e707bb2b', 'block_time': 1626227886000, 'block_hash': 'b39fea622676f727fa5d7566642c0f19391bf1df8d840f26eed6d9dd98abb730', 'block_height': 527, 'block_index': 0, 'block_transactions_count': 1, 'inputs': [{'type': 'coinbase', 'asset_id': '0000000000000000000000000000000000000000000000000000000000000000', 'asset_definition': None, 'amount': 0, 'arbitrary': '00353237', 'input_id': 'd73da8eda907fe0314f01fe5910f32316e6580b8b341b0954402f1cb69720530', 'witness_arguments': None, 'sign_data': '0000000000000000000000000000000000000000000000000000000000000000'}], 'outputs': [{'type': 'control', 'id': '1979e57feda22efe713f25ae175624cf1f7ea1130936457d02a1c0155c67f8b1', 'position': 0, 'asset_id': 'ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff', 'asset_alias': 'BTM', 'asset_definition': {'decimals': 8, 'description': 'Bytom Official Issue', 'name': 'BTM', 'symbol': 'BTM'}, 'amount': 0, 'account_id': '1SA0QDN500A02', 'account_alias': 'ipqhjjybj', 'control_program': '00144a068fe5ff924d078be11a6807a8502b22268f0c', 'address': 'sm1qfgrgle0ljfxs0zlprf5q02zs9v3zdrcv6tmuvx'}], 'size': 76}}
Object(tx_id='f52c3e16747879471514df2dbfec7063d4bf34c0fd08ec094e0ba7a5e707bb2b', block_time=1626227886000, block_hash='b39fea622676f727fa5d7566642c0f19391bf1df8d840f26eed6d9dd98abb730', block_height=527, block_index=0, block_transactions_count=1, inputs=[Object(type='coinbase', asset_id='0000000000000000000000000000000000000000000000000000000000000000', asset_definition=None, amount=0, arbitrary='00353237', input_id='d73da8eda907fe0314f01fe5910f32316e6580b8b341b0954402f1cb69720530', witness_arguments=None, sign_data='0000000000000000000000000000000000000000000000000000000000000000')], outputs=[Object(type='control', id='1979e57feda22efe713f25ae175624cf1f7ea1130936457d02a1c0155c67f8b1', position=0, asset_id='ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff', asset_alias='BTM', asset_definition=Object(decimals=8, description='Bytom Official Issue', name='BTM', symbol='BTM'), amount=0, account_id='1SA0QDN500A02', account_alias='ipqhjjybj', control_program='00144a068fe5ff924d078be11a6807a8502b22268f0c', address='sm1qfgrgle0ljfxs0zlprf5q02zs9v3zdrcv6tmuvx')], size=76)
'''

# print(api.list_transactions(account_id="1SA0QDN500A02", count=2))
'''
{'status': 'success', 'data': [{'tx_id': '7e80560a4cabe8afdf52566e0ca16caf91fcfcd5897ee315660d939fe5c80fc1', 'block_time': 1626227988000, 'inputs': [{'type': 'coinbase', 'asset_id': '0000000000000000000000000000000000000000000000000000000000000000', 'arbitrary': '00353434'}], 'outputs': [{'type': 'control', 'asset_id': 'ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff', 'asset_alias': 'BTM', 'account_id': '1SA0QDN500A02', 'account_alias': 'ipqhjjybj'}]}, {'tx_id': '94a723b1ef1fbcc336648638ff9dfb770b5f6ca9fe2b61ac32053477899d56bf', 'block_time': 1626227982000, 'inputs': [{'type': 'coinbase', 'asset_id': '0000000000000000000000000000000000000000000000000000000000000000', 'arbitrary': '00353433'}], 'outputs': [{'type': 'control', 'asset_id': 'ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff', 'asset_alias': 'BTM', 'account_id': '1SA0QDN500A02', 'account_alias': 'ipqhjjybj'}]}]}
[Object(tx_id='7e80560a4cabe8afdf52566e0ca16caf91fcfcd5897ee315660d939fe5c80fc1', block_time=1626227988000, inputs=[Object(type='coinbase', asset_id='0000000000000000000000000000000000000000000000000000000000000000', arbitrary='00353434')], outputs=[Object(type='control', asset_id='ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff', asset_alias='BTM', account_id='1SA0QDN500A02', account_alias='ipqhjjybj')]), Object(tx_id='94a723b1ef1fbcc336648638ff9dfb770b5f6ca9fe2b61ac32053477899d56bf', block_time=1626227982000, inputs=[Object(type='coinbase', asset_id='0000000000000000000000000000000000000000000000000000000000000000', arbitrary='00353433')], outputs=[Object(type='control', asset_id='ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff', asset_alias='BTM', account_id='1SA0QDN500A02', account_alias='ipqhjjybj')])]
'''

actions = [
    {
        "account_id": "1SA0QDN500A02",
        "amount": 4000000,
        "asset_id": "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff",
        "type": "spend_account"
    },
    # {
    #   "account_id": "1QEPIO7OG0A02",
    #   "amount": 300000,
    #   "asset_id": asset_id,
    #   "type": "spend_account"
    # },
    {
        "amount": 2000000,
        "asset_id": "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff",
        "address": "sm1qfgrgle0ljfxs0zlprf5q02zs9v3zdrcv6tmuvx",
        "type": "control_address"
    }
]

# print(api.build_transaction(base_transaction=None, actions=actions, ttl=10, time_range=int(time.time()),
#                             return_dict=True))
'''
{'status': 'success', 'data': {'raw_transaction': '07018391b98706010161015f088f6fb47aee1c1922158a513ee84d485a4042afa05c81001a6444c475fe9de1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9cf2aea86a00011600144a068fe5ff924d078be11a6807a8502b22268f0c0001000201003effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8cefaea86a011600144a068fe5ff924d078be11a6807a8502b22268f0c000001003bffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc801011600144a068fe5ff924d078be11a6807a8502b22268f0c0000', 'signing_instructions': [{'position': 0, 'witness_components': [{'type': 'raw_tx_signature', 'quorum': 1, 'keys': [{'xpub': 'e8f60df830801929b5486b7270d3be928f3e20441585864738630b53b72dba82b0d0d5036a93cef482aa5873d310f98caea5dc35c6f162648715c81dfee554ea', 'derivation_path': ['2c000000', '99000000', '01000000', '00000000', '02000000']}], 'signatures': None}, {'type': 'data', 'value': 'e464d86eedccec8887681416accf8361254007e9c75819cc9f9a0f44f8be376e'}]}], 'fee': 200, 'allow_additional_actions': False}}
{'raw_transaction': '07018391b98706010161015f088f6fb47aee1c1922158a513ee84d485a4042afa05c81001a6444c475fe9de1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9cf2aea86a00011600144a068fe5ff924d078be11a6807a8502b22268f0c0001000201003effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8cefaea86a011600144a068fe5ff924d078be11a6807a8502b22268f0c000001003bffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc801011600144a068fe5ff924d078be11a6807a8502b22268f0c0000', 'signing_instructions': [{'position': 0, 'witness_components': [{'type': 'raw_tx_signature', 'quorum': 1, 'keys': [{'xpub': 'e8f60df830801929b5486b7270d3be928f3e20441585864738630b53b72dba82b0d0d5036a93cef482aa5873d310f98caea5dc35c6f162648715c81dfee554ea', 'derivation_path': ['2c000000', '99000000', '01000000', '00000000', '02000000']}], 'signatures': None}, {'type': 'data', 'value': 'e464d86eedccec8887681416accf8361254007e9c75819cc9f9a0f44f8be376e'}]}], 'fee': 200, 'allow_additional_actions': False}
'''

# print(api.build_chain_transactions(base_transaction=None, actions=actions, ttl=10,
#                                    time_range=int(time.time()), return_dict=True))
'''
{'status': 'success', 'data': [{'raw_transaction': '070100010161015f088f6fb47aee1c1922158a513ee84d485a4042afa05c81001a6444c475fe9de1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9cf2aea86a00011600144a068fe5ff924d078be11a6807a8502b22268f0c0001000201003effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8cefaea86a011600144a068fe5ff924d078be11a6807a8502b22268f0c000001003bffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc801011600144a068fe5ff924d078be11a6807a8502b22268f0c0000', 'signing_instructions': [{'position': 0, 'witness_components': [{'type': 'raw_tx_signature', 'quorum': 1, 'keys': [{'xpub': 'e8f60df830801929b5486b7270d3be928f3e20441585864738630b53b72dba82b0d0d5036a93cef482aa5873d310f98caea5dc35c6f162648715c81dfee554ea', 'derivation_path': ['2c000000', '99000000', '01000000', '00000000', '02000000']}], 'signatures': None}, {'type': 'data', 'value': 'e464d86eedccec8887681416accf8361254007e9c75819cc9f9a0f44f8be376e'}]}], 'fee': 200, 'allow_additional_actions': False}]}
[{'raw_transaction': '070100010161015f088f6fb47aee1c1922158a513ee84d485a4042afa05c81001a6444c475fe9de1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9cf2aea86a00011600144a068fe5ff924d078be11a6807a8502b22268f0c0001000201003effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8cefaea86a011600144a068fe5ff924d078be11a6807a8502b22268f0c000001003bffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc801011600144a068fe5ff924d078be11a6807a8502b22268f0c0000', 'signing_instructions': [{'position': 0, 'witness_components': [{'type': 'raw_tx_signature', 'quorum': 1, 'keys': [{'xpub': 'e8f60df830801929b5486b7270d3be928f3e20441585864738630b53b72dba82b0d0d5036a93cef482aa5873d310f98caea5dc35c6f162648715c81dfee554ea', 'derivation_path': ['2c000000', '99000000', '01000000', '00000000', '02000000']}], 'signatures': None}, {'type': 'data', 'value': 'e464d86eedccec8887681416accf8361254007e9c75819cc9f9a0f44f8be376e'}]}], 'fee': 200, 'allow_additional_actions': False}]
'''

# template = api.build_transaction(base_transaction=None, actions=actions, ttl=10, time_range=1521625823, return_dict=True)
# print(api.sign_transaction(password="86458043", transaction=template))

'''
{'status': 'success', 'data': {'transaction': {'raw_transaction': '0701dfd5c8d505010161015f088f6fb47aee1c1922158a513ee84d485a4042afa05c81001a6444c475fe9de1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9cf2aea86a00011600144a068fe5ff924d078be11a6807a8502b22268f0c00630240043ad4ab765ebb576fef12e76c24b37ec86e667f62c8cd0fa758611cee009798bec0e26d7c4af4ac11ca8293b3fd7cc9b158a7b8f17245bbd2e6bd45f4030b0d20e464d86eedccec8887681416accf8361254007e9c75819cc9f9a0f44f8be376e0201003effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8cefaea86a011600144a068fe5ff924d078be11a6807a8502b22268f0c000001003bffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc801011600144a068fe5ff924d078be11a6807a8502b22268f0c0000', 'signing_instructions': [{'position': 0, 'witness_components': [{'type': 'raw_tx_signature', 'quorum': 1, 'keys': [{'xpub': 'e8f60df830801929b5486b7270d3be928f3e20441585864738630b53b72dba82b0d0d5036a93cef482aa5873d310f98caea5dc35c6f162648715c81dfee554ea', 'derivation_path': ['2c000000', '99000000', '01000000', '00000000', '02000000']}], 'signatures': ['043ad4ab765ebb576fef12e76c24b37ec86e667f62c8cd0fa758611cee009798bec0e26d7c4af4ac11ca8293b3fd7cc9b158a7b8f17245bbd2e6bd45f4030b0d']}, {'type': 'data', 'value': 'e464d86eedccec8887681416accf8361254007e9c75819cc9f9a0f44f8be376e'}]}], 'fee': 200, 'allow_additional_actions': False}, 'sign_complete': True}}
Object(transaction=Object(raw_transaction='0701dfd5c8d505010161015f088f6fb47aee1c1922158a513ee84d485a4042afa05c81001a6444c475fe9de1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9cf2aea86a00011600144a068fe5ff924d078be11a6807a8502b22268f0c00630240043ad4ab765ebb576fef12e76c24b37ec86e667f62c8cd0fa758611cee009798bec0e26d7c4af4ac11ca8293b3fd7cc9b158a7b8f17245bbd2e6bd45f4030b0d20e464d86eedccec8887681416accf8361254007e9c75819cc9f9a0f44f8be376e0201003effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8cefaea86a011600144a068fe5ff924d078be11a6807a8502b22268f0c000001003bffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc801011600144a068fe5ff924d078be11a6807a8502b22268f0c0000', signing_instructions=[Object(position=0, witness_components=[Object(type='raw_tx_signature', quorum=1, keys=[Object(xpub='e8f60df830801929b5486b7270d3be928f3e20441585864738630b53b72dba82b0d0d5036a93cef482aa5873d310f98caea5dc35c6f162648715c81dfee554ea', derivation_path=['2c000000', '99000000', '01000000', '00000000', '02000000'])], signatures=['043ad4ab765ebb576fef12e76c24b37ec86e667f62c8cd0fa758611cee009798bec0e26d7c4af4ac11ca8293b3fd7cc9b158a7b8f17245bbd2e6bd45f4030b0d']), Object(type='data', value='e464d86eedccec8887681416accf8361254007e9c75819cc9f9a0f44f8be376e')])], fee=200, allow_additional_actions=False), sign_complete=True)
'''

# template = api.build_transaction(base_transaction=None, actions=actions, ttl=10, time_range=1521625823, return_dict=True)
# print(api.sign_transactions(password="86458043", transactions=[template]))

'''
{'status': 'success', 'data': {'transaction': [{'raw_transaction': '0701dfd5c8d505010161015f088f6fb47aee1c1922158a513ee84d485a4042afa05c81001a6444c475fe9de1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9cf2aea86a00011600144a068fe5ff924d078be11a6807a8502b22268f0c00630240043ad4ab765ebb576fef12e76c24b37ec86e667f62c8cd0fa758611cee009798bec0e26d7c4af4ac11ca8293b3fd7cc9b158a7b8f17245bbd2e6bd45f4030b0d20e464d86eedccec8887681416accf8361254007e9c75819cc9f9a0f44f8be376e0201003effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8cefaea86a011600144a068fe5ff924d078be11a6807a8502b22268f0c000001003bffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc801011600144a068fe5ff924d078be11a6807a8502b22268f0c0000', 'signing_instructions': [{'position': 0, 'witness_components': [{'type': 'raw_tx_signature', 'quorum': 1, 'keys': [{'xpub': 'e8f60df830801929b5486b7270d3be928f3e20441585864738630b53b72dba82b0d0d5036a93cef482aa5873d310f98caea5dc35c6f162648715c81dfee554ea', 'derivation_path': ['2c000000', '99000000', '01000000', '00000000', '02000000']}], 'signatures': ['043ad4ab765ebb576fef12e76c24b37ec86e667f62c8cd0fa758611cee009798bec0e26d7c4af4ac11ca8293b3fd7cc9b158a7b8f17245bbd2e6bd45f4030b0d']}, {'type': 'data', 'value': 'e464d86eedccec8887681416accf8361254007e9c75819cc9f9a0f44f8be376e'}]}], 'fee': 200, 'allow_additional_actions': False}], 'sign_complete': True}}
Object(transaction=[Object(raw_transaction='0701dfd5c8d505010161015f088f6fb47aee1c1922158a513ee84d485a4042afa05c81001a6444c475fe9de1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9cf2aea86a00011600144a068fe5ff924d078be11a6807a8502b22268f0c00630240043ad4ab765ebb576fef12e76c24b37ec86e667f62c8cd0fa758611cee009798bec0e26d7c4af4ac11ca8293b3fd7cc9b158a7b8f17245bbd2e6bd45f4030b0d20e464d86eedccec8887681416accf8361254007e9c75819cc9f9a0f44f8be376e0201003effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8cefaea86a011600144a068fe5ff924d078be11a6807a8502b22268f0c000001003bffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc801011600144a068fe5ff924d078be11a6807a8502b22268f0c0000', signing_instructions=[Object(position=0, witness_components=[Object(type='raw_tx_signature', quorum=1, keys=[Object(xpub='e8f60df830801929b5486b7270d3be928f3e20441585864738630b53b72dba82b0d0d5036a93cef482aa5873d310f98caea5dc35c6f162648715c81dfee554ea', derivation_path=['2c000000', '99000000', '01000000', '00000000', '02000000'])], signatures=['043ad4ab765ebb576fef12e76c24b37ec86e667f62c8cd0fa758611cee009798bec0e26d7c4af4ac11ca8293b3fd7cc9b158a7b8f17245bbd2e6bd45f4030b0d']), Object(type='data', value='e464d86eedccec8887681416accf8361254007e9c75819cc9f9a0f44f8be376e')])], fee=200, allow_additional_actions=False)], sign_complete=True)
'''

template = api.build_transaction(base_transaction=None, actions=actions, ttl=10, time_range=1521625823, return_dict=True)
data = api.sign_transaction(password="86458043", transaction=template, return_dict=True)
print(api.submit_transaction(raw_transaction=data["transaction"]["raw_transaction"]))

'''
{"status":"success","data":{"raw_transaction":"0701dfd5c8d505010161015fa3b5efee4fe6d913b818295df4148fe0ff0b026d2f0a74ceefa0b6cfd0797018ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9cf2aea86a00011600144a068fe5ff924d078be11a6807a8502b22268f0c0001000201003effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ce0baa66a011600144a068fe5ff924d078be11a6807a8502b22268f0c000001003cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff80897a011600144a068fe5ff924d078be11a6807a8502b22268f0c0000","signing_instructions":[{"position":0,"witness_components":[{"type":"raw_tx_signature","quorum":1,"keys":[{"xpub":"e8f60df830801929b5486b7270d3be928f3e20441585864738630b53b72dba82b0d0d5036a93cef482aa5873d310f98caea5dc35c6f162648715c81dfee554ea","derivation_path":["2c000000","99000000","01000000","00000000","02000000"]}],"signatures":null},{"type":"data","value":"e464d86eedccec8887681416accf8361254007e9c75819cc9f9a0f44f8be376e"}]}],"fee":2000000,"allow_additional_actions":false}}

{'status': 'success', 'data': {'raw_transaction': '0701dfd5c8d505010161015fa3b5efee4fe6d913b818295df4148fe0ff0b026d2f0a74ceefa0b6cfd0797018ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9cf2aea86a00011600144a068fe5ff924d078be11a6807a8502b22268f0c0001000201003effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ce0baa66a011600144a068fe5ff924d078be11a6807a8502b22268f0c000001003cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff80897a011600144a068fe5ff924d078be11a6807a8502b22268f0c0000', 'signing_instructions': [{'position': 0, 'witness_components': [{'type': 'raw_tx_signature', 'quorum': 1, 'keys': [{'xpub': 'e8f60df830801929b5486b7270d3be928f3e20441585864738630b53b72dba82b0d0d5036a93cef482aa5873d310f98caea5dc35c6f162648715c81dfee554ea', 'derivation_path': ['2c000000', '99000000', '01000000', '00000000', '02000000']}], 'signatures': None}, {'type': 'data', 'value': 'e464d86eedccec8887681416accf8361254007e9c75819cc9f9a0f44f8be376e'}]}], 'fee': 2000000, 'allow_additional_actions': False}}
http://0.0.0.0:9888/sign-transaction
{"status":"success","data":{"transaction":{"raw_transaction":"0701dfd5c8d505010161015fa3b5efee4fe6d913b818295df4148fe0ff0b026d2f0a74ceefa0b6cfd0797018ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9cf2aea86a00011600144a068fe5ff924d078be11a6807a8502b22268f0c006302403dde9df8bb6398835e63b9a151d465466bca62a97e3c80bc12c6d5814230b5c17e70ad3845cdd1d5547f9a1f34084d25cde85679da7a142dcac7bfbabc38730a20e464d86eedccec8887681416accf8361254007e9c75819cc9f9a0f44f8be376e0201003effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ce0baa66a011600144a068fe5ff924d078be11a6807a8502b22268f0c000001003cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff80897a011600144a068fe5ff924d078be11a6807a8502b22268f0c0000","signing_instructions":[{"position":0,"witness_components":[{"type":"raw_tx_signature","quorum":1,"keys":[{"xpub":"e8f60df830801929b5486b7270d3be928f3e20441585864738630b53b72dba82b0d0d5036a93cef482aa5873d310f98caea5dc35c6f162648715c81dfee554ea","derivation_path":["2c000000","99000000","01000000","00000000","02000000"]}],"signatures":["3dde9df8bb6398835e63b9a151d465466bca62a97e3c80bc12c6d5814230b5c17e70ad3845cdd1d5547f9a1f34084d25cde85679da7a142dcac7bfbabc38730a"]},{"type":"data","value":"e464d86eedccec8887681416accf8361254007e9c75819cc9f9a0f44f8be376e"}]}],"fee":2000000,"allow_additional_actions":false},"sign_complete":true}}

{'status': 'success', 'data': {'transaction': {'raw_transaction': '0701dfd5c8d505010161015fa3b5efee4fe6d913b818295df4148fe0ff0b026d2f0a74ceefa0b6cfd0797018ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9cf2aea86a00011600144a068fe5ff924d078be11a6807a8502b22268f0c006302403dde9df8bb6398835e63b9a151d465466bca62a97e3c80bc12c6d5814230b5c17e70ad3845cdd1d5547f9a1f34084d25cde85679da7a142dcac7bfbabc38730a20e464d86eedccec8887681416accf8361254007e9c75819cc9f9a0f44f8be376e0201003effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ce0baa66a011600144a068fe5ff924d078be11a6807a8502b22268f0c000001003cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff80897a011600144a068fe5ff924d078be11a6807a8502b22268f0c0000', 'signing_instructions': [{'position': 0, 'witness_components': [{'type': 'raw_tx_signature', 'quorum': 1, 'keys': [{'xpub': 'e8f60df830801929b5486b7270d3be928f3e20441585864738630b53b72dba82b0d0d5036a93cef482aa5873d310f98caea5dc35c6f162648715c81dfee554ea', 'derivation_path': ['2c000000', '99000000', '01000000', '00000000', '02000000']}], 'signatures': ['3dde9df8bb6398835e63b9a151d465466bca62a97e3c80bc12c6d5814230b5c17e70ad3845cdd1d5547f9a1f34084d25cde85679da7a142dcac7bfbabc38730a']}, {'type': 'data', 'value': 'e464d86eedccec8887681416accf8361254007e9c75819cc9f9a0f44f8be376e'}]}], 'fee': 2000000, 'allow_additional_actions': False}, 'sign_complete': True}}
{'transaction': {'raw_transaction': '0701dfd5c8d505010161015fa3b5efee4fe6d913b818295df4148fe0ff0b026d2f0a74ceefa0b6cfd0797018ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9cf2aea86a00011600144a068fe5ff924d078be11a6807a8502b22268f0c006302403dde9df8bb6398835e63b9a151d465466bca62a97e3c80bc12c6d5814230b5c17e70ad3845cdd1d5547f9a1f34084d25cde85679da7a142dcac7bfbabc38730a20e464d86eedccec8887681416accf8361254007e9c75819cc9f9a0f44f8be376e0201003effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ce0baa66a011600144a068fe5ff924d078be11a6807a8502b22268f0c000001003cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff80897a011600144a068fe5ff924d078be11a6807a8502b22268f0c0000', 'signing_instructions': [{'position': 0, 'witness_components': [{'type': 'raw_tx_signature', 'quorum': 1, 'keys': [{'xpub': 'e8f60df830801929b5486b7270d3be928f3e20441585864738630b53b72dba82b0d0d5036a93cef482aa5873d310f98caea5dc35c6f162648715c81dfee554ea', 'derivation_path': ['2c000000', '99000000', '01000000', '00000000', '02000000']}], 'signatures': ['3dde9df8bb6398835e63b9a151d465466bca62a97e3c80bc12c6d5814230b5c17e70ad3845cdd1d5547f9a1f34084d25cde85679da7a142dcac7bfbabc38730a']}, {'type': 'data', 'value': 'e464d86eedccec8887681416accf8361254007e9c75819cc9f9a0f44f8be376e'}]}], 'fee': 2000000, 'allow_additional_actions': False}, 'sign_complete': True}
http://0.0.0.0:9888/submit-transaction
{"status":"success","data":{"tx_id":"0e2ce865c77af38ad70119c4eb7e0f74d8071c28428d39f4b238a87519a6a416"}}

{'status': 'success', 'data': {'tx_id': '0e2ce865c77af38ad70119c4eb7e0f74d8071c28428d39f4b238a87519a6a416'}}
Object(tx_id='0e2ce865c77af38ad70119c4eb7e0f74d8071c28428d39f4b238a87519a6a416')

'''

# template = api.build_transaction(base_transaction=None, actions=actions, ttl=10, time_range=1521625823, return_dict=True)
# data = api.sign_transaction(password="86458043", transaction=template, return_dict=True)
# print(api.submit_transactions(raw_transactions=[data["transaction"]["raw_transaction"]]))
'''
{"status":"success","data":{"raw_transaction":"0701dfd5c8d505010161015f758e3ae2dae6417296202ac4ab8c2ccc206b01056bac023c418a2e7ea01eb124ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ce0baa66a00011600144a068fe5ff924d078be11a6807a8502b22268f0c0001000201003effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ccec6a46a011600144a068fe5ff924d078be11a6807a8502b22268f0c000001003cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff80897a011600144a068fe5ff924d078be11a6807a8502b22268f0c0000","signing_instructions":[{"position":0,"witness_components":[{"type":"raw_tx_signature","quorum":1,"keys":[{"xpub":"e8f60df830801929b5486b7270d3be928f3e20441585864738630b53b72dba82b0d0d5036a93cef482aa5873d310f98caea5dc35c6f162648715c81dfee554ea","derivation_path":["2c000000","99000000","01000000","00000000","02000000"]}],"signatures":null},{"type":"data","value":"e464d86eedccec8887681416accf8361254007e9c75819cc9f9a0f44f8be376e"}]}],"fee":2000000,"allow_additional_actions":false}}

{'status': 'success', 'data': {'raw_transaction': '0701dfd5c8d505010161015f758e3ae2dae6417296202ac4ab8c2ccc206b01056bac023c418a2e7ea01eb124ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ce0baa66a00011600144a068fe5ff924d078be11a6807a8502b22268f0c0001000201003effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ccec6a46a011600144a068fe5ff924d078be11a6807a8502b22268f0c000001003cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff80897a011600144a068fe5ff924d078be11a6807a8502b22268f0c0000', 'signing_instructions': [{'position': 0, 'witness_components': [{'type': 'raw_tx_signature', 'quorum': 1, 'keys': [{'xpub': 'e8f60df830801929b5486b7270d3be928f3e20441585864738630b53b72dba82b0d0d5036a93cef482aa5873d310f98caea5dc35c6f162648715c81dfee554ea', 'derivation_path': ['2c000000', '99000000', '01000000', '00000000', '02000000']}], 'signatures': None}, {'type': 'data', 'value': 'e464d86eedccec8887681416accf8361254007e9c75819cc9f9a0f44f8be376e'}]}], 'fee': 2000000, 'allow_additional_actions': False}}
http://0.0.0.0:9888/sign-transaction
{"status":"success","data":{"transaction":{"raw_transaction":"0701dfd5c8d505010161015f758e3ae2dae6417296202ac4ab8c2ccc206b01056bac023c418a2e7ea01eb124ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ce0baa66a00011600144a068fe5ff924d078be11a6807a8502b22268f0c00630240fd7fe115767d8034f0a6db8a9884fe2a44a5c0a7a1ccd87c8efae8e684fda13fc6d4aa2a80d859b3b3edf7439b5400e5f43a61aca2d6c378427072d5ccdb0e0b20e464d86eedccec8887681416accf8361254007e9c75819cc9f9a0f44f8be376e0201003effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ccec6a46a011600144a068fe5ff924d078be11a6807a8502b22268f0c000001003cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff80897a011600144a068fe5ff924d078be11a6807a8502b22268f0c0000","signing_instructions":[{"position":0,"witness_components":[{"type":"raw_tx_signature","quorum":1,"keys":[{"xpub":"e8f60df830801929b5486b7270d3be928f3e20441585864738630b53b72dba82b0d0d5036a93cef482aa5873d310f98caea5dc35c6f162648715c81dfee554ea","derivation_path":["2c000000","99000000","01000000","00000000","02000000"]}],"signatures":["fd7fe115767d8034f0a6db8a9884fe2a44a5c0a7a1ccd87c8efae8e684fda13fc6d4aa2a80d859b3b3edf7439b5400e5f43a61aca2d6c378427072d5ccdb0e0b"]},{"type":"data","value":"e464d86eedccec8887681416accf8361254007e9c75819cc9f9a0f44f8be376e"}]}],"fee":2000000,"allow_additional_actions":false},"sign_complete":true}}

{'status': 'success', 'data': {'transaction': {'raw_transaction': '0701dfd5c8d505010161015f758e3ae2dae6417296202ac4ab8c2ccc206b01056bac023c418a2e7ea01eb124ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ce0baa66a00011600144a068fe5ff924d078be11a6807a8502b22268f0c00630240fd7fe115767d8034f0a6db8a9884fe2a44a5c0a7a1ccd87c8efae8e684fda13fc6d4aa2a80d859b3b3edf7439b5400e5f43a61aca2d6c378427072d5ccdb0e0b20e464d86eedccec8887681416accf8361254007e9c75819cc9f9a0f44f8be376e0201003effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ccec6a46a011600144a068fe5ff924d078be11a6807a8502b22268f0c000001003cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff80897a011600144a068fe5ff924d078be11a6807a8502b22268f0c0000', 'signing_instructions': [{'position': 0, 'witness_components': [{'type': 'raw_tx_signature', 'quorum': 1, 'keys': [{'xpub': 'e8f60df830801929b5486b7270d3be928f3e20441585864738630b53b72dba82b0d0d5036a93cef482aa5873d310f98caea5dc35c6f162648715c81dfee554ea', 'derivation_path': ['2c000000', '99000000', '01000000', '00000000', '02000000']}], 'signatures': ['fd7fe115767d8034f0a6db8a9884fe2a44a5c0a7a1ccd87c8efae8e684fda13fc6d4aa2a80d859b3b3edf7439b5400e5f43a61aca2d6c378427072d5ccdb0e0b']}, {'type': 'data', 'value': 'e464d86eedccec8887681416accf8361254007e9c75819cc9f9a0f44f8be376e'}]}], 'fee': 2000000, 'allow_additional_actions': False}, 'sign_complete': True}}
http://0.0.0.0:9888/submit-transactions
{"status":"success","data":{"tx_id":["da1a21d35e08b4c377df2220a9b593d0dd17f3b4bd915f2884e8a1460619da53"]}}

{'status': 'success', 'data': {'tx_id': ['da1a21d35e08b4c377df2220a9b593d0dd17f3b4bd915f2884e8a1460619da53']}}
Object(tx_id=['da1a21d35e08b4c377df2220a9b593d0dd17f3b4bd915f2884e8a1460619da53'])
'''

# template = api.build_transaction(base_transaction=None, actions=actions, ttl=10, time_range=1521625823, return_dict=True)
# print(api.estimate_transaction_gas(transaction_template=template))
'''
{'status': 'success', 'data': {'total_neu': 993600, 'flexible_neu': 336600, 'storage_neu': 93400, 'vm_neu': 563600, 'chain_tx_neu': 0}}
Object(total_neu=993600, flexible_neu=336600, storage_neu=93400, vm_neu=563600, chain_tx_neu=0)
'''

# template = api.build_transaction(base_transaction=None, actions=actions, ttl=10, time_range=1521625823, return_dict=True)
# print(api.estimate_chain_transaction_gas(transaction_templates=[template]))
'''
{"status":"success","data":{"total_neu":993600,"flexible_neu":336600,"storage_neu":93400,"vm_neu":563600,"chain_tx_neu":0}}
Object(total_neu=993600, flexible_neu=336600, storage_neu=93400, vm_neu=563600, chain_tx_neu=0)
'''

#print(api.create_access_token(id="token1"))
'''
{"status":"success","data":{"id":"token1","token":"token1:e464e843f50b91011c3627d02b5682614a5917060debb928735ad038858264ce","created_at":"2021-07-14T10:45:15.844982+08:00"}}
Object(id='token1', token='token1:e464e843f50b91011c3627d02b5682614a5917060debb928735ad038858264ce', created_at='2021-07-14T10:45:15.844982+08:00')
Object(id='token1', token='token1:6ef74364d492f972d168ff679263734eb1ee7d10c9668d8b8f093f71373e9bbf', created_at='2021-07-14T10:47:55.285026+08:00')
{"status":"fail","code":"BTM000","msg":"Bytom API Error","error_detail":"invalid token"}

'''

#print(api.list_access_tokens())
'''
{"status":"success","data":[{"id":"token1","token":"token1:e464e843f50b91011c3627d02b5682614a5917060debb928735ad038858264ce","created_at":"2021-07-14T10:45:15.844982+08:00"}]}
[Object(id='token1', token='token1:e464e843f50b91011c3627d02b5682614a5917060debb928735ad038858264ce', created_at='2021-07-14T10:45:15.844982+08:00')]
'''

#print(api.delete_access_token(id="token1"))
'''
{"status":"success"}
None
'''

#print(api.check_access_token(id="token1", secret="6ef74364d492f972d168ff679263734eb1ee7d10c9668d8b8f093f71373e9bbf"))
'''
{"status":"success"}
None
'''

# print(api.create_contract(alias="", ))

# print(api.create_transaction_feed(alias="test1"))
'''
{"status":"success"}
None
'''

#print(api.get_transaction_feed(alias="test1"))
'''
{"status":"success","data":{"txfeed":{"alias":"test1","param":{}}}}
Object(txfeed=Object(alias='test1', param=Object()))
'''

#print(api.list_transaction_feeds())
'''
{"status":"success","data":[{"alias":"test1","param":{}}]}
[Object(alias='test1', param=Object())]
'''

#print(api.delete_transaction_feed(alias="test1"))
'''
{"status":"success"}
None
'''

#print(api.update_transaction_feed(alias="test1"))
'''
{"status":"success"}
None
'''

#print(api.get_unconfirmed_transaction(tx_id="7ffc6e2f206b1480123627061872405cda8cc87a8f79d3e5dc2b43afbc121218"))
'''
{"status":"fail","code":"BTM000","msg":"Bytom API Error","error_detail":"transaction are not existed in the mempool"}
'''

#print(api.list_unconfirmed_transactions())
'''
{"status":"success","data":{"total":0,"tx_ids":[]}}
Object(total=0, tx_ids=[])
'''

#print(api.decode_raw_transaction(raw_transaction="0701dfd5c8d505010161015f758e3ae2dae6417296202ac4ab8c2ccc206b01056bac023c418a2e7ea01eb124ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ce0baa66a00011600144a068fe5ff924d078be11a6807a8502b22268f0c0001000201003effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9ccec6a46a011600144a068fe5ff924d078be11a6807a8502b22268f0c000001003cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff80897a011600144a068fe5ff924d078be11a6807a8502b22268f0c0000"))
'''
{"status":"success","data":{"tx_id":"da1a21d35e08b4c377df2220a9b593d0dd17f3b4bd915f2884e8a1460619da53","version":1,"size":240,"time_range":1521625823,"inputs":[{"type":"spend","asset_id":"ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff","asset_definition":{},"amount":28534812700,"control_program":"00144a068fe5ff924d078be11a6807a8502b22268f0c","address":"sm1qfgrgle0ljfxs0zlprf5q02zs9v3zdrcv6tmuvx","spent_output_id":"2ad50c4ced9d418675b0bf0cf4a963d74fbf729796f9e09ef8a8894da2bd524e","input_id":"3b3a328c8efe96f97363fddc1c4a66b713922ea07f1bced7e1435c68a639d6b3","witness_arguments":null,"sign_data":"2ad24339b33bebf7b64561a51ad74490b0fcbc3d3ebd58fc911b2897116accf6"}],"outputs":[{"type":"control","id":"e254b57328255b0c8126e4d41a92f0b6cd51e8833a938e1f90f62a186e895f37","position":0,"asset_id":"ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff","asset_definition":{},"amount":28530812700,"control_program":"00144a068fe5ff924d078be11a6807a8502b22268f0c","address":"sm1qfgrgle0ljfxs0zlprf5q02zs9v3zdrcv6tmuvx"},{"type":"control","id":"dc9d12c22b783fa0b0d26699bd7a5d0a119dcc37bff240d2ed8ec478f636945c","position":1,"asset_id":"ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff","asset_definition":{},"amount":2000000,"control_program":"00144a068fe5ff924d078be11a6807a8502b22268f0c","address":"sm1qfgrgle0ljfxs0zlprf5q02zs9v3zdrcv6tmuvx"}],"fee":2000000}}
Object(tx_id='da1a21d35e08b4c377df2220a9b593d0dd17f3b4bd915f2884e8a1460619da53', version=1, size=240, time_range=1521625823, inputs=[Object(type='spend', asset_id='ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff', asset_definition=Object(), amount=28534812700, control_program='00144a068fe5ff924d078be11a6807a8502b22268f0c', address='sm1qfgrgle0ljfxs0zlprf5q02zs9v3zdrcv6tmuvx', spent_output_id='2ad50c4ced9d418675b0bf0cf4a963d74fbf729796f9e09ef8a8894da2bd524e', input_id='3b3a328c8efe96f97363fddc1c4a66b713922ea07f1bced7e1435c68a639d6b3', witness_arguments=None, sign_data='2ad24339b33bebf7b64561a51ad74490b0fcbc3d3ebd58fc911b2897116accf6')], outputs=[Object(type='control', id='e254b57328255b0c8126e4d41a92f0b6cd51e8833a938e1f90f62a186e895f37', position=0, asset_id='ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff', asset_definition=Object(), amount=28530812700, control_program='00144a068fe5ff924d078be11a6807a8502b22268f0c', address='sm1qfgrgle0ljfxs0zlprf5q02zs9v3zdrcv6tmuvx'), Object(type='control', id='dc9d12c22b783fa0b0d26699bd7a5d0a119dcc37bff240d2ed8ec478f636945c', position=1, asset_id='ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff', asset_definition=Object(), amount=2000000, control_program='00144a068fe5ff924d078be11a6807a8502b22268f0c', address='sm1qfgrgle0ljfxs0zlprf5q02zs9v3zdrcv6tmuvx')], fee=2000000)
'''

#print(api.get_block_count())
'''
{"status":"success","data":{"block_count":742}}
Object(block_count=742)
'''

#print(api.get_block_hash())
'''
{"status":"success","data":{"block_hash":"fc2930d964474df7182734c6e6e18afa235634772e22f0a76480d1ccd73b4cc9"}}
Object(block_hash='fc2930d964474df7182734c6e6e18afa235634772e22f0a76480d1ccd73b4cc9')
'''

#print(api.get_block())
'''
{"status":"success","data":{"hash":"1615de51985135e0df820351bdf8da42c2eb42ba28e4bd6a9a3c6c6559cda5db","size":448,"version":1,"height":0,"validator":"","previous_block_hash":"0000000000000000000000000000000000000000000000000000000000000000","timestamp":1528945000000,"transaction_merkle_root":"0118f65d7940f8874191fbf83c50dc45988e29c2e741e617ae019ae41356a684","transactions":[{"id":"59cbf59079fcbf26b0a24d4bbf614c74bd06338c9001219abed662525f3a8166","version":1,"size":145,"time_range":0,"inputs":[{"type":"coinbase","asset_id":"0000000000000000000000000000000000000000000000000000000000000000","asset_definition":{},"amount":0,"arbitrary":"496e666f726d6174696f6e20697320706f7765722e202d2d204a616e2f31312f323031332e20436f6d707574696e6720697320706f7765722e202d2d204170722f32342f323031382e","input_id":"953b17a15c82cc524e0e25230736a512809dc1a5fe6c0b29747fa2de2e2d64b4","witness_arguments":null,"sign_data":"0000000000000000000000000000000000000000000000000000000000000000"}],"outputs":[{"type":"control","id":"a57153a4bf0cf00dfd4896022e4918634b7a99ed81393d624bb09fc0e3be2b95","position":0,"asset_id":"ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff","asset_definition":{},"amount":0,"control_program":"00148c9d063ff74ee6d9ffa88d83aeb038068366c4c4","address":"sm1q3jwsv0lhfmndnlag3kp6avpcq6pkd3xyxg7z8f"}],"mux_id":"3c93cef5366c1dff8f09cb3a33f45c309bfb86037209d66bb6dc2c21b65d6352"}]}}
Object(hash='1615de51985135e0df820351bdf8da42c2eb42ba28e4bd6a9a3c6c6559cda5db', size=448, version=1, height=0, validator='', previous_block_hash='0000000000000000000000000000000000000000000000000000000000000000', timestamp=1528945000000, transaction_merkle_root='0118f65d7940f8874191fbf83c50dc45988e29c2e741e617ae019ae41356a684', transactions=[Object(id='59cbf59079fcbf26b0a24d4bbf614c74bd06338c9001219abed662525f3a8166', version=1, size=145, time_range=0, inputs=[Object(type='coinbase', asset_id='0000000000000000000000000000000000000000000000000000000000000000', asset_definition=Object(), amount=0, arbitrary='496e666f726d6174696f6e20697320706f7765722e202d2d204a616e2f31312f323031332e20436f6d707574696e6720697320706f7765722e202d2d204170722f32342f323031382e', input_id='953b17a15c82cc524e0e25230736a512809dc1a5fe6c0b29747fa2de2e2d64b4', witness_arguments=None, sign_data='0000000000000000000000000000000000000000000000000000000000000000')], outputs=[Object(type='control', id='a57153a4bf0cf00dfd4896022e4918634b7a99ed81393d624bb09fc0e3be2b95', position=0, asset_id='ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff', asset_definition=Object(), amount=0, control_program='00148c9d063ff74ee6d9ffa88d83aeb038068366c4c4', address='sm1q3jwsv0lhfmndnlag3kp6avpcq6pkd3xyxg7z8f')], mux_id='3c93cef5366c1dff8f09cb3a33f45c309bfb86037209d66bb6dc2c21b65d6352')])
'''

#print(api.get_raw_block())
'''
{"status":"success","data":{"raw_block":"0301000000000000000000000000000000000000000000000000000000000000000000c0fce4e1bf2c200118f65d7940f8874191fbf83c50dc45988e29c2e741e617ae019ae41356a684010001000107010001014b0249496e666f726d6174696f6e20697320706f7765722e202d2d204a616e2f31312f323031332e20436f6d707574696e6720697320706f7765722e202d2d204170722f32342f323031382e000101003affffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00011600148c9d063ff74ee6d9ffa88d83aeb038068366c4c40000"}}
Object(raw_block='0301000000000000000000000000000000000000000000000000000000000000000000c0fce4e1bf2c200118f65d7940f8874191fbf83c50dc45988e29c2e741e617ae019ae41356a684010001000107010001014b0249496e666f726d6174696f6e20697320706f7765722e202d2d204a616e2f31312f323031332e20436f6d707574696e6720697320706f7765722e202d2d204170722f32342f323031382e000101003affffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff00011600148c9d063ff74ee6d9ffa88d83aeb038068366c4c40000')
'''

#print(api.get_block_header())
'''
{"status":"success","data":{"block_header":"0101000000000000000000000000000000000000000000000000000000000000000000c0fce4e1bf2c200118f65d7940f8874191fbf83c50dc45988e29c2e741e617ae019ae41356a68401000100","reward":0}}
Object(block_header='0101000000000000000000000000000000000000000000000000000000000000000000c0fce4e1bf2c200118f65d7940f8874191fbf83c50dc45988e29c2e741e617ae019ae41356a68401000100', reward=0)
'''

#print(api.is_mining())
'''
{"status":"success","data":{"is_mining":false}}
Object(is_mining=False)
'''

#print(api.set_mining(is_mining=True))
'''
{"status":"success","data":""}
None
'''

#print(api.net_info())
'''
{"status":"success","data":{"listening":true,"syncing":false,"mining":true,"node_xpub":"6b90db9ee85f76f8a246ae085337dab69b5bfc03c0fd4e8ac184b2944e83c994bce77b7d06d03af835fa98007788127fdb4ae507fe1a5903438eae91d91ea2ec","peer_count":0,"current_block":748,"highest_block":748,"finalized_block":600,"network_id":"solonet","version_info":{"version":"1.1.1+91e799b4","update":0,"new_version":"1.1.1+91e799b4"}}}
Object(listening=True, syncing=False, mining=True, node_xpub='6b90db9ee85f76f8a246ae085337dab69b5bfc03c0fd4e8ac184b2944e83c994bce77b7d06d03af835fa98007788127fdb4ae507fe1a5903438eae91d91ea2ec', peer_count=0, current_block=748, highest_block=748, finalized_block=600, network_id='solonet', version_info=Object(version='1.1.1+91e799b4', update=0, new_version='1.1.1+91e799b4'))
'''

# print(api.gas_rate())
'''
{"status":"success","data":{"gas_rate":200}}
Object(gas_rate=200)
'''

# print(api.verify_message("bm1qx2qgvvjz734ur8x5lpfdtlau74aaa5djs0a5jn", "6ff8c3d1321ce39a3c3550f57ba70b67dcbcef821e9b85f6150edb7f2f3f91009e67f3075e6e76ed5f657ee4b1a5f4749b7a8c74c8e7e6a1b0e5918ebd5df4d0", "this is a test message", "74da3d6572233736e3a439166719244dab57dd0047f8751b1efa2da26eeab251d915c1211dcad77e8b013267b86d96e91ae67ff0be520ef4ec326e911410b609"))


# print(api.list_peers())
'''
{"status":"success","data":[]}
[]
'''

# print(api.get_vote_result())
