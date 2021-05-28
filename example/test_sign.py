# coding:utf-8


from pybtmsdk import BytomAPI
from pybtmsdk.transaction import decode_raw_tx
from pybtmsdk.signature import generate_signatures_use_mnemonic
from pybtmsdk.receiver import get_new_address
from pybtmsdk.key import get_child_xprv, get_xpub, get_seed, get_root_xprv, xprv_sign


mnemonic_str = "famous atom coral belt grab together patrol steak forum undo someone motor"
sign_data = "f58eb312702c47f489fcaa6093c5af1e9edea62c605705d405848b1adf8f2756"

derivation_path = [
"2c000000",
"99000000",
"01000000",
"01000000",
"02000000"
]

private_key = get_root_xprv(get_seed(mnemonic_str))
expanded_prv = get_child_xprv(private_key, derivation_path)
expandex_pub_key = get_xpub(expanded_prv)

print(expandex_pub_key[:64])

sign_message = xprv_sign(expanded_prv, sign_data)
print(sign_message)
