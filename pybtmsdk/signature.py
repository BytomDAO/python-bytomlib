import ed25519
import copy

from pybtmsdk.key import get_child_xprv, get_xpub, get_seed, get_root_xprv
# You can verify or get more test data from: https://gist.github.com/zcc0721/bfa5c34a49ddfcaf9fdc3374cecb1477
# test data 1:
#   private_key_str: 33c6e964cf64246fc37f26be46c7b783ef4364f9d4c69daa4ccd9d0fef5fcef1
#   public_key_str: b25690a0ccd290a3346fb412dfd342c5ce6134ef116e89b0642d7534e34df432
#   message_str: 68656c6c6f206279746f6d      # value is: 'hello bytom'
#   signature_str: dfb19c1892796ad9560eb61a065c016c82a7a81a42f2c3f69d20f44582262551b62fee6836c866e008c2cb37bba7e2045013f073ad7f69f5dd2a634929c3d406
# test data 2:
#   private_key_str: 0164f0d6bc1f063fc74f1010dc4c5393af40d215cc905884443ed0cfe2e2c1c4
#   public_key_str: 5faaee522735460654190609cab55f96edd44ea78e358d6a02ef769b0c9eb314
#   message_str: b435f948bd3748ede8f9d6f59728d669939e79c6c885667a5c138e05bbabde1de0dcfcbe0c6112022fbbf0da522f4e224a9c2381016380688b51886248b3156f
#   signature_str: 18d29864775ff4ec0c78a477f57c5d4dd03526d55ba33bd6768acf3ca0cf7e41fe9c241a7bc550f4fa14a745fbe0155cb896f9e4d88c87337e6dc3a313c8d80b
# test data 3:
#   private_key_str: 7eb40ebe8beee07dfbc645300f571948a9ce83191c28505e710b6900ec2531ed
#   public_key_str: 026b5e22e282d07051203fb0596be140cf17f2532a31407f3b177faa74237cbe
#   message_str: 48ec69c784c519b65d0e52badda3b7c25113a6b53b4c8e582abee3e2f9aab41514f15bd44c999f3d2ddae4bbab15baf9f4d82dde4f97aa5042cbcfdd8271530e
#   signature_str: 691fe6fc51603adbac0db2f71f383e7039b6a031a2242da8fd6203f9c71e3b526d0cdace626811ee06797de21afebe54d0293027eb6b22b10c63d4dd0ab8790c
def sign(private_key_str, message_str):
    signing_key = ed25519.SigningKey(bytes.fromhex(private_key_str))
    # signature = signing_key.sign(message_str.encode(), encoding='hex')
    signature = signing_key.sign(bytes.fromhex(message_str), encoding='hex')
    return {
        "signature": signature.decode()
    }


def verify(public_key_str, signature_str, message_str):
    result = False
    verifying_key = ed25519.VerifyingKey(public_key_str.encode(), encoding='hex')
    try:
        verifying_key.verify(signature_str.encode(), bytes.fromhex(message_str), encoding='hex')
        result = True
    except ed25519.BadSignatureError:
        result = False
    return result


def find_dist(private_keys, xpub):
    dst = -1
    for i, key in enumerate(private_keys):
        temp_xpub = get_xpub(key)
        if xpub == temp_xpub:
            dst = i
            print("private[dst]: %s", private_keys[dst])
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

                        sig = sign(expanded_prv, message)["signature"] + "de"
                        
                        print("sig: %s" % sig)
                        wc["signatures"][j] = sig
                        result["signing_instructions"][i]["witness_components"][j]["signatures"] = wc["signatures"]
                break
            elif wc.type == "":
                break
            else:
                continue

    return result


def generate_signatures_use_mnemonic(mnemonics_keys, input_template, input_decoded_tx):
    private_keys = []
    for mnemonic_str in mnemonics_keys:
        seed = get_seed(mnemonic_str)
        secret_key = get_root_xprv(seed)
        private_keys.append(secret_key)
    return generate_signatures(private_keys, input_template, input_decoded_tx)

