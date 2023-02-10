This guide describes how to register software packages in the Autonolas Protocol using the [protocol frontend](https://protocol.autonolas.network/). You can register three types of packages: **services**, **agents** and **components**.

## How packages are registered

To register a package in the protocol, it must have been already published into a remote (IPFS) registry. Read [how to publish packages](https://docs.autonolas.network/open-autonomy/guides/publish_fetch_packages/) with the {{open_autonomy}} framework.

The process of registering a package comprises the creation of a **metadata file** which contains a pointer to the IPFS hash of the published software package itself, plus some other additional information required by the protocol. This metadata file is also stored in the IPFS registry. The [protocol frontend](https://protocol.autonolas.network/) will automatically create and publish the metadata file once you provide the necessary information, and it will interact with the protocol smart contracts to complete the registration of your package.

Upon completing the registration process, you will have minted on-chain an NFT representing your package. The process is summarized in the figure below.

<figure markdown>
![Package registration](./images/register_package.svg)
</figure>

## Requirements

In order to register a software package, you must ensure that you have:

* A **crypto wallet** (e.g., [Metamask](https://metamask.io/) or a cold wallet) with funds for the chain that you wish to register the package.
* The **hash of the package** that you want to register on-chain, and which should be already published into a remote registry.
* An **NFT image URL**. This image will be used to represent the minted NFT for the package on marketplaces such as [OpenSea](https://opensea.io/). You can use [this sample image URL](https://gateway.autonolas.tech/ipfs/Qmbh9SQLbNRawh9Km3PMEDSxo77k1wib8fYZUdZkhPBiev) for testing purposes.

## Register a component

Connect your wallet to the frontend, open the [components section](https://protocol.autonolas.network/components) and press the button _Register_. Fill in the data of your component:

  1. **Owner Address.** The wallet address of the component owner (starting by `0x...`). It need not be the address of the wallet connected.

  2. **Generate IPFS hash of metadata file.** Press the button _Generate Hash & File_ and fill in the following data:

      * **Name.** A name for the component.
      * **Description.** A description of the component.
      * **Version.** The component version, in the format, `<major>.<minor>.<patch>`.
      * **Package hash.** The remote registry package hash starting by `bafybei...` obtained when the component was published in the remote registry.
      * **NFT Image URL.** An URL pointing to an image. You can use [this sample image URL](https://gateway.autonolas.tech/ipfs/Qmbh9SQLbNRawh9Km3PMEDSxo77k1wib8fYZUdZkhPBiev) for testing purposes.

      By pressing _Save File & Generate Hash_ a metadada file with this information will be automatically generated and uploaded in the remote registry. You will notice that the hash will be populated in the component registration form.

  3. **Dependencies.** Comma-separated list of component IDs which the component requires. You can find the IDs by browsing the [components section](https://protocol.autonolas.network/components).

Press the button _Submit_. Your wallet will ask you to approve the transaction. Once the transaction is settled, you should see a message indicating that the component has been registered successfully.

## Register an agent

Connect your wallet to the frontend, open the [agents section](https://protocol.autonolas.network/agents) and press the button _Register_. Fill in the data of your agent:

  1. **Owner Address.** The wallet address of the agent owner (starting by `0x...`). It need not be the address of the wallet connected.

  2. **Generate IPFS hash of metadata file.** Press the button _Generate Hash & File_ and fill in the following data:

      * **Name.** A name for the agent.
      * **Description.** A description of the agent.
      * **Version.** The agent version, in the format, `<major>.<minor>.<patch>`.
      * **Package hash.** The remote registry package hash starting by `bafybei...` obtained when the agent was published in the remote registry.
      * **NFT Image URL.** An URL pointing to an image. You can use [this sample image URL](https://gateway.autonolas.tech/ipfs/Qmbh9SQLbNRawh9Km3PMEDSxo77k1wib8fYZUdZkhPBiev) for testing purposes.

      By pressing _Save File & Generate Hash_ a metadada file with this information will be automatically generated and uploaded in the remote registry. You will notice that the hash will be populated in the agent registration form.

  3. **Dependencies.** Comma-separated list of component IDs which the agent requires. You can find the IDs by browsing the [components section](https://protocol.autonolas.network/components).

Press the button _Submit_. Your wallet will ask you to approve the transaction. Once the transaction is settled, you should see a message indicating that the agent has been registered successfully.

## Register a service

Connect your wallet to the frontend, open the [services section](https://protocol.autonolas.network/services) and press the button _Register_. Fill in the data of your service:

  1. **Owner Address.** The wallet address of the service owner (starting by `0x...`). It need not be the address of the wallet connected.

  2. **Generate IPFS hash of metadata file.** Press the button _Generate Hash & File_ and fill in the following data:

      * **Name.** A name for the service.
      * **Description.** A description of the service.
      * **Version.** The service version, in the format, `<major>.<minor>.<patch>`.
      * **Package hash.** The remote registry package hash starting by `bafybei...` obtained when the service was published in the remote registry.      * **NFT Image URL.** An URL pointing to an image. You can use [this sample image URL](https://gateway.autonolas.tech/ipfs/Qmbh9SQLbNRawh9Km3PMEDSxo77k1wib8fYZUdZkhPBiev) for testing purposes.

      By pressing _Save File & Generate Hash_ a metadada file with this information will be automatically generated and uploaded in the remote registry. You will notice that the hash will be populated in the service registration form.

  3. **Canonical agent Ids.** Comma-separated list of agent IDs which the service requires. You can find the IDs by browsing the [agents section](https://protocol.autonolas.network/agents).

  4. **No. of slots to canonical agent Ids.** Specify the number of agent instances for each agent ID listed above.

  5. **Cost of agent instance bond.** Specify (in wei units) what is the bond per each agent instance  joining the service. If you are using it for testing purposes, we suggest that you use a small value (e.g., 1000000000000000 GörliWei = 0.001 GörliETH).

  6. **Threshold.** Specify the threshold of agents required to sign.

Press the button _Submit_. Your  wallet will ask you to approve the transaction. Once the transaction is settled, you should see a message indicating that the service has been registered successfully. You should see that the service is in **Pre-Registration** state.

Once it has been registered, you can [manage the life cycle of a service](./life_cycle_of_a_service.md).
