Olas SDK is a set of tools and instructions that allow engineers to register autonomous agents built with any framework to be registered on {{ autonolas_protocol_registry_dapp }} and executed through {{ olas_agent_quickstart }}

## Step 1: Building the Agent

The agent can be built using any framework and it will be made available through the deployment of Olas Agent Configuration (step 2) and a docker image (step 3).

### Considerations for building the agent
- Environment variables will be set up in a docker container when the service starts through {{ olas_agent_quickstart }} with the prefix `CONNECTION_CONFIGS_CONFIG_<variable_name>`.
- {{ olas_agent_quickstart }} will deploy a service from a given agent and configure the service multisig Safe and the agent EOA. These information will be available in the docker container as follows:
    - The agent EOA private key will be on the file `/agent_key/ethereum_private_key.txt`.
    - The service safe contract address will be accessible through the environment variable `CONNECTION_CONFIGS_CONFIG_SAFE_CONTRACT_ADDRESSES` as a dictionary with the chain as the key (e.g., `{ "gnosis": "0xE7CA89bE11A7A3b3d0bF6016d7a09f33c03a0a8f" }`).

### Agent examples
Here you can see the examples of two agents built with different frameworks:

- [Langchain Hello World Agent](https://github.com/valory-xyz/langchain_hello_world)

- Eliza Memeooorr Agent (link to repo will be added soon)

## Step 2: Olas Agent and Service Configuration
Once the agent is ready, the next step is to configure the Olas Agent and Service. 

Check the guide at [Olas SDK Starter](https://github.com/valory-xyz/olas-sdk-starter/blob/main/README.md).

## Step 3: Docker Image
Once the Olas Agent configuration is complete, the next step is to push the Docker image to [Docker Hub](https://hub.docker.com/). The image needs to follow the requirements below:

### Docker Image Requirements

- **ENTRYPOINT**: A script file should be used to start the agent execution.
- **HEALTHCHECK**: A health check must be defined; otherwise, the agent will not be executed through {{ olas_agent_quickstart }}.

You can find a docker file example [here](https://github.com/valory-xyz/langchain_hello_world/blob/main/Dockerfile).

- **Image Name**: The image name must be:

    ```
    <author_name>/oar-<agent_name>:<agent_package_hash>
    ```
    - **`author_name`** and **`agent_name`**: These must match the names defined at Step 2 in the Olas agent and service configuration.
    
    - **`agent_package_hash`**: The hash generated when the Olas agent package was pushed to IPFS. This can be found in **`packages/packages.json`** from Step 2.

## Step 4: Minting the Olas Agent
To register the agent in the {{ autonolas_protocol_registry_dapp }}, follow the steps in this guide: [Mint an Agent](https://docs.autonolas.network/protocol/mint_packages_nfts/#mint-an-agent).

**Note 1:** Your Olas Agent must provide at least one dependency, as default specify the value 1. 

**Note 2:** The agent hash can be found in **`packages/packages.json`** from Step 2.

## Executing the Agent via {{ olas_agent_quickstart }}
To run the agent using {{ olas_agent_quickstart }}, follow these steps:

### 1. Clone the {{ olas_agent_quickstart }} repository:
   ```sh
   git clone https://github.com/valory-xyz/quickstart
   ```

### 2. Add a `config.json` file to the `configs` folder with the following fields:

- **`agent_name`**: The name of your Olas Agent defined on Step 2.
- **`agent_id`**: The id of your agent minted on {{ autonolas_protocol_registry_dapp }}, this is number you see on your agent page from Step 4.
- **`service_hash`**: The hash of your Olas Service generated on Step 2.
- **`env_variables`**: Here you can define the environment variables that your agent needs, the names must follow what was configured on the file `service.yaml` on Step 2. The provision type of these variables can be:
    - **user**: It will prompt the user running your agent to provide a value.
    - **fixed**: It will use the value defined on the configuration file.
    - **computed**: It will be automatically computed.


  **Example of `config_hello_world.json`**

```json
{
    "name": "<agent_name>",
    "hash": "<service_hash>",
    "description": "My awesome agent service",
    "image": "",
    "service_version": "v0.1.0",
    "home_chain": "gnosis",
    "configurations": {
        "gnosis": {
            "agent_id": <agent_id>,
            "nft": "bafybeifgj3kackzfoq4fxjiuousm6epgwx7jbc3n2gjwzjgvtbbz7fc3su",
            "threshold": 1,
            "use_mech_marketplace": false,
            "fund_requirements": {
                "0x0000000000000000000000000000000000000000": {
                    "agent": 0,
                    "safe": 0
                }
            }
        }
    },
    "env_variables": {
        "SAFE_CONTRACT_ADDRESSES": {
            "name": "Safe contract addresses",
            "description": "",
            "value": "",
            "provision_type": "computed"
        },
        "GNOSIS_LEDGER_RPC": {
            "name": "Gnosis ledger RPC",
            "description": "",
            "value": "",
            "provision_type": "computed"
        },
        "<ENV_VAR_NAME_1>": {
            "name": "<ENV_VAR_NAME_1>",
            "description": "",
            "value": "",
            "provision_type": "user"
        },
        "<ENV_VAR_NAME_2>": {
            "name": "<ENV_VAR_NAME_2>",
            "description": "",
            "value": "",
            "provision_type": "user"
        }
    }
}
```

### 3. Once all the {{ olas_agent_quickstart }} repo requirements are met, start the service by running:
```sh
./run_service.sh <agent_config.json>
```

This script will
    - Prompts for the Gnosis RPC and required environment variables.
    - Sets up the service safe and agent wallet (asking for required funds).
    - Mints the service in the registry until it reaches the `DEPLOYED` state.
    - Downloads the agent's docker image.
    - Setup and starts the docker container.
