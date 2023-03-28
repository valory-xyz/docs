# Autonolas Protocol

<figure markdown>
![Autonolas Protocol logo](images/protocol.png){ align=left width="150" }
</figure>

The **Autonolas Protocol** is a collection of smart contracts that implements a mechanism to secure open-source code on-chain, and provides incentives to developers proportionally for their efforts in supporting the growth of the Autonolas ecosystem. The protocol is built with the {{open_autonomy}} framework in mind as the primary framework for realizing agent services,  alternative frameworks can also be used.

The Autonolas Protocol is [currently deployed](./registry_technical_overview.md#contract-addresses) on Ethereum mainnet and Görli testnet, and it will be eventually deployed on all major smart-contract blockchains.

## Components

There are three main elements that make up the protocol:

* The **On-Chain Registry** anchors Autonolas autonomous services on-chain, and provides the primitives needed to create, operate and secure such services.

* The **Tokenomics** defines an economic model facilitated by the [OLAS token](https://etherscan.io/token/0x0001A500A6B18995B03f44bb040A5fFc28E45CB0). This is a mechanism to grow the capital deployed in services and reward developers.

* **Governance** defines the rules of Autonolas as a decentralized, autonomous
organization (DAO), which is governed by the community.

<figure markdown>
![Autonolas Protocol elements](./images/autonolas_protocol_elements.svg)
</figure>

!!! abstract "Learn more"

    Read the **Technical Architecture**, **Tokenomics** and **Governance** sections in the [Autonolas Whitepaper](https://www.autonolas.network/documents/whitepaper/Whitepaper%20v1.0.pdf) for the full details of the **Autonolas Protocol**.

## Rationale

In most settings, the reward model for service owners and agent operators is usually straightforward: users remunerate service owners, and service owners remunerate operators supporting their service. However it is not always well-defined how this is propagated to open-source software developers. This is where the Autonolas Protocol plays its role.

Autonolas strives to propose a model where open-source developers benefit from their contributions to the community by incentivizing software **composability**, **reusability** and **utility**. Software packages (components and agents) brought to the Autonolas ecosystem are secured and minted as NFTs in the Autonolas protocol. These packages can be used to compose agents and services, and the protocol has mechanisms to unambiguously represent the actual software/system composition on-chain. This is a crucial feature to [measure the utility](https://github.com/valory-xyz/autonolas-tokenomics/blob/main/docs/Autonolas_tokenomics_audit.pdf) of the code brought by developers and provide a fair reward for their contributions.

<figure markdown>
![](./images/protocol_developer_perspective.svg)
</figure>
