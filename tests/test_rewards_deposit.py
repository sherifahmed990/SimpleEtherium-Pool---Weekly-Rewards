import brownie, math

def test_rewards_deposit(ETHPoolContract, accounts):
    """
     Add deposits
    """
    ETHPoolContract.deposit({'value': '1000 wei','from': accounts[0]})
    ETHPoolContract.deposit({'value': '500 wei','from': accounts[1]})
    ETHPoolContract.deposit({'value': '250 wei','from': accounts[2]})
    totalDeposits = 1000 + 500 + 250
    acc0Balance = ETHPoolContract.depositBalances(accounts[0])
    acc1Balance = ETHPoolContract.depositBalances(accounts[1])
    acc2Balance = ETHPoolContract.depositBalances(accounts[2])

    expectedAccount0Balance = acc0Balance + math.trunc((acc0Balance * 100) / totalDeposits)
    expectedAccount1Balance = acc1Balance + math.trunc((acc1Balance * 100) / totalDeposits)
    expectedAccount2Balance = acc2Balance + math.trunc((acc2Balance * 100) / totalDeposits)

    ETHPoolContract.addTeamMember(accounts[1])
    ETHPoolContract.depositAndDestriputeRewards({'value': '100 wei','from': accounts[1]})
    """
     After calling depositAndDestriputeRewards, all the users blances are marked as locked.
    """

    """
    Test if the first distributed rewards correspond to 
    the users balances when the rewards was deposited.
    (doesn't depend on the time of the users deposits)
    """
    assert ETHPoolContract.depositBalances(accounts[0]) == expectedAccount0Balance
    assert ETHPoolContract.depositBalances(accounts[1]) == expectedAccount1Balance
    assert ETHPoolContract.depositBalances(accounts[2]) == expectedAccount2Balance

    """
        After the first rewards deposit , all deposits will be rewarded based on the locked
        balance (meaning the balance that stayed in the pool for the period between 
        two rewards deposits)
    """
    lockedAccount0Balance = ETHPoolContract.depositBalances(accounts[0])
    lockedAccount1Balance = ETHPoolContract.depositBalances(accounts[1])
    lockedAccount2Balance = ETHPoolContract.depositBalances(accounts[2])

    
    """
     Add deposits
    """
    ETHPoolContract.deposit({'value': '2000000 wei','from': accounts[0]})
    totalDeposits += 2000000

    """
     Withdraw from the locked amount
    """
    ETHPoolContract.withdraw(100, {'from': accounts[1]})
    lockedAccount1Balance -= 100
    totalDeposits += 2000000 - 100

    totalLockedDeposits = lockedAccount0Balance + lockedAccount1Balance + lockedAccount2Balance

    acc0Balance = ETHPoolContract.depositBalances(accounts[0])
    acc1Balance = ETHPoolContract.depositBalances(accounts[1])
    acc2Balance = ETHPoolContract.depositBalances(accounts[2])

    expectedAccount0Balance = acc0Balance + math.trunc((lockedAccount0Balance * 200) / totalLockedDeposits)
    expectedAccount1Balance = acc1Balance + math.trunc((lockedAccount1Balance * 200) / totalLockedDeposits)
    expectedAccount2Balance = acc2Balance + math.trunc((lockedAccount2Balance * 200) / totalLockedDeposits)

    ETHPoolContract.depositAndDestriputeRewards({'value': '200 wei','from': accounts[1]})

    """
    Test if the second distributed rewards correspond to the users locked balances.
    """
    assert ETHPoolContract.depositBalances(accounts[0]) == expectedAccount0Balance
    assert ETHPoolContract.depositBalances(accounts[1]) == expectedAccount1Balance
    assert ETHPoolContract.depositBalances(accounts[2]) == expectedAccount2Balance

    acc1Balance = ETHPoolContract.depositBalances(accounts[1])   
    ETHPoolContract.setMinBalance(100)
    """
     Withdraw all avaliable balance
    """
    ETHPoolContract.withdraw(acc1Balance-10, {'from': accounts[1]})
    ETHPoolContract.depositAndDestriputeRewards({'value': '200 wei','from': accounts[1]})
    """
    Test if users with zero balance is removed from the users array
    after calling the depositAndDestriputeRewards function
    """
    assert not ETHPoolContract.users(1) == accounts[1]

    

    