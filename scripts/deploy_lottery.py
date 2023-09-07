from brownie import accounts, Lottery, Contract
from scripts.helpful_scripts import getAccount


def deploy_lottery():
    account = getAccount()
    lottery = Lottery.deploy(
        get_contract()
    )

def main():
    deploy_lottery()

