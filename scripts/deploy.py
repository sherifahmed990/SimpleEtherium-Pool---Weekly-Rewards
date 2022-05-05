from brownie import ETHPool, accounts

def main():
    owner = accounts.load("KovanDeploy")
    ETHPoolContract = ETHPool.deploy({'from':owner}, publish_source=True)