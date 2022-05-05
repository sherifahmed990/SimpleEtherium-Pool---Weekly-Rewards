import pytest

@pytest.fixture(autouse=True)
def setup(fn_isolation):
    """
    Isolation setup fixture.
    This ensures that each test runs against the same base environment.
    """
    pass

@pytest.fixture(scope="module")
def ETHPoolContract(accounts, ETHPool):
    """
    Yield a `Contract` object for the ETHPool contract.
    """
    yield accounts[0].deploy(ETHPool)
