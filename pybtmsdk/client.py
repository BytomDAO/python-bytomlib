#!/usr/bin/env python
# coding=utf-8

from pybtmsdk.bind import bind_method

NO_ACCEPT_PARAMETERS = []


class BytomAPI(object):
    default_url = "http://localhost:9888"
    api_name = "Bytom"
    version = "1.0.3"

    def __init__(self, url=default_url):
        self.url = url
        self.auth = ()

    # Available with wallet enable
    # yes has
    create_key = bind_method(
                path="/create-key",
                accepts_parameters=["alias", "password", "language", "mnemonic"])

    # new add
    update_key_alias = bind_method(
                path="/update-key-alias",
                accepts_parameters=["xpub", "new_alias"])

    # yes has
    list_keys = bind_method(
                path="/list-keys",
                accepts_parameters=NO_ACCEPT_PARAMETERS)

    # yes has
    delete_key = bind_method(
                path="/delete-key",
                accepts_parameters=["xpub", "password"])

    # yes has
    check_key_password = bind_method(
                path="/check-key-password",
                accepts_parameters=["xpub", "password"])

    # yes has
    reset_key_password = bind_method(
                path="/reset-key-password",
                accepts_parameters=["xpub", "old_password", "new_password"])

    # yes has
    create_account = bind_method(
                path="/create-account",
                accepts_parameters=["root_xpubs", "alias", "quorum"])

    # new add
    update_account_alias = bind_method(
                path="/update-account-alias",
                accepts_parameters=["account_id", "account_alias", "new_alias"])

    # yes has
    list_accounts = bind_method(
                path="/list-accounts",
                accepts_parameters=["id", "alias"])

    # yes has
    delete_account = bind_method(
                path="/delete-account",
                accepts_parameters=["account_id", "account_alias"])

    # yes has
    create_account_receiver = bind_method(
                path="/create-account-receiver",
                accepts_parameters=["account_alias", "account_id"])

    # yes has
    list_addresses = bind_method(
                path="/list-addresses",
                accepts_parameters=["account_id", "account_alias", "from", "count"])

    # yes has
    validate_address = bind_method(
                path="/validate-address",
                accepts_parameters=["address"])

    # yes has
    list_pubkeys = bind_method(
                path="/list-pubkeys",
                accepts_parameters=["account_alias", "account_id", "public_key"])

    # new add
    get_mining_address = bind_method(
                path="/get-mining-address",
                accepts_parameters=NO_ACCEPT_PARAMETERS)

    # new add
    set_mining_address = bind_method(
                path="/set-mining-address",
                accepts_parameters=["mining_address"])

    # yes has
    create_asset = bind_method(
                path="/create-asset",
                accepts_parameters=["alias", "root_xpubs", "quorum", "definition", "limit_height", "issuance_program"])

    # yes has
    get_asset = bind_method(
                path="/get-asset",
                accepts_parameters=["id"])

    # yes has
    # maybe has error ! should check it!
    list_assets = bind_method(
                path="/list-assets",
                accepts_parameters=NO_ACCEPT_PARAMETERS)

    # yes has
    update_asset_alias = bind_method(
                path="/update-asset-alias",
                accepts_parameters=["id", "alias"])

    # yes has
    list_balances = bind_method(
                path="/list-balances",
                accepts_parameters=["account_id", "account_alias"])

    # yes has
    list_unspent_outputs = bind_method(
                path="/list-unspent-outputs",
                accepts_parameters=["id", "unconfirmed", "smart_contract", "from",
                                    "count", "account_id", "account_alias"])

    # new add
    list_account_votes = bind_method(
                path="/list-account-votes",
                accepts_parameters=["account_id", "account_alias"])

    # yes has
    backup_wallet = bind_method(
                path="/backup-wallet",
                accepts_parameters=NO_ACCEPT_PARAMETERS)

    # yes has
    restore_wallet = bind_method(
                path="/restore-wallet",
                accepts_parameters=["account_image", "asset_image", "key_images"])

    # yes has
    rescan_wallet = bind_method(
                path="/rescan-wallet",
                accepts_parameters=NO_ACCEPT_PARAMETERS)

    # yes has
    wallet_info = bind_method(
                path="/wallet-info",
                accepts_parameters=NO_ACCEPT_PARAMETERS)

    # new add
    recovery_wallet = bind_method(
                path="/recovery-wallet",
                accepts_parameters=["xpubs"])

    # yes has
    sign_message = bind_method(
                path="/sign-message",
                accepts_parameters=["address", "message", "password"])

    # yes has
    decode_program = bind_method(
                path="/decode-program",
                accepts_parameters=["program"])

    # yes has
    get_transaction = bind_method(
                path="/get-transaction",
                accepts_parameters=["tx_id"])

    # yes has
    list_transactions = bind_method(
                path="/list-transactions",
                accepts_parameters=["id", "account_id", "detail", "unconfirmed", "from", "count"])

    # yes has
    build_transaction = bind_method(
                path="/build-transaction",
                accepts_parameters=["base_transaction", "ttl", "time_range", "actions"])

    # yes has
    build_chain_transactions = bind_method(
                path="/build-chain-transactions",
                accepts_parameters=["base_transaction", "ttl", "time_range", "actions"])

    # yes has
    sign_transaction = bind_method(
                path="/sign-transaction",
                accepts_parameters=["password", "transaction"])

    # yes has
    sign_transactions = bind_method(
                path="/sign-transactions",
                accepts_parameters=["password", "transactions"])

    # Available whether or not the wallet is open
    # yes has
    submit_transaction = bind_method(
                path="/submit-transaction",
                accepts_parameters=["raw_transaction"])

    # yes has
    submit_transactions = bind_method(
                path="/submit-transactions",
                accepts_parameters=["raw_transactions"])

    # yes has
    estimate_transaction_gas = bind_method(
                path="/estimate-transaction-gas",
                accepts_parameters=["transaction_template"])

    # new add
    estimate_chain_transaction_gas = bind_method(
                path="/estimate-chain-transaction-gas",
                accepts_parameters=["transaction_templates"])

    # yes has
    create_access_token = bind_method(
                path="/create-access-token",
                accepts_parameters=["id", "type"])

    # yes has
    list_access_tokens = bind_method(
                path="/list-access-tokens",
                accepts_parameters=NO_ACCEPT_PARAMETERS)

    # yes has
    delete_access_token = bind_method(
                path="/delete-access-token",
                accepts_parameters=["id"])

    # yes has
    check_access_token = bind_method(
                path="/check-access-token",
                accepts_parameters=["id", "secret"])

    # new add
    create_contract = bind_method(
                path="/create-contract",
                accepts_parameters=["alias", "contract"])

    # new add
    update_contract_alias = bind_method(
                path="/update-contract-alias",
                accepts_parameters=["id", "alias"])

    # new add
    get_contract = bind_method(
                path="/get-contract",
                accepts_parameters=["id"])

    # yes has
    create_transaction_feed = bind_method(
                path="/create-transaction-feed",
                accepts_parameters=["alias", "filter"])

    # yes has
    get_transaction_feed = bind_method(
                path="/get-transaction-feed",
                accepts_parameters=["alias"])

    # yes has
    list_transaction_feeds = bind_method(
                path="/list-transaction-feeds",
                accepts_parameters=NO_ACCEPT_PARAMETERS)

    # yes has
    delete_transaction_feed = bind_method(
                path="/delete-transaction-feed",
                accepts_parameters=["alias"])

    # yes has
    update_transaction_feed = bind_method(
                path="/update-transaction-feed",
                accepts_parameters=["alias", "filter"])

    # yes has
    get_unconfirmed_transaction = bind_method(
                path="/get-unconfirmed-transaction",
                accepts_parameters=["tx_id"])

    # yes has
    list_unconfirmed_transactions = bind_method(
                path="/list-unconfirmed-transactions",
                accepts_parameters=NO_ACCEPT_PARAMETERS)

    # yes has
    decode_raw_transaction = bind_method(
                path="/decode-raw-transaction",
                accepts_parameters=["raw_transaction"])

    # yes has
    get_block_count = bind_method(
                path="/get-block-count",
                accepts_parameters=NO_ACCEPT_PARAMETERS)

    # yes has
    get_block_hash = bind_method(
                path="/get-block-hash",
                accepts_parameters=NO_ACCEPT_PARAMETERS)

    # yes has
    get_block = bind_method(
                path="/get-block",
                accepts_parameters=["block_height", "block_hash"])

    # new add
    get_raw_block = bind_method(
                path="/get-raw-block",
                accepts_parameters=["block_height", "block_hash"])

    # yes has
    get_block_header = bind_method(
                path="/get-block-header",
                accepts_parameters=["block_height", "block_hash"])

    # new add
    is_mining = bind_method(
                path="/is-mining",
                accepts_parameters=NO_ACCEPT_PARAMETERS)

    # new add
    set_mining = bind_method(
                path="/set-mining",
                accepts_parameters=["is_mining"])

    # yes has
    net_info = bind_method(
                path="/net-info",
                accepts_parameters=NO_ACCEPT_PARAMETERS)

    # yes has
    gas_rate = bind_method(
                path="/gas-rate",
                accepts_parameters=NO_ACCEPT_PARAMETERS)

    # yes has
    verify_message = bind_method(
                path="/verify-message",
                accepts_parameters=["address", "derived_xpub", "message", "signature"])

    # yes has
    compile = bind_method(
                path="/compile",
                accepts_parameters=["contract", "args"])

    # yes has
    list_peers = bind_method(
                path="/list-peers",
                accepts_parameters=NO_ACCEPT_PARAMETERS)

    # yes has
    disconnect_peer = bind_method(
                path="/disconnect-peer",
                accepts_parameters=["peer_id"])

    # yes has
    connect_peer = bind_method(
                path="/connect-peer",
                accepts_parameters=["ip", "port"])

    # new add
    get_merkle_proof = bind_method(
                path="/get-merkle-proof",
                accepts_parameters=["tx_ids", "block_hash"])

    # new add
    get_vote_result = bind_method(
                path="/get-vote-result",
                accepts_parameters=["block_hash", "block_height"])

