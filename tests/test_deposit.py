import brownie

def test_deposit_function(ETHPoolContract, accounts):
    """
    Test if a user can call deposit with 0 ether sent
    """
    with brownie.reverts("No Ether to deposit!"):
        ETHPoolContract.deposit()

    """
    Test if a user balance is updated after a deposit
    """
    ETHPoolContract.deposit({'value': "1 ether"})
    assert ETHPoolContract.depositBalances(accounts[0]) == 10**18

    """
    Test if a user the deposit amount is deducted from the caller account
    """
    userAccountBalance = accounts[0].balance()
    ETHPoolContract.deposit({'value': "1 ether"})
    assert accounts[0].balance() == userAccountBalance - 10**18

    """
    Test if a user can make a first deposit less than the minimum balance
    """
    ETHPoolContract.setMinBalance(10**5)
    with brownie.reverts("Deposit amount is less that the minimum allowed."):
        ETHPoolContract.deposit({'value': "1 wei",'from': accounts[3]})

    """
    Test if a user added to users list after deposit
    """
    ETHPoolContract.deposit({'value': '1 ether','from': accounts[2]})
    assert ETHPoolContract.users(0) == accounts[0]
    assert ETHPoolContract.users(1) == accounts[2]

    """
    Test if totalDepositBalance increased after deposit
    """
    tdb = ETHPoolContract.totalDepositBalance()
    ETHPoolContract.deposit({'value': "1 ether"})
    assert ETHPoolContract.totalDepositBalance() == tdb + 10**18

    """
    Test Deposit event emitted after deposit
    """
    deposit = ETHPoolContract.deposit({'value': "1 ether"})
    assert 'Deposit' in deposit.events