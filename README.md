pybtmsdk
======

- [1 Installation](#1-installation)
- [2 Usage](#2-usage)
  - [2.1 Create entropy](#21-create-entropy)
  - [2.2 Create mnemonics](#22-create-mnemonics)
  - [2.3 Create seed](#23-create-seed)
  - [2.4 Create root expanded private key](#24-create-root-expanded-private-key)
  - [2.5 Create expanded public key](#25-create-expanded-public-key)
  - [2.6 Create expanded private key](#26-create-expanded-private-key)
  - [2.7 Create public key](#27-create-public-key)
  - [2.8 Create child expanded private key](#28-create-child-expanded-private-key)
  - [2.9 Create child expanded public key](#29-create-child-expanded-public-key)
  - [2.10 Sign message](#210-sign-message)
  - [2.11 Verify signature](#211-verify-signature)
  - [2.12 Create new key](#212-create-new-key)
  - [2.13 Create HD path](#213-create-hd-path)
  - [2.14 Create control program](#214-create-control-program)
  - [2.15 Create address](#215-create-address)
  - [2.16 Create new address](#216-create-new-address)
  - [2.17 Submit raw transaction](#217-submit-raw-transaction)
  - [2.18 Decode raw transaction](#218-decode-raw-transaction)
- [3 Api](#3-api)
  - [3.1 Use api client](#31-use-api-client)

Python3 implementation of the Bytom protocol.


## 1 Installation

```
python3 setup.py install
```

Requires:

- Python>=3.7

## 2 Usage

### 2.1 Create entropy

get_entropy() create 128 bits entropy.

Return:

- entropy_hexstr: 128 bits entropy.

```python
>>> from pybtmsdk import key
>>> key.get_entropy()
'100e2704b431f914e3262926bdba6fce'
```

### 2.2 Create mnemonics

get_mnemonic create 12 new mnemonics.

Parameter:

- entropy_hexstr(optional): 128 bits entropy, type is hex string.

Return:

- mnemonic_str: 12 mnemonics.

```python
>>> key.get_mnemonic('089fe9bf0cac76760bc4b131d938669e')
'ancient young hurt bone shuffle deposit congress normal crack six boost despair'
```

If no paramater is specified, it will return 12 new random mnemonics.

```python
>>> from pybtmsdk import key
>>> key.get_mnemonic()
'nothing gate perfect glide wink lizard journey negative load quote wrong reason'
```

### 2.3 Create seed

get_seed create 512 bits seed from 12 mnemonics.

Parameter:

- mnemonic_str: 12 mnemonics.

Return:

- seed_hexstr: 512 bits seed, type is hex string.

```python
>>> from pybtmsdk import key
>>> key.get_seed('ancient young hurt bone shuffle deposit congress normal crack six boost despair')
'afa3a86bbec2f40bb32833fc6324593824c4fc7821ed32eac1f762b5893e56745f66a6c6f2588b3d627680aa4e0e50efd25065097b3daa8c6a19d606838fe7d4'
```

### 2.4 Create root expanded private key

get_root_xprv create root expanded private key.

Parameter:

- seed_hexstr: 512 bits seed, type is hex string.

Return:

- root_xprv_hexstring: 512 bits seed, type is hex string.

```python
>>> from pybtmsdk import key
>>> key.get_root_xprv('afa3a86bbec2f40bb32833fc6324593824c4fc7821ed32eac1f762b5893e56745f66a6c6f2588b3d627680aa4e0e50efd25065097b3daa8c6a19d606838fe7d4')
'302a25c7c0a68a83fa043f594a2db8b44bc871fced553a8a33144b31bc7fb84887c9e75915bb6ba3fd0b9f94a60b7a5897ab9db6a48f888c2559132dba9152b0'
```

### 2.5 Create expanded public key

get_xpub create expanded public key.

Parameter:

- xprv_hexstr: 512 bits expanded private key, type is hex string.

Return:

- xpub_hexstr: 512 bits expanded public key, type is hex string.

```python
>>> from pybtmsdk import key
>>> xprv_hexstr = 'c003f4bcccf9ad6f05ad2c84fa5ff98430eb8e73de5de232bc29334c7d074759d513bc370335cac51d77f0be5dfe84de024cfee562530b4d873b5f5e2ff4f57c'
>>> key.get_xpub(xprv_hexstr)
'1b0541a7664cee929edb54d9ef21996b90546918a920a77e1cd6015d97c56563d513bc370335cac51d77f0be5dfe84de024cfee562530b4d873b5f5e2ff4f57c'
```

### 2.6 Create expanded private key

get_expanded_private_key create expanded private key.

Parameter:

- xprv_hexstr: 512 bits expanded private key, type is hex string.

Return:

- expanded_private_key_hexstr: 512 bits expanded private key, type is hex string.

```python
>>> from pybtmsdk import key
>>> xprv_hexstr = '406c82307bf7978d17f3ecfeea7705370e9faef2027affa86c8027c6e11a8a50e231e65bd97048850ae6c39d0f46b63ae70aa24f5aac7877727c430c2201e6d6'
>>> key.get_expanded_private_key(xprv_hexstr)
'406c82307bf7978d17f3ecfeea7705370e9faef2027affa86c8027c6e11a8a50d828bf44b1a109c2bbb4c72685858e2f2ab8b405beef1e4ecc12d1ed8511e8eb'
```

### 2.7 Create public key

get_public_key create 32 bytes public key.

Parameter:

- xpub_hexstr: 512 bits expanded public key, type is hex string.

Return:

- public_key_hexstr: 256 bits public key, type is hex string.

```python
>>> from pybtmsdk import key
>>> xpub_hexstr = 'ecc2bbb6c0492873cdbc81edf56bd896d3b644047879840e357be735b7fa7b6f4af1be7b8d71cc649ac4ca3816f9ccaf11bf49f4effb845f3c19e16eaf8bfcda'
>>> key.get_public_key(xpub_hexstr)
'ecc2bbb6c0492873cdbc81edf56bd896d3b644047879840e357be735b7fa7b6f'
```

### 2.8 Create child expanded private key

get_child_xprv create child private key.

Parameter:

- xprv_hexstr: 512 bits expanded private key, type is hex string.
- path_list: 010203 7906a1

Return:

- child_xprv_hexstr: 512 bits private key, type is hex string.

```python
>>> from pybtmsdk import key
>>> xprv_hexstr = 'c003f4bcccf9ad6f05ad2c84fa5ff98430eb8e73de5de232bc29334c7d074759d513bc370335cac51d77f0be5dfe84de024cfee562530b4d873b5f5e2ff4f57c'
>>> path_list = ['010203', '7906a1']
>>> key.get_child_xprv(xprv_hexstr, path_list)
'4853a0b00bdcb139e85855d9594e5f641b65218db7c50426946511397e094759bd9de7f2dcad9d7d45389bc94baecaec88aabf58f6e1d832b1f9995a93ec37ea'
```

### 2.9 Create child expanded public key

get_child_xpub create child public key.

Parameter:

- xpub_hexstr: 512 bits expanded public key, type is hex string.
- path_list: 010203 7906a1

Return:

- child_xpub_hexstr: 512 bits public key, type is hex string.

```python
>>> from pybtmsdk import key
>>> xpub_hexstr = '1b0541a7664cee929edb54d9ef21996b90546918a920a77e1cd6015d97c56563d513bc370335cac51d77f0be5dfe84de024cfee562530b4d873b5f5e2ff4f57c'
>>> path_list = ['010203', '7906a1']
>>> key.get_child_xpub(xpub_hexstr, path_list)
'e65c1a9714e2116c6e5d57dee188a53b98dc901a21def5a5ca46fcf78303f4f2bd9de7f2dcad9d7d45389bc94baecaec88aabf58f6e1d832b1f9995a93ec37ea'
```

### 2.10 Sign message

xprv_sign sign message.

Parameter:

- xprv_hexstr: 512 bits expanded private key, type is hex string.
- message_hexstr: message, type is hex string.

Return:

- signature_hexstr: 512 bits signature, type is hex string.

```python
>>> from pybtmsdk import key
>>> xprv_hexstr = '88c0c40fb54ef9c1b90af8cce8dc4c9d54f915074dde93f79ab61cedae03444101ff37ac4a07869214c2735bba0175e001abe608db18538e083e1e44430a273b'
>>> message_hexstr = '1246b84985e1ab5f83f4ec2bdf271114666fd3d9e24d12981a3c861b9ed523c6'
>>> key.xprv_sign(xprv_hexstr, message_hexstr)
'ab18f49b23d03295bc2a3f2a7d5bb53a2997bed733e1fc408b50ec834ae7e43f7da40fe5d9d50f6ef2d188e1d27f976aa2586cef1ba00dd098b5c9effa046306'
```

### 2.11 Verify signature

xpub_verify verify signature.

Parameter:

- xpub_hexstr: 512 bits expanded public key, type is hex string.
- message_hexstr: message, type is hex string.
- signature_hexstr: 512 bits signature, type is hex string.

Return:

- result: True or False.

```python
>>> from pybtmsdk import key
>>> xpub_hexstr = 'cb22ce197d342d6bb440b0bf13ddd674f367275d28a00f893d7f0b10817690fd01ff37ac4a07869214c2735bba0175e001abe608db18538e083e1e44430a273b'
>>> message_hexstr = '1246b84985e1ab5f83f4ec2bdf271114666fd3d9e24d12981a3c861b9ed523c6'
>>> signature_hexstr = 'ab18f49b23d03295bc2a3f2a7d5bb53a2997bed733e1fc408b50ec834ae7e43f7da40fe5d9d50f6ef2d188e1d27f976aa2586cef1ba00dd098b5c9effa046306'
>>> key.xpub_verify(xpub_hexstr, message_hexstr, signature_hexstr)
True
```

### 2.12 Create new key

get_new_key create new key.

Parameter:

- entropy_hexstr(optional): 128 bits entropy, type is hex string.
- mnemonic_str(optional): 12 mnemonics.

Return:

- entropy: 128 bits entropy.
- mnemonic: 12 mnemonics.
- seed: 512 bits seed.
- xprv: 512 bits expaneded private key.
- xpub: 512 bits expaneded public key.
- xprv_base64: xprv hex string qrcode base64.

```python
>>> from pybtmsdk import key
>>> r = key.get_new_key()
>>> r['entropy']
'8466b1128f92051361c9aa2de52d1bb0'
>>> r['mnemonic']
'love culture dwarf busy cake meadow mango crystal combine city eight genuine'
>>> r['seed']
'4d15bf0f72bad754987fdcd0628ea37af03ac24666019c6d362e0200c9b49bee35aa0a788ed09e3a86cd529df0a1c20ea6aa719cf1e0da4ffb15efbc38fba498'
>>> r['xprv']
'f09ad64c2714b45e23c75e4541ad771def99b97e6da16b0cc6bcdac045f4d34745b62093173fd8f9a67e1da4b81233bc947880b6ed4b9641cf8f5223212fa18d'
>>> r['xpub']
'ebcc4b14444adb207dd53fd89b2881b21e839de42a1b6687a5a9d83b82c1b5b645b62093173fd8f9a67e1da4b81233bc947880b6ed4b9641cf8f5223212fa18d'
>>> r['xprv_base64']
{'base64': '/9j/4AAQSkZJRgABAQAAAQABAAD...'}
```

```python
>>> from pybtmsdk import key
>>> r = key.get_new_key(entropy_hexstr='4d33735a9e92f634d22aecbb4044038d')
>>> r['entropy']
'4d33735a9e92f634d22aecbb4044038d'
>>> r['mnemonic']
'essay oppose stove diamond control bounce emerge frown robust acquire abstract brick'
```

```python
>>> from pybtmsdk import key
>>> r = key.get_new_key(mnemonic_str='ancient young hurt bone shuffle deposit congress normal crack six boost despair')
>>> r['entropy']
''
>>> r['mnemonic']
'ancient young hurt bone shuffle deposit congress normal crack six boost despair'
>>> r['seed']
'afa3a86bbec2f40bb32833fc6324593824c4fc7821ed32eac1f762b5893e56745f66a6c6f2588b3d627680aa4e0e50efd25065097b3daa8c6a19d606838fe7d4'
```

### 2.13 Create HD path

get_path_from_index create HD path.

Parameter:

- account_index_int: 1, 2, 3, ..., type is hex string.
- address_index_int: 1, 2, 3, ..., type is hex string.
- change_bool: If receiver is change, change_bool is True, otherwise the change_bool is False.

Return:

- path_list: path list.
- path_str: path string.

```python
>>> from pybtmsdk import receiver
>>> account_index_int = 1
>>> address_index_int = 1
>>> change_bool = True
>>> receiver.get_path_from_index(account_index_int, address_index_int, change_bool)
{'path': ['2c000000', '99000000', '01000000', '01000000', '01000000'], 'path_str': 'm/44/153/1/1/1'}
```

### 2.14 Create control program

get_control_program create control program.

Parameter:

- account_index_int: account index, e.g. 1, 2, 3...
- address_index_int: address index, e.g. 1, 2, 3...
- change_bool: If receiver is change, change_bool is True, otherwise the change_bool is False.
- xpub_hexstr: 512 bits expanded public key, type is hex string.

Return:

- control_program_hexstr: type is hex string.

```python
>>> from pybtmsdk import receiver
>>> account_index_int = 1
>>> address_index_int = 1
>>> change_bool = False
>>> xpub_hexstr = '3c6664244d2d57168d173c4691dbf8741a67d972b2d3e1b0067eb825e2005d20c5eebd1c26ccad4de5142d7c339bf62cc1fb79a8b3e42a708cd521368dbc9286'
>>> receiver.get_control_program(account_index_int, address_index_int, change_bool, xpub_hexstr)
'0014052620b86a6d5e07311d5019dffa3864ccc8a6bd'
```

### 2.15 Create address

get_address create address from control program.

Parameter:

- control_program_hexstr: control program.
- network_str: 3 types of network is available: mainnet, testnet and solonet.

Return:

- address: bytom address.

```python
>>> from pybtmsdk import receiver
>>> control_program_hexstr = '001431f2b90b469e89361225aae370f73e5473b9852b'
>>> network_str = 'mainnet'
>>> receiver.get_address(control_program_hexstr, network_str)
'bm1qx8etjz6xn6ynvy394t3hpae723emnpft3nrwej'
```

### 2.16 Create new address

get_new_address create new address.

Parameter:

- xpub_hexstr: 512 bits expanded public key, type is hex string.
- account_index_int: account index, e.g. 1, 2, 3...
- address_index_int: address index, e.g. 1, 2, 3...
- change_bool: If receiver is change, change_bool is True, otherwise the change_bool is False.
- network_str: 3 types of network is available: mainnet, testnet and solonet.

Return:

- path: BIP44 HD path.
- control program: control program.
- address: bytom address.
- address_base64: bytom address image base64.

```python
>>> from pybtmsdk import receiver
>>> xpub_hexstr = '8fde12d7c9d6b6cbfbf344edd42f2ed86ae6270b36bab714af5fd5bb3b54adcec4265f1de85ece50f17534e42016ee9404a11fec94ddfadd4a064d27ef3f3f4c'
>>> account_index_int = 1
>>> address_index_int = 1
>>> change_bool = False
>>> network_str = 'solonet'
>>> receiver.get_new_address(xpub_hexstr, account_index_int, address_index_int, change_bool, network_str)
{'path': 'm/44/153/1/0/1', 'control_program': '00147640f3c34fe4b2b298e54e54a4692a47ce47aa5e', 'address': 'sm1qweq08s60ujet9x89fe22g6f2gl8y02j7lgr5v5', 'address_base64': '/9j/4AAQSkZJRgAB...'}
```

### 2.17 Submit raw transaction

submit_transaction submit transaction.

Parameter:

- raw_transaction_hexstr: raw transaction.
- submit_url: you can send raw transaction through submit_url.

Return:

- result: If submit transaction successfully, result is 1.

```python
>>> from pybtmsdk import transaction
>>> raw_transaction_hexstr = '070100010160015e5dfc352f9247985e92b2688a9a0a0e3e45a52f633c7d2c35cf6485fc1f03a89cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8094ebdc030101160014052620b86a6d5e07311d5019dffa3864ccc8a6bd630240988348a301c86563eb16105cc0c7e12e8cd1fbc7e9031933dac05a32d2a696bc77b83f25a99a4a9458d976c5327b8004918545a3fde567f28d805f741db54e0b20e87ca3acdebdcad9a1d0f2caecf8ce0dbfc73d060807a210c6f225488347961402013dffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff80b6f7f302011600147950bb5fcfb1c3fe14198c14ebd4ad85bb69bbc500013cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8084af5f011600141d8e1c2d71843f41e2131d7fd6df8b47e2cf56b900'
>>> submit_url = 'https://blockmeta.com/api/wisdom/broadcast-transaction'
>>> transaction.submit_transaction(raw_transaction_hexstr, submit_url)
'1'
```

```python
>>> from pybtmsdk import transaction
>>> raw_transaction_hexstr = '07010001015f015d2f4a8f10afbc0448779fadd916a3f1b8518ffe0b7d20fdf470d8e9b4993ef2b4ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc0d8883200011600144a594e3e4cbbd87629476e7ee24c1637df66c0b76302406fd39079681118840fd6fd66cdff769f2d05d8520312e9dd559dc23c36a3cb3921e47cba233d5d2267eb0f128a908d1bab877e172e880d3f36dc6a5e5826540c202854e5c181f5a862edd190e413d75937549758ef4902e1475aac52623f0a239302013cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc09dd81001160014f63f68597df5c88a92e04229e0fd08a3584ade3b00013cffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff80e1eb1701160014664f28ec6ab8826a028658dc0d0d1f94c6e20fa300'
>>> submit_url = 'https://blockmeta.com/api/v2/broadcast-transaction'
>>> transaction.submit_transaction(raw_transaction_hexstr, submit_url)
'1'
```

### 2.18 Decode raw transaction

decode_raw_tx decode raw transaction.

Parameter:

- raw_transaction_hexstr: raw transaction, type is hex string.
- network_str: 3 types of network is available: mainnet, testnet and solonet.

Return:

- tx: tx dict.

```python
>>> from pybtmsdk import transaction
>>> raw_transaction_hexstr = '070100010161015f28b7b53d8dc90006bf97e0a4eaae2a72ec3d869873188698b694beaf20789f21ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8099c4d5990100011600149335b1cbd4a77b78e33315a0ed10a95b12e7ca48630240897e2d9d24a3b5faaed0579dee7597b401491595675f897504f8945b29d836235bd2fca72a3ad0cae814628973ebcd142d9d6cc92d0b2571b69e5370a98a340c208cb7fb3086f58db9a31401b99e8c658be66134fb9034de1d5c462679270b090702013effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff80f9f8bc98010116001406ce4b689ba026ffd3a7ca65d1d059546d4b78a000013dffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff80c6868f01011600147929ef91997c827bebf60fa608f876ea27523c4700'
>>> network_str = 'solonet'
>>> transaction.decode_raw_tx(raw_transaction_hexstr, network_str)
{'fee': 20000000, 'inputs': [{'address': 'sm1qjv6mrj755aah3cenzksw6y9ftvfw0jjgk0l2mw', 'amount': 41250000000, 'asset_definition': {}, 'asset_id': 'ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff', 'control_program': '00149335b1cbd4a77b78e33315a0ed10a95b12e7ca48', 'input_id': '6e3f378ed844b143a335e306f4ba26746157589c87e8fc8cba6463c566c56768', 'spent_output_id': 'f229ec6f403d586dc87aa2546bbe64c5f7b5f46eb13c6ee4823d03bc88a7cf17', 'type': 'spend', 'witness_arguments': ['897e2d9d24a3b5faaed0579dee7597b401491595675f897504f8945b29d836235bd2fca72a3ad0cae814628973ebcd142d9d6cc92d0b2571b69e5370a98a340c', '8cb7fb3086f58db9a31401b99e8c658be66134fb9034de1d5c462679270b0907']}], 'outputs': [{'address': 'sm1qqm8yk6ym5qn0l5a8efjar5ze23k5k79qnvtslj', 'amount': 40930000000, 'asset_definition': {}, 'asset_id': 'ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff', 'control_program': '001406ce4b689ba026ffd3a7ca65d1d059546d4b78a0', 'id': '74c73266730d3c6ea32e8667ef9b867068736b84be240fe9fef205fa68bb7b95', 'position': 0, 'type': 'control'}, {'address': 'sm1q0y57lyve0jp8h6lkp7nq37rkagn4y0z8hvh6kq', 'amount': 300000000, 'asset_definition': {}, 'asset_id': 'ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff', 'control_program': '00147929ef91997c827bebf60fa608f876ea27523c47', 'id': 'f115a833d0c302a5006032858a7ed3987f0feb2daf2a9f849384950e4766af51', 'position': 1, 'type': 'control'}], 'size': 333, 'time_range': 0, 'tx_id': '814a73dd57bae67c604f9cbc696cbc42035577423408cb9267136ed971e2bf63', 'version': 1}
```

## 3 Api

### 3.1 Use api client

#### Create Bytom Client
Create bytom client with local node, default url is http://localhost:9888:
```python
from pybtmsdk import BytomAPI

api = BytomAPI()
```

or

 Create bytom client with remote node:
```python
from pybtmsdk import BytomAPI

url = 'http://YOUR_HOST:9888'
access_token = 'YOUR_ACCESS_TOKEN'
api = BytomAPI(url, access_token)
```

#### API response
use python object as return:
```python
ret = api.wallet_info()
print(ret.best_block_height) # 76251
print(ret.wallet_height)     # 76251
```
or

use Dict object as return:
```python
ret = api.get_block_count(return_dict=True)
print(ret)                   # {u'block_count': 76409}
print(ret["block_count"])    # 76409
```
or

use original API response (JSON) as return:
```python
ret = api.get_block_count(return_json=True)
print(ret)                   # '{"block_count": 80267}'
```
