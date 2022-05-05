<br />
<div align="center">
  <h3 align="center">Simple Etherium Pool - Weekly Rewards</h3>
</div>


<!-- ABOUT THE PROJECT -->
## About The Project

ETHPool provides a service where people can deposit ETH and they will receive weekly
rewards. Users must be able to take out their deposits along with their portion of rewards
at any time. New rewards are deposited manually into the pool by the ETHPool team
each week using a contract function.

## Deployed and verified contracts
* ETHPool (kovan) = "0xc2FddDDAF6Af6C33d6B4C24a4efF74506b849BE1"
https://kovan.etherscan.io/address/0xc2FddDDAF6Af6C33d6B4C24a4efF74506b849BE1

### Deploy Contract
    brownie account new KovanDeploy
    brownie run scripts/deploy.py --network kovan

### Run the interact.py script
    
    brownie account new user1
    brownie account new user2
    brownie run scripts/interact.py --network kovan

    
### Built With
This Project is build with:

* [Solidity](soliditylang.org)
* [Brownie](https://eth-brownie.readthedocs.io/)


<!-- CONTACT -->
## Contact

Sherif Abdelmoatty - [@SherifA990](https://twitter.com/SherifA990) - sherif.ahmed990@gmail.com