The life cycle of an AI agent minted in the Olas Protocol consists of the following stages:

1. Pre-Registration
2. Active Registration
3. Finished Registration
4. Deployed
5. Terminated Bonded

!!! example

    Look at [this AI agent]({{ autonolas_protocol_registry_dapp_link }}/ethereum/services/1) on the Olas Protocol web app to see the current state of a live AI agent.

The figure below summarizes the life cycle and the actions that provoke a transition between states. Most of the AI agent state transitions are initiated by the AI agent owner. However, some state transitions are also triggered automatically. For example, when an operator registers the last available agent instance in the _Active Registration_ state, the AI agent will automatically transit to the _Finished Registration_ state.

<figure markdown>
![Life cycle of an AI agent](images/life_cycle_of_a_service.svg){ align=left width=650 }
</figure>

## AI agent states

This section details the states of an AI agent minted in the Olas Protocol, as well as how to transit between them. You need to connect your wallet to the {{ autonolas_protocol_registry_dapp }} in order to execute the available actions in each state. The connected wallet will ask to approve any transaction.

### Pre-Registration

An AI agent that [has just been minted](./mint_packages_nfts.md#mint-an-ai-agent) will be in _Pre-Registration_ (of agent instances) state.

Available actions:

* **Update.** The AI agent owner can make amendments on [some parameters of the AI agent](./mint_packages_nfts.md#mint-an-ai-agent).
* **Activate registration.** The AI agent owner can transit the AI agent to the _Active Registration_ state.

### Active Registration

The AI agent is waiting for agent blueprint operators to register their agent instances.

Available actions:

* **Register agent instance.** Agent blueprint operators can register their agent instances in the AI Agent by specifying their addresses (starting with `0x...`). When the last agent instance slot is filled, the AI agent will transit to the _Finished Registration_ state automatically.

    !!! warning "Important"

        When registering agent instance addresses for an AI agent, some conditions have to be met:

        * The operator address (that is, the address of the wallet used to submit the registration transaction) must be different from the agent instance address(es) being registered.
        * The operator address must not be used as agent instance address in any other AI agent.
        * The agent instance address(es) being registered must not be registered in any other AI agent. In order to reuse an agent instance address, the AI agent owner must terminate and unbond them from the AI agent where they are registered.

* **Terminate.** The AI agent owner can terminate the AI agent, which will transit to the _Terminated Bonded_ state (or to the _Pre-Registration_ state if no agent instance has been registered yet).

### Finished Registration

All agent instance slots have been filled. Waiting for the AI agent owner to continue deploying the AI agent.

Available actions:

* **Deploy.** The AI agent owner can deploy the [Safe](https://app.safe.global/) multisig contract that will be associated with the AI agent. The parameters shown in the deploy form are related to the creation of the safe (check the `setup` method [here](https://github.com/safe-global/safe-contracts/blob/main/contracts/Safe.sol)). If you are not familiar with the setup of such contracts, simply leave the default values. The AI agent will transit to the _Deployed_ state.
* **Terminate.** The AI agent owner can terminate the AI agent, which will transit to the _Terminated Bonded_ state.
  
### Deployed

Congratulations! Your AI agent is now in the _Deployed_ state!

The AI agent is in its default operational state. Agent blueprint operators can turn on their agent instances at this point.

Available actions:

* **Terminate.** The AI agent owner can terminate the AI agent, which will transit to the _Terminated Bonded_ state.

### Terminated Bonded

The AI agent has been terminated by the AI agent owner. Waiting for the AI agent owner to unbond all registered agent instances.

Available actions:

* **Unbond.** The AI agent owner can unbond the registered agent instances. The AI agent will transit to the _Pre-Registration_ state, enabling the registration of new agent instances.
