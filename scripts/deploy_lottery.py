from brownie import accounts, Lottery, Contract, config, network
from scripts.helpful_scripts import getAccount, get_contract


def deploy_lottery():
    account = getAccount()
    lottery = Lottery.deploy(
        get_contract("link_token").address,
        get_contract("vrf_coordinator").address,
        get_contract("eth_usd_price_feed").address,
        config["networks"][network.show_active()]["fee"],
        config["networks"][network.show_active()]["key_hash"],
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )

    print("Lotery deployed")


def start_lottery():
    account = getAccount()
    lottery = Lottery[-1]
    starting_txn = lottery.startLottery({"from": account})

    starting_txn.wait(1)
    print("Lottery Started")


def enter_lottery():
    account = getAccount()
    lottery = Lottery[-1]
    value = lottery.getEntranceFee() + 100000000


def main():
    deploy_lottery()
    start_lottery()
    enter_lottery()
