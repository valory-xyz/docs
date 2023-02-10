The life cycle of a service registered in the Autonolas Protocol passes through the following states:

* pre-registration,
* active registration,
* finished registration,
* deployed, and
* terminated bonded.

You can see the current state of a service by browsing the [services section](https://protocol.autonolas.network/services) in the frontend, and clicking on the corresponding service.

<figure markdown>
![Life cycle of a service](images/life_cycle_of_a_service.svg){ align=left width=600 }
</figure>

Only the service owner can change the state of a given service. Connect your wallet to the frontend in order to make changes.

## Pre-registration

A service that [has just been registered](./register_packages_on-chain.md#register-a-service) will be in pre-registration state.
In this state the service owner can make amendments by pressing the button _Update_.
Press the button _Activate Registration_ to advance to the next state. The connected wallet will ask to approve the transaction.

## Active registration

Agent operators must specify the addresses (starting by `0x...`) of their agent instances that are part of the service, and press _Register Agents_ to associate them with the service.

Once all agent instances have been registered, the service owner can press the button _Terminate_ to proceed to the next state. Wallets will ask to approve the transactions.

## Finished Registration

The goal of this state is to deploy the [Gnosis Safe](https://gnosis-safe.io/) multisig contract that will be associated with the service. The parameters shown in this screen are related to the creation of the safe (check the `setup` method [here](https://github.com/safe-global/safe-contracts/blob/main/contracts/Safe.sol)). If you are not familiar with the setup of such contracts, simply leave the default values and press the button _Submit_. The connected wallet will ask to approve the transaction.

## Deployed

Congratulations! Your service is now in the **Deployed** state!

This is the default operational state of an active service. Agent operators can turn on their agent instances at this point. The service owner can terminate the operation of the service by pressing the button _Terminate_. The connected wallet will ask to approve the transaction.

## Terminated bonded

A terminated service can be reactivated again by unbonding its registered agents. The service owner can do so by pressing the button _Unbond_. Once again, the connected wallet will ask to approve the transaction. The service will transit to the **pre-registration** state, enabling the registration of new agent instances.
