from brownie import Lottery, accounts, config, network
from web3 import Web3


def test_get_entranceFee():
    account = accounts[0]

    lottery = Lottery.deploy(
        config["networks"][network.show_active()]["eth_usd_price_feed"],
        {"from": account},
    )
    assert lottery.getEntranceFee() > Web3.toWei(0.014, "ether")
    assert lottery.getEntranceFee() > Web3.toWei(0.017, "ether")
