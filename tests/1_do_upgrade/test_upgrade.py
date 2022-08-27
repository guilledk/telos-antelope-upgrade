#!/usr/bin/env python3


def test_upgrade(cleos):

    # perform protocol activations
    eos_mainnet = 'https://proton.greymass.com'
    telos_testnet = 'https://testnet.telos.net'

    feat_diff = cleos.diff_protocol_activations(
        eos_mainnet, telos_testnet)

    cleos.activate_feature('BLOCKCHAIN_PARAMETERS')
    # cleos.activate_feature('CONFIGURABLE_WASM_LIMITS')

    cleos.logger.info(f'feature diff: {feat_diff}')
    # for feat in feat_diff:
    #    cleos.activate_feature(feat)

    # deploy new contracts
    cleos.deploy_contract_from_host(
        'eosio.msig',
        'contracts/new/eosio.msig',
        create_account=False,
        verify_hash=False
    )
    cleos.deploy_contract_from_host(
        'eosio',
        'contracts/new/eosio.system',
        create_account=False,
        verify_hash=False
    )
    cleos.deploy_contract_from_host(
        'eosio.token',
        'contracts/new/eosio.token',
        create_account=False,
        verify_hash=False
    )
    cleos.deploy_contract_from_host(
        'eosio.wrap',
        'contracts/new/eosio.wrap',
        create_account=False,
        verify_hash=False
    )


