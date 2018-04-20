"""A simple GraphQL API for the Bitcoin Core Node software
For a full description of all available API"s see https://bitcoin.org/en/developer-reference
"""
import configparser

import graphene
from bitcoinrpc.authproxy import AuthServiceProxy

import backend.btcserver.types as types

CONFIG = configparser.ConfigParser()
CONFIG.read("config.ini")

def make_rpc_auth_url():
    """Constructs the RPC authentication URL from configuration

    Returns:
        str -- The URL containing the authentication info
    """

    config = CONFIG["DEFAULT"]
    http_type = "http"

    if config["btc_rpc_use_https"] == "false":
        http_type = "https"

    return "{}://{}:{}@{}:{}".format(
        http_type,
        config["btc_rpc_username"],
        config["btc_rpc_password"],
        config["btc_rpc_ip"],
        config["btc_rpc_port"])

RPC_CONNECTION = AuthServiceProxy(make_rpc_auth_url())

class Query(graphene.ObjectType):
    """Contains all Bitcoin RPC queries"""

    get_blockchain_info = graphene.Field(types.BlockchainInfoType)

    def resolve_get_blockchain_info(self, info, **kwargs):
        """bitcoin-cli getblockchaininfo
        https://bitcoin.org/en/developer-reference#getblockchaininfo
        """
        output = RPC_CONNECTION.getblockchaininfo()
        info = types.BlockchainInfoType()
        info.chain = output["chain"]
        info.blocks = output["blocks"]
        info.headers = output["headers"]
        info.best_block_hash = output["bestblockhash"]
        info.difficulty = output["difficulty"]
        info.median_time = output["mediantime"]
        info.verification_progress = output["verificationprogress"]
        info.initial_block_download = output["initialblockdownload"]
        info.chain_work = output["chainwork"]
        info.size_on_disk = output["size_on_disk"]
        info.pruned = output["pruned"]
        info.softforks = output["softforks"]
        info.bip9_softforks = output["bip9_softforks"]
        info.warnings = output["warnings"]
        return info

    get_mining_info = graphene.Field(types.MiningInfoType)

    def resolve_get_mining_info(self, info, **kwargs):
        """bitcoin-cli getmininginfo
        https://bitcoin.org/en/developer-reference#getmininginfo
        """
        output = RPC_CONNECTION.getmininginfo()
        info = types.MiningInfoType()
        info.blocks = output["blocks"]
        info.current_block_weight = output["currentblockweight"]
        info.current_block_tx = output["currentblocktx"]
        info.difficulty = output["difficulty"]
        info.network_hash_hps = output["networkhashps"]
        info.pooled_tx = output["pooledtx"]
        info.chain = output["chain"]
        info.warnings = output["warnings"]
        return info

    get_network_info = graphene.Field(types.NetworkInfoType)

    def resolve_get_network_info(self, info, **kwargs):
        """bitcoin-cli getnetworkinfo
        https://bitcoin.org/en/developer-reference#getnetworkinfo
        """
        output = RPC_CONNECTION.getnetworkinfo()
        info = types.NetworkInfoType()
        info.version = output["version"]
        info.subversion = output["subversion"]
        info.protocol_version = output["protocolversion"]
        info.local_services = output["localservices"]
        info.local_relay = output["localrelay"]
        info.time_offset = output["timeoffset"]
        info.network_active = output["networkactive"]
        info.connections = output["connections"]
        info.networks = output["networks"]
        info.relay_fee = output["relayfee"]
        info.incremental_fee = output["incrementalfee"]
        info.local_addresses = output["localaddresses"]
        info.warnings = output["warnings"]
        return info

    get_wallet_info = graphene.Field(types.WalletInfoType)

    def resolve_get_wallet_info(self, info, **kwargs):
        """bitcoin-cli getwalletinfo
        https://bitcoin.org/en/developer-reference#getwalletinfo
        """
        output = RPC_CONNECTION.getwalletinfo()
        info = types.WalletInfoType()
        info.wallet_name = output["walletname"]
        info.wallet_version = output["walletversion"]
        info.balance = output["balance"]
        info.unconfirmed_balance = output["unconfirmed_balance"]
        info.immature_balance = output["immature_balance"]
        info.tx_count = output["txcount"]
        info.keypool_oldest = output["keypoololdest"]
        info.keypool_size = output["keypoolsize"]
        info.keypool_size_hd_internal = output["keypoolsize_hd_internal"]
        info.pay_tx_fee = output["paytxfee"]
        info.hd_master_key_id = output["hdmasterkeyid"]
        return info
