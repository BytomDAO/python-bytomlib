#from pybtmsdk import ed25519
#import pybtmsdk.edwards25519 as ed25519
import copy

from binascii import hexlify
from binascii import unhexlify

from pybtmsdk.key import get_child_xprv, get_xpub, get_seed, get_root_xprv, xprv_sign
from pybtmsdk import utils


def find_dist(private_keys, xpub):
    dst = -1
    for i, key in enumerate(private_keys):
        temp_xpub = get_xpub(key)
        if xpub == temp_xpub:
            dst = i
            print("private[dst]: ", private_keys[dst])
            break

    if dst == -1:
        raise Exception("Not a proper private key to sign transaction.")
    
    return dst


def generate_signatures(private_keys, input_template, input_decoded_tx):
    if type(input_template) != dict:
        template = simplejson.loads(simplejson.dumps(input_template))
    else:
        template = copy.deepcopy(input_template)

    if type(input_decoded_tx) != dict:
        decoded_tx = simplejson.loads(simplejson.dumps(input_decoded_tx))
    else:
        decoded_tx = copy.deepcopy(input_decoded_tx)
        
    result = copy.deepcopy(template)

    for i, signing in enumerate(template["signing_instructions"]):
        for wc in signing["witness_components"]:
            # Have two cases
            if wc["type"] == "raw_tx_signature":
                if wc["signatures"] is None or len(wc["signatures"]) < len(wc["keys"]):
                    wc["signatures"] = ["" for i in range(0, len(wc["keys"]))]

                wc["pubkeys"] = ["" for i in range(len(wc["keys"]))]

                message = decoded_tx["inputs"][signing["position"]]["sign_data"]

                for j, key in enumerate(wc["keys"]):
                    if wc["signatures"][j] is None or wc["signatures"][j] == "":
                        public_key = key["xpub"]
                        dst = find_dist(private_keys, public_key)
                        private_key = private_keys[dst]
                        expanded_prv = get_child_xprv(private_key, key["derivation_path"])

                        print("private_key: %s" % private_key)
                        print("child_xprv: %s" % expanded_prv)

                        print("message: %s" % message)

                        sig = xprv_sign(expanded_prv, message)
                        
                        print("sig: %s" % sig)
                        wc["signatures"][j] = sig
                        wc["pubkeys"][j] = get_xpub(expanded_prv)
                        result["signing_instructions"][i]["witness_components"][j]["signatures"] = wc["signatures"]
                break
            elif wc.type == "":
                break
            else:
                continue

    return {
        "transaction": result,
        "sign_complete": True
    }


def generate_signatures_use_mnemonic(mnemonics_keys, input_template, input_decoded_tx):
    private_keys = []
    for mnemonic_str in mnemonics_keys:
        seed = get_seed(mnemonic_str)
        secret_key = get_root_xprv(seed)
        private_keys.append(secret_key)
    return generate_signatures(private_keys, input_template, input_decoded_tx)





