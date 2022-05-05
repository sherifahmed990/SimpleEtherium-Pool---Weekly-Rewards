import brownie

def test_only_governance_can_call_governance_functions(ETHPoolContract, accounts):
    """
    Test if the governance account can add team members
    """
    ETHPoolContract.addTeamMember(accounts[1])
    assert ETHPoolContract.isTeam(accounts[1])

    """
    Test if another account can add team members
    """
    with brownie.reverts():
        ETHPoolContract.addTeamMember(accounts[2],{"from": accounts[1]})

    """
    Test if another account can remove team members
    """
    with brownie.reverts():
        ETHPoolContract.removeTeamMember(accounts[1],{"from": accounts[1]})

    """
    Test if the governance account can remove team members
    """
    ETHPoolContract.removeTeamMember(accounts[1])
    assert not ETHPoolContract.isTeam(accounts[1])

    """
    Test if the governance account can set minimum balance
    """
    ETHPoolContract.setMinBalance(10**5)
    assert ETHPoolContract.minimumBalance() == 10**5
    
    """
    Test if another account can set minimum deposit
    """
    with brownie.reverts():
        ETHPoolContract.setMinBalance(10**5, {"from": accounts[1]})
