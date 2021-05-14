#!/usr/bin/env python
# coding=utf-8

from .bind import bind_method

NO_ACCEPT_PARAMETERS = []

class BytomAPI(object):
    default_url = "http://localhost:9888"
    api_name = "Bytom"
    version = "1.0.3"

    def __init__(self, url=default_url, access_token=""):
        self.url = url
        self.access_token = access_token
        self.auth = ()
        if self.access_token != "":
            self.auth = tuple(self.access_token.split(":"))

    # Available with wallet enable
    # has
    create_key = bind_method(
                path="/create-key",
                accepts_parameters=["alias", "password", "language", "mnemonic"])

    # has
    list_keys = bind_method(
                path="/list-keys",
                accepts_parameters=NO_ACCEPT_PARAMETERS)

    # has
    delete_key = bind_method(
                path="/delete-key",
                accepts_parameters=["xpub", "password"])

    # check-key-password
    check_key_password = bind_method(
                path="/check-key-password",
                accepts_parameters=["xpub", "password"])

    # has
    reset_key_password = bind_method(
                path="/reset-key-password",
                accepts_parameters=["xpub", "old_password", "new_password"])

    # has
    create_account = bind_method(
                path="/create-account",
                accepts_parameters=["root_xpubs", "alias", "quorum"])

    # has
    list_accounts = bind_method(
                path="/list-accounts",
                accepts_parameters=["id", "alias"])

    # has
    delete_account = bind_method(
                path="/delete-account",
                accepts_parameters=["account_id", "account_alias"])

    # has
    create_account_receiver = bind_method(
                path="/create-account-receiver",
                accepts_parameters=["account_alias", "account_id"])

    # has
    list_addresses = bind_method(
                path="/list-addresses",
                accepts_parameters=["account_id", "account_alias", "from", "count"])

    # has
    validate_address = bind_method(
                path="/validate-address",
                accepts_parameters=["address"])

    # has
    list_pubkeys = bind_method(
                path="/list-pubkeys",
                accepts_parameters=["account_alias", "account_id", "public_key"])

    # has
    create_asset = bind_method(
                path="/create-asset",
                accepts_parameters=["alias", "root_xpubs", "quorum", "definition", "limit_height", "issuance_program"])

    # has
    get_asset = bind_method(
                path="/get-asset",
                accepts_parameters=["id"])

    # has
    list_assets = bind_method(
                path="/list-assets",
                accepts_parameters=NO_ACCEPT_PARAMETERS)

    # has
    update_asset_alias = bind_method(
                path="/update-asset-alias",
                accepts_parameters=["id", "alias"])

    # has
    list_balances = bind_method(
                path="/list-balances",
                accepts_parameters=["account_id", "account_alias"])

    # has
    list_unspent_outputs = bind_method(
                path="/list-unspent-outputs",
                accepts_parameters=["id", "unconfirmed", "smart_contract", "from", "count", "account_id", "account_alias"])

    # has
    backup_wallet = bind_method(
                path="/backup-wallet",
                accepts_parameters=NO_ACCEPT_PARAMETERS)

    # has
    restore_wallet = bind_method(
                path="/restore-wallet",
                accepts_parameters=["account_image", "asset_image", "key_images"])

    # has
    rescan_wallet = bind_method(
                path="/rescan-wallet",
                accepts_parameters=NO_ACCEPT_PARAMETERS)

    # has
    wallet_info = bind_method(
                path="/wallet-info",
                accepts_parameters=NO_ACCEPT_PARAMETERS)

    # has
    sign_message = bind_method(
                path="/sign-message",
                accepts_parameters=["address", "message", "password"])

    # has
    decode_program = bind_method(
                path="/decode-program",
                accepts_parameters=["program"])

    get_transaction = bind_method(
                path="/get-transaction",
                accepts_parameters=["tx_id"])

    # has
    list_transactions = bind_method(
                path="/list-transactions",
                accepts_parameters=["id", "account_id", "detail", "unconfirmed", "from", "count"])

    # has
    build_transaction = bind_method(
                path="/build-transaction",
                accepts_parameters=["base_transaction", "ttl", "time_range", "actions"])

    # has
    build_chain_transactions = bind_method(
                path="/build-chain-transactions",
                accepts_parameters=["base_transaction", "ttl", "time_range", "actions"])

    # has
    sign_transaction = bind_method(
                path="/sign-transaction",
                accepts_parameters=["password", "transaction"])

    # Available whether or not the wallet is open
    # has
    submit_transaction = bind_method(
                path="/submit-transaction",
                accepts_parameters=["raw_transaction"])

    # has
    submit_transactions = bind_method(
                path="/submit-transactions",
                accepts_parameters=["raw_transactions"])

    # has
    estimate_transaction_gas = bind_method(
                path="/estimate-transaction-gas",
                accepts_parameters=["transaction_template"])

    # has
    create_access_token = bind_method(
                path="/create-access-token",
                accepts_parameters=["id", "type"])

    # has
    list_access_tokens = bind_method(
                path="/list-access-tokens",
                accepts_parameters=NO_ACCEPT_PARAMETERS)

    # has
    delete_access_token = bind_method(
                path="/delete-access-token",
                accepts_parameters=["id"])

    # has
    check_access_token = bind_method(
                path="/check-access-token",
                accepts_parameters=["id", "secret"])

    # has
    create_transaction_feed = bind_method(
                path="/create-transaction-feed",
                accepts_parameters=["alias", "filter"])

    # has
    get_transaction_feed = bind_method(
                path="/get-transaction-feed",
                accepts_parameters=["alias"])

    # has
    list_transaction_feeds = bind_method(
                path="/list-transaction-feeds",
                accepts_parameters=NO_ACCEPT_PARAMETERS)

    # has
    delete_transaction_feed = bind_method(
                path="/delete-transaction-feed",
                accepts_parameters=["alias"])

    # has
    update_transaction_feed = bind_method(
                path="/update-transaction-feed",
                accepts_parameters=["alias", "filter"])

    # has
    get_unconfirmed_transaction = bind_method(
                path="/get-unconfirmed-transaction",
                accepts_parameters=["tx_id"])

    # has
    list_unconfirmed_transactions = bind_method(
                path="/list-unconfirmed-transactions",
                accepts_parameters=NO_ACCEPT_PARAMETERS)

    # has
    decode_raw_transaction = bind_method(
                path="/decode-raw-transaction",
                accepts_parameters=["raw_transaction"])

    # has
    get_block_count = bind_method(
                path="/get-block-count",
                accepts_parameters=NO_ACCEPT_PARAMETERS)

    # has
    get_block_hash = bind_method(
                path="/get-block-hash",
                accepts_parameters=NO_ACCEPT_PARAMETERS)

    # has
    get_block = bind_method(
                path="/get-block",
                accepts_parameters=["block_height", "block_hash"])

    # has
    get_block_header = bind_method(
                path="/get-block-header",
                accepts_parameters=["block_height", "block_hash"])

    # has
    net_info = bind_method(
                path="/net-info",
                accepts_parameters=NO_ACCEPT_PARAMETERS)


    # has
    gas_rate = bind_method(
                path="/gas-rate",
                accepts_parameters=NO_ACCEPT_PARAMETERS)

    # has
    verify_message = bind_method(
                path="/verify-message",
                accepts_parameters=["address", "derived_xpub", "message", "signature"])

    # has
    compile = bind_method(
                path="/compile",
                accepts_parameters=["contract", "args"])

    # has
    list_peers = bind_method(
                path="/list-peers",
                accepts_parameters=NO_ACCEPT_PARAMETERS)

    # has
    disconnect_peer = bind_method(
                path="/disconnect-peer",
                accepts_parameters=["peer_id"])

    # has
    connect_peer = bind_method(
                path="/connect-peer",
                accepts_parameters=["ip", "port"])

