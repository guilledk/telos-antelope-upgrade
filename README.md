# Telos Mandel Upgrade

### CI tests to perform telos+mandel upgrade

Contracts used:

            contract - branch - cdt

    old: `github.com/telosnetwork/telos.contracts`
 
        - eosio.msig   - v1.5.2 - v1.4.1
        - eosio.system - master - v1.6.3
        - eosio.token  - master - v1.6.3
        - eosio.wrap   - v1.5.2 - v1.4.1

    new: `github.com/guilledk/telos.contracts`
 
        - eosio.msig   - mandel_merge - v1.7.0
        - eosio.system - mandel_merge - v1.7.0
        - eosio.token  - mandel_merge - v1.7.0
        - eosio.wrap   - mandel_merge - v1.7.0

Check the `tests/` directory.
