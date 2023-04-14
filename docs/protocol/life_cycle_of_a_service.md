The life cycle of a service minted in the Autonolas Protocol consists of the following stages:

1. Pre-Registration
2. Active Registration
3. Finished Registration
4. Deployed
5. Terminated Bonded

!!! example

    Look at [this service](https://protocol.autonolas.network/services/1) on the Protocol app to see the current state of a live service.

The figure below summarizes the life cycle and the actions that provoke a transition between states. Most of the service state transitions are initiated by the service owner. However, some state transitions are also triggered automatically. For example, when an operator registers the last available agent instance in the _Active Registration_ state, the service will automatically transit to the _Finished Registration_ state.

<figure markdown>
![Life cycle of a service](images/life_cycle_of_a_service.svg){ align=left width=650 }
</figure>

## Service states

This section details the states of a service minted in the Autonolas Protocol, as well as how to transit between them. You need to connect your wallet to the [Autonolas Protocol web app](https://protocol.autonolas.network/) in order to execute the available actions in each state. The connected wallet will ask to approve any transaction.

### Pre-Registration

A service that [has just been minted](./mint_packages_nfts.md#mint-a-service) will be in _Pre-Registration_ (of agent instances) state.

**Available actions:**

* The service owner can make amendments by pressing the _Update_ button.
* The service owner can advance to the _Active Registration_ state by pressing the _Activate Registration_ button.

### Active Registration

The service is waiting for agent operators to register their agent instances.

**Available actions:**

* Agent operators can register their agent instances in the service by specifying their addresses (starting with `0x...`) and pressing the _Register Agents_ button. When the last agent instance slot is filled, the service state will transit to the _Finished Registration_ state automatically.
* The service owner can terminate the service by pressing the _Terminate_ button.

### Finished Registration

All agent instance slots have been filled. Waiting for the service owner to continue deploying the service.

**Available actions:**

* The service owner can deploy the [Safe](https://gnosis-safe.io/) multisig contract that will be associated with the service. The parameters shown in this screen are related to the creation of the safe (check the `setup` method [here](https://github.com/safe-global/safe-contracts/blob/main/contracts/Safe.sol)). If you are not familiar with the setup of such contracts, simply leave the default values. Press the _Submit_ button to transit to the _Deployed_ state.
* The service owner can terminate the service by pressing the _Terminate_ button.

### Deployed

Congratulations! Your service is now in the _Deployed_ state!

The service is in its default operational state. Agent operators can turn on their agent instances at this point.

**Available actions:**

* The service owner can terminate the service by pressing the _Terminate_ button.

### Terminated Bonded

The service has been terminated by the service owner. Waiting for the service owner to unbond all registered agents.

**Available actions:**

* The service owner can unbond the registered agent instances by pressing the _Unbond_ button. The service will transit to the _Pre-Registration_ state, enabling the registration of new agent instances.
