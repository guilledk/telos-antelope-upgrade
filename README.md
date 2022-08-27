# Telos Antelope Upgrade

### CI tests to perform telos+antelope upgrade

    - Deploy old contracts to a local chain running leap-3.1.0
    - Run a bunch of msig, token and wrap exec tests
    - Upgrade system contracts to new version
    - Re-run tests and check we get same resutlts

### Contracts used:

            contract - branch - cdt

    old: `github.com/telosnetwork/telos.contracts`

        - eosio.msig   - v1.5.2 - v1.4.1
        - eosio.system - master - v1.6.3
        - eosio.token  - master - v1.6.3
        - eosio.wrap   - v1.5.2 - v1.4.1

    new: `github.com/guilledk/telos-system-contracts`

        - eosio.msig   - telos-specific - v3.0.0-rc2
        - eosio.system - telos-specific - v3.0.0-rc2
        - eosio.token  - telos-specific - v3.0.0-rc2
        - eosio.wrap   - telos-specific - v3.0.0-rc2

Checkout the `tests/` directory.
