# Autonolas Protocol

<figure markdown>
![Autonolas Protocol logo](images/protocol.png){ align=left width="150" }
</figure>

The on-chain **Autonolas Protocol** anchors the Autonolas autonomous services -and in particular the current incarnation as agent services- on the target settlement layer and provides the primitives needed to create, operate and secure such services. The protocol benefits from a modular design with a clear separation of concerns and opportunity for extensibility without compromising its security and permissionless nature.

!!! info

    The Autonolas Protocol is currently deployed in Ethereum and Goerly chains, and it will be progressively deployed in all major blockchains.

From an architectural point of view, the smart contracts that make up the Autonolas Protocol satisfy the following properties:

* Follow a core-periphery architecture (such as in Uniswap), which allows for changing out periphery functionality without changing the data models at the core.
* Allow for extension via modules (such as in MakerDAO).

Examples of modules include governance and staking. Governance is particularly important in a modular system, as it is used to vote on the adoption or abandoning of modules. By ensuring an immutable core, the Autonolas protocol provides guarantees that once created, the ecosystem’s agent components, canonical agents, and services are not mutable by governance – an important guarantee of censorship resistance.

The Autonolas Protocol is built with the {{open_autonomy}} framework in mind as the primary framework for realizing agent services. However, it does not prescribe the usage of the {{open_autonomy}} framework and allows for services to be implemented on alternative frameworks.

!!! abstract "Learn more"

    Read the **Technical Architecture**, **Tokenomics** and **Governance** sections in the [Autonolas Whitepaper](https://www.autonolas.network/documents/whitepaper/Whitepaper%20v1.0.pdf) for the full details of the **Autonolas Protocol**.

## Core smart contracts

Core smart contracts are permissionless. Autonolas governance controls the process of service management functionalities and of minting new NFTs representing components and agents (i.e. it can change the minting rules and pause minting). The remaining functionalities, in particular transfer functionalities, are not pausable by governance.

**Generic Registry**
:	An abstract smart contract for the generic registry template which inherits the Solmate ERC721 implementation. 

**Unit Registry**
:	An abstract smart contract for generic agents/components template which inherits the GenericRegistry

**Component Registry**
:	An ERC721 contract that inherits the UnitRegistry and represents agent components.

**Agent Registry**
:	An ERC721 contract that inherits the UnitRegistry and represents canonical agents.

**Service Registry**
:	An ERC721 contract that inherits the GenericRegistry, is used to represent services and provides service management utility methods.

Autonolas extends the ERC721 standard to support appending additional hashes to the NFT over time. This allows developers and service owners to record version changes in their code or configuration, and to signal it on-chain without breaking backward compatibility.

## Periphery smart contracts

Periphery contracts are fully controlled by the governance and can be replaced to enable new functionality. They also act as guards to restrict existing functionality.

**Generic Manager**
:	An abstract smart contract for the generic registry manager template.

**Registries Manager**
:	A contract inheriting from GenericManager via which developers can mint component and agent NFTs.

**Service Manager**
:	A contract inheriting from GenericManager via which service owners can create and manage their services.
