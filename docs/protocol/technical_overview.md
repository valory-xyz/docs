The **Olas Protocol** benefits from a modular design with a clear separation of concerns and opportunity for extensibility without compromising its security and permissionless nature. From an architectural point of view, the smart contracts that make up the protocol satisfy the following properties:

* Follow a core-periphery architecture (such as in [Uniswap](https://docs.uniswap.org/contracts/v2/concepts/protocol-overview/smart-contracts)), which allows for changing out periphery functionality without changing the data models at the core.
* Allow for extension via modules (such as in [MakerDAO](https://docs.makerdao.com/)).

Examples of modules include governance and staking. Governance is particularly important in a modular system, as it is used to vote on the adoption or abandoning of modules. By ensuring an immutable core, the Olas Protocol provides guarantees that once created, the ecosystem’s agent components, agent blueprints, and AI agents are not mutable by governance – an important guarantee of censorship resistance.

The Olas Protocol is built with the {{open_autonomy}} framework in mind as the primary framework for realizing AI agents. However, it does not enforces the usage of the {{open_autonomy}} framework, and it allows for AI agents to be implemented on alternative frameworks.

!!! abstract "Learn more"

    Read the **Technical Architecture**, **Tokenomics** and **Governance** sections in the {{ autonolas_whitepaper }} for the full details of the **Olas Protocol**.

## Registry

This section gives an overview on the technical details of the Olas Protocol Registry, where NFTs representing software packages can be minted.

### Core smart contracts

Core smart contracts are permissionless. Olas governance controls the process of AI agent management functionalities and of minting new NFTs representing components and agent blueprints (i.e. it can change the minting rules and pause minting). The remaining functionalities, in particular transfer functionalities, are not pausable by governance.

<figure markdown>
![Core smart contracts](./images/core_smart_contracts.svg)
</figure>

**Generic Registry**
:	An abstract smart contract for the generic registry template which inherits the Solmate ERC721 implementation. 

**Unit Registry**
:	An abstract smart contract for generic agent blueprints/components template which inherits the Generic Registry.

**Component Registry**
:	An ERC721 contract that inherits the Unit Registry and represents agent components.

**Agent Blueprint Registry**
:	An ERC721 contract that inherits the Unit Registry and represents canonical agent blueprints.

**Service Registry**
:	An ERC721 contract that inherits the Generic Registry, is used to represent AI agents and provides AI agent management utility methods.

Olas extends the ERC721 standard to support appending additional hashes to the NFT over time. This allows developers and AI agent owners to record version changes in their code or configuration, and to signal it on-chain without breaking backward compatibility.

### Periphery smart contracts

Periphery contracts are fully controlled by the governance and can be replaced to enable new functionality. They also act as guards to restrict existing functionality.

<figure markdown>
![Periphery smart contracts](./images/periphery_smart_contracts.svg)
</figure>

**Generic Manager**
:	An abstract smart contract for the Generic Registry manager template.

**Registries Manager**
:	A contract inheriting from Generic Manager via which developers can mint component and agent blueprint NFTs.

**Service Manager**
:	A contract inheriting from Generic Manager via which AI agent owners can create and manage their AI agents.

### Contract addresses

The [Olas Registries repository](https://github.com/valory-xyz/autonolas-registries) contains the most up-to-date information on the deployment status. Find the currently deployed contract addresses [here](https://github.com/valory-xyz/autonolas-registries/blob/main/docs/configuration.json).

## Tokenomics

!!! info

	This section will be completed soon.

### Contract addresses

The [Olas Tokenomics repository](https://github.com/valory-xyz/autonolas-tokenomics) contains the most up-to-date information on the deployment status. Find the currently deployed contract addresses [here](https://github.com/valory-xyz/autonolas-tokenomics/blob/main/docs/configuration.json).

## Governance

!!! info

	This section will be completed soon.

### Contract addresses

The [Olas Governance repository](https://github.com/valory-xyz/autonolas-governance) contains the most up-to-date information on the deployment status. Find the currently deployed contract addresses [here](https://github.com/valory-xyz/autonolas-governance/blob/main/docs/configuration.json).
