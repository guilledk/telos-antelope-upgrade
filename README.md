# Telos Antelope Upgrade

### CI tests to perform telos+antelope upgrade

Contracts used:

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

Check the `tests/` directory.
