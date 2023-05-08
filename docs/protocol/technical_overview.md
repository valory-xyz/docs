The **Autonolas Protocol** benefits from a modular design with a clear separation of concerns and opportunity for extensibility without compromising its security and permissionless nature. From an architectural point of view, the smart contracts that make up the protocol satisfy the following properties:

* Follow a core-periphery architecture (such as in [Uniswap](https://docs.uniswap.org/contracts/v2/concepts/protocol-overview/smart-contracts)), which allows for changing out periphery functionality without changing the data models at the core.
* Allow for extension via modules (such as in [MakerDAO](https://docs.makerdao.com/)).

Examples of modules include governance and staking. Governance is particularly important in a modular system, as it is used to vote on the adoption or abandoning of modules. By ensuring an immutable core, the protocol provides guarantees that once created, the ecosystem’s agent components, canonical agents, and services are not mutable by governance – an important guarantee of censorship resistance.

!!! abstract "Learn more"

    Read the **Technical Architecture**, **Tokenomics** and **Governance** sections in the [Autonolas Whitepaper](https://www.autonolas.network/documents/whitepaper/Whitepaper%20v1.0.pdf) for the full details of the **Autonolas Protocol**.

## Registry

This section gives an overview on the technical details of the Autonolas Protocol Registry, where NFTs representing software packages can be minted.

### Core smart contracts

Core smart contracts are permissionless. Autonolas governance controls the process of service management functionalities and of minting new NFTs representing components and agents (i.e. it can change the minting rules and pause minting). The remaining functionalities, in particular transfer functionalities, are not pausable by governance.

<figure markdown>
![Core smart contracts](./images/core_smart_contracts.svg)
</figure>

**Generic Registry**
:	An abstract smart contract for the generic registry template which inherits the Solmate ERC721 implementation. 

**Unit Registry**
:	An abstract smart contract for generic agents/components template which inherits the Generic Registry.

**Component Registry**
:	An ERC721 contract that inherits the Unit Registry and represents agent components.

**Agent Registry**
:	An ERC721 contract that inherits the Unit Registry and represents canonical agents.

**Service Registry**
:	An ERC721 contract that inherits the Generic Registry, is used to represent services and provides service management utility methods.

Autonolas extends the ERC721 standard to support appending additional hashes to the NFT over time. This allows developers and service owners to record version changes in their code or configuration, and to signal it on-chain without breaking backward compatibility.

### Periphery smart contracts

Periphery contracts are fully controlled by the governance and can be replaced to enable new functionality. They also act as guards to restrict existing functionality.

<figure markdown>
![Periphery smart contracts](./images/periphery_smart_contracts.svg)
</figure>

**Generic Manager**
:	An abstract smart contract for the Generic Registry manager template.

**Registries Manager**
:	A contract inheriting from Generic Manager via which developers can mint component and agent NFTs.

**Service Manager**
:	A contract inheriting from Generic Manager via which service owners can create and manage their services.

### Contract addresses

Find below the addresses of the Autonolas Protocol contracts currently deployed in different chains.

<figure markdown>
| Contract           | Ethereum                                                                                                              | Görli                                                                                                                        |
|--------------------|-----------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| Component Registry | [View on Etherscan :material-open-in-new:](https://etherscan.io/address/0x15bd56669F57192a97dF41A2aa8f4403e9491776)   | [View on Etherscan  :material-open-in-new: ](https://goerli.etherscan.io/address/0x7Fd1F4b764fA41d19fe3f63C85d12bf64d2bbf68) |
| Agent Registry     | [View on Etherscan  :material-open-in-new: ](https://etherscan.io/address/0x2F1f7D38e4772884b88f3eCd8B6b9faCdC319112) | [View on Etherscan  :material-open-in-new: ](https://goerli.etherscan.io/address/0xEB5638eefE289691EcE01943f768EDBF96258a80) |
| Service Registry   | [View on Etherscan  :material-open-in-new: ](https://etherscan.io/address/0x48b6af7B12C71f09e2fC8aF4855De4Ff54e775cA) | [View on Etherscan  :material-open-in-new: ](https://goerli.etherscan.io/address/0x1cEe30D08943EB58EFF84DD1AB44a6ee6FEff63a) |
| Registries Manager | [View on Etherscan  :material-open-in-new: ](https://etherscan.io/address/0x9eC9156dEF5C613B2a7D4c46C383F9B58DfcD6fE) | [View on Etherscan  :material-open-in-new: ](https://goerli.etherscan.io/address/0x10c5525F77F13b28f42c5626240c001c2D57CAd4) |
| Service Manager    | [View on Etherscan  :material-open-in-new: ](https://etherscan.io/address/0x38b062d11CD7596Ab5aDFe4d0e9F0dC3218E5389) | [View on Etherscan  :material-open-in-new: ](https://goerli.etherscan.io/address/0xcDdD9D9ABaB36fFa882530D69c73FeE5D4001C2d) |
</figure>

## Tokenomics

!!! info

	This section will be added soon.

## Governance

!!! info

	This section will be added soon.