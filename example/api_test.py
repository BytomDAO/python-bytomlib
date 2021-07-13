# coding:utf-8


from pybtmsdk import BytomAPI
from pybtmsdk.transaction import decode_raw_tx, encode_raw_tx
from pybtmsdk.signature import generate_signatures_use_mnemonic

url = 'http://0.0.0.0:9888'
access_token = 'YOUR_ACCESS_TOKEN'

api = BytomAPI(url=url)

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

#print(api.wallet_info())
'''
{'status': 'success', 'data': {'best_block_height': 432, 'wallet_height': 432}}
Object(best_block_height=432, wallet_height=432)
'''

#print(api.recovery_wallet(xpubs=['e8f60df830801929b5486b7270d3be928f3e20441585864738630b53b72dba82b0d0d5036a93cef482aa5873d310f98caea5dc35c6f162648715c81dfee554ea']))
'''
{'status': 'success'}
None
'''

print(api.sign_message)


