from brownie import (
    network,
    config,
    accounts,
    MockV3Aggregator,
    Contract,
    VRFCoordinatorMock,
)

LOCAL_BLOCKCHAIN_ENVIROMENTS = ["development", "ganache-local", "mainnet-fork-dev"]
FORKED_LOCAL_ENVIROMENTS = ["mainnet-fork"]
DECIMALS = 8
STARTING_PRICE = 20000000000

contract_to_mock = {
    "eth_usd_price_feed": MockV3Aggregator,
    "vrf_coordinator": VRFCoordinatorMock,
}


def getAccount(id=None, index=None):
    if id:
        return accounts.load(id)
    if index:
        return accounts[index]
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIROMENTS
        or network.show_active() in FORKED_LOCAL_ENVIROMENTS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def get_contract(contract_name):
    """
    Toma el address de contrato desde brownie config, si esta definido. En caso contrario
    despliega Mocks de ese contrato

    Args:
        contract_name (String)
        returns:
            brownie.network.contract.ProjectContract: Implementacion mas reciente de este contrato
    """
    contract_type = contract_to_mock[contract_name]
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIROMENTS:
        if len(contract_type) <= 0:
            deploy_mocks()

        contract = contract_type[-1]

    else:
        contract_address = config["networks"][network.show_active()][contract_name]
        contract = Contract.from_abi(
            contract_type._name, contract_address, contract_type.abi
        )
        return contract


def deploy_mocks():
    account = getAccount()

    MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE)
    print("Mocks deployed")
