from brownie import ETHPool, accounts

def main():
    owner = accounts.load("KovanDeploy")
    user1 = accounts.load("user1")
    user2 = accounts.load("user2")
    ETHPoolContract = ETHPool.at("0xc2FddDDAF6Af6C33d6B4C24a4efF74506b849BE1")
    
    #ETHPoolContract.removeTeamMember("0xe48D5A8Ebb82d0365Cd734840b6d15e3370ca913",{'from':owner})
    ETHPoolContract.addTeamMember("0xe48D5A8Ebb82d0365Cd734840b6d15e3370ca913",{'from':owner})

    ETHPoolContract.setMinBalance(50,{'from':owner})
    ETHPoolContract.deposit({'value': '300 wei','from':owner})
    ETHPoolContract.deposit({'value': '200 wei','from':user1})
    ETHPoolContract.deposit({'value': '100 wei','from':user2})
    ETHPoolContract.withdraw(50,{'from':owner})
    ETHPoolContract.depositAndDestriputeRewards({'value': '10000 wei','from':owner})
    ETHPoolContract.deposit({'value': '400 wei','from':owner})
    ETHPoolContract.depositAndDestriputeRewards({'value': '700 wei','from':owner})
    
    balance0 = ETHPoolContract.depositBalances(owner,{'from':owner})
    balance1 = ETHPoolContract.depositBalances(user1,{'from':user1})
    balance2 = ETHPoolContract.depositBalances(user2,{'from':user2})

    print("Account0 balance is ", balance0)
    print("Account1 balance is ", balance1)
    print("Account2 balance is ", balance2)


    