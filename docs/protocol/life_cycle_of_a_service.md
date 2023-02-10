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

Most of the service state changes are triggered by the service owner. However, some state transitions are also triggered when certain conditions are met (e.g., when an operator registers the last available agent instance in the _active registration_ state). Connect your wallet to the frontend in order to make changes.

## Pre-registration

A service that [has just been registered](./register_packages_on-chain.md#register-a-service) will be in pre-registration state.

**Available actions:**

* The service owner can make amendments by pressing the _Update_ button.
* The service owner can advance to the _active registration_ state by pressing the _Activate Registration_ button.

The connected wallet will ask to approve any transaction.

## Active registration

In this state the service is waiting for agent operators to register their agent instances on the service.

**Available actions:**

* Agent operators can register their agent instances in the service by specifying their addresses (starting with `0x...`) and pressing the _Register Agents_ button. When the last agent instance slot is filled, the service state will transit to the _finished registration_ state automatically.
* The service owner can terminate the service by pressing the _Terminate_ button.

The connected wallet will ask to approve any transaction.

## Finished Registration

This state is reached once all the available slots for agent instances are filled and is waiting for the service owner to continue transiting to the next state.

**Available actions:**

* The service owner can deploy the [Safe](https://gnosis-safe.io/) multisig contract that will be associated with the service. The parameters shown in this screen are related to the creation of the safe (check the `setup` method [here](https://github.com/safe-global/safe-contracts/blob/main/contracts/Safe.sol)). If you are not familiar with the setup of such contracts, simply leave the default values. Press the _Submit_ button to transit to the _deployed_ state.
* The service owner can terminate the service by pressing the _Terminate_ button.

The connected wallet will ask to approve any transaction.

## Deployed

Congratulations! Your service is now in the **Deployed** state!

This is the default operational state of an active service. Agent operators can turn on their agent instances at this point.

**Available actions:**

* The service owner can terminate the service by pressing the _Terminate_ button.

The connected wallet will ask to approve any transaction.

## Terminated bonded

This state is reached whenever the service owner terminates the service at any given state above. The service is waiting for the owner to unbond all registered agents.

**Available actions:**

* The service owner can unbond the registered agent instances by pressing the _Unbond_ button. The service will transit to the **pre-registration** state, enabling the registration of new agent instances.

The connected wallet will ask to approve any transaction.
