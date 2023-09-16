from brownie import accounts, Lottery, Contract
from scripts.helpful_scripts import getAccount, get_contract


def deploy_lottery():
    account = getAccount()
    lottery = Lottery.deploy(
        get_contract("eth_usd_price_feed").address,
        get_contract("vrf_coordinator").address,
    )


def main():
    deploy_lottery()
