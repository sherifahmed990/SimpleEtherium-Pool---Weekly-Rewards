import brownie

def test_withdraw_function(ETHPoolContract, accounts):

    ETHPoolContract.deposit({'value': "1 ether"})

    """
    Test if a user can call withdraw with amount 0 
    """
    with brownie.reverts("Amount must be higher than 0."):
        ETHPoolContract.withdraw(0)

    """
    Test if a user can withdraw higher than his balance
    """
    userBalance = ETHPoolContract.depositBalances(accounts[0])
    with brownie.reverts("No suffecient funds in user balance."):
        ETHPoolContract.withdraw(userBalance+1)

    """
    Test if a user balance is updated after a withdraw
    """
    ETHPoolContract.withdraw(10**2)
    assert ETHPoolContract.depositBalances(accounts[0]) == userBalance - 10**2

    """
    Test if a user the withdraw amount is transfered to the caller account
    """
    userAccountBalance = accounts[0].balance()
    ETHPoolContract.withdraw(10**2)
    assert accounts[0].balance() == userAccountBalance + 10**2

    """
    Test if a user balance after withdraw is less than the minimum, 
        all the remaining balance is added to the amount transfered
        and the user balance is set is 0
    """
    ETHPoolContract.setMinBalance(10**5)
    userContractBalance = ETHPoolContract.depositBalances(accounts[0])
    userAccountBalance = accounts[0].balance()
    ETHPoolContract.withdraw(userContractBalance - 10**3)
    assert accounts[0].balance() == userAccountBalance + userContractBalance
    assert ETHPoolContract.depositBalances(accounts[0]) == 0

    """
    Test Withdraw event emitted after deposit
    """
    ETHPoolContract.deposit({'value': "1 ether"})
    withdraw = ETHPoolContract.withdraw(10**2)
    assert 'Withdraw' in withdraw.events
    
