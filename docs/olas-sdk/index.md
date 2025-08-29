# Bring your agent to the Olas Protocol

Agents built with any framework can now be brought to the Olas Protocol in just a few steps.

This allows you to:

- Monetize your agent by earning [Dev Rewards](https://open-autonomy.docs.autonolas.tech/protocol/tokenomics/).
- Start your agent with all of the wallet abstraction necessary to make on-chain transactions.

The Olas SDK is a set of tools and instructions that allows engineers to register autonomous agents built with any framework on the {{ autonolas_protocol_registry_dapp }}. Once registered, you can start your agent using the {{ olas_operate_quickstart }} or the {{ olas_operate_app }}.


## Step 1: Build the agent supporting the following requirements
- **ENTRYPOINT**: A script file should be used to start the agent execution.
- **AGENT EOA**: Agent reads the file `ethereum_private_key.txt` from its working directory, which contains the Agent EOA private key.
- **SERVICE SAFE**: Agent reads the environment variable `CONNECTION_CONFIGS_CONFIG_SAFE_CONTRACT_ADDRESSES` which contains the addresses of the Agent Safe in the relevant chains. Syntax is a JSON object with the chain as the key (e.g., `{ "gnosis": "0xE7CA89bE11A7A3b3d0bF6016d7a09f33c03a0a8f" }`).
- **LOGS**: Agent produces a `log.txt` file in its working directory. Log file follows format `[YYYY-MM-DD HH:MM:SS,mmm] [LOG_LEVEL] [agent] Your message`.
- **HEALTHCHECK**: Agent exposes the endpoint at `GET http://localhost:8716/healthcheck`. Healthcheck response satisfies the required JSON format (`seconds_since_last_transition`, `is_transitioning_fast`, etc.).
- **AGENT UI** (optional): Agent exposes the endpoint at `GET http://localhost:8716/`. Agent handles `POST` requests for real-time communication if needed. Endpoints can also return HTML content with appropriate `content-type` headers for agent specific UI.
- **ENVIRONMENT VARIABLES**: Agent uses standard environment variables set by the SDK where needed (`ETHEREUM_LEDGER_RPC`, `GNOSIS_LEDGER_RPC`, `BASE_LEDGER_RPC`, etc.). 
All the used environment variables are specified in the service template JSON with the standard schema.
The same environment variables are mentioned in the `service.yaml` of the service package prepared in [Step 2](#step-2-build-olas-agent-configuration), and used by the agent with the prefix path where these variables are mentioned. For example: `CONNECTION_CONFIGS_CONFIG_<variable_name>`.
- **WITHDRAWAL** (optional): Agent handles withdrawal of invested funds to Agent Safe. Agent works in withdrawal mode by reading the environment variable `WITHDRAWAL_MODE=true`.


## Step 2: Build Olas Agent Configuration
Check the guide at [Olas SDK Starter](https://github.com/valory-xyz/olas-sdk-starter/blob/main/README.md).


## Step 3: Mint it

To register the agent in the {{ autonolas_protocol_registry_dapp }}, follow the steps in this guide: [Mint an Agent](https://stack.olas.network/protocol/mint_packages_nfts/#mint-an-agent).

**Note 1:** Your Olas Agent must provide at least one dependency, as default specify the value 1. 

**Note 2:** The agent, service, and component hashes can be found in **`packages/packages.json`** from [Step 2](#step-2-build-olas-agent-configuration).


## Step 4: Execute it

There are two ways to run your Olas Agent:

1. Using the {{ olas_operate_quickstart }} - [Steps below](#1-using-the-quickstart).
2. Using the {{ olas_operate_app }} - [Steps below](#2-using-the-pearl-app).

### 1. Using the Quickstart
To run the agent using {{ olas_operate_quickstart }}, follow these steps:

#### 1. Publish it
Push the Docker image to [Docker Hub](https://hub.docker.com/).
You can find a docker file example [here](https://github.com/valory-xyz/langchain_hello_world/blob/main/Dockerfile).

- **Image Name**: The image name must be:

    ```
    <author_name>/oar-<agent_name>:<agent_package_hash>
    ```
    - **`author_name`** and **`agent_name`**: These must match the names defined at [Step 2](#step-2-build-olas-agent-configuration) in the Olas agent and service configuration.
    
    - **`agent_package_hash`**: The hash generated when the Olas agent package was pushed to IPFS. This can be found in **`packages/packages.json`** from [Step 2](#step-2-build-olas-agent-configuration).

#### 2. Clone the {{ olas_operate_quickstart }} repository:
   ```sh
   git clone https://github.com/valory-xyz/quickstart
   ```

#### 3. Add a `config.json` file to the `configs` folder with the following fields:

- **`agent_name`**: The name of your Olas Agent defined on [Step 2](#step-2-build-olas-agent-configuration).
- **`agent_id`**: The id of your agent minted on {{ autonolas_protocol_registry_dapp }}, this is number you see on your agent page from [Step 3](#step-3-mint-it).
- **`service_hash`**: The hash of your Olas Service generated on [Step 2](#step-2-build-olas-agent-configuration).
- **`env_variables`**: Here you can define the environment variables that your agent needs, the names must follow what was configured on the file `service.yaml` on [Step 2](#step-2-build-olas-agent-configuration). The provision type of these variables can be:
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

#### 4. Once all the {{ olas_operate_quickstart }} repo requirements are met, start the service by running:
```sh
./run_service.sh <agent_config.json>
```
where `<agent_config.json>` is the path of the configuration file you created in the previous step (e.g., `config_hello_world.json`).

This script will

- Prompts for the Gnosis RPC and required environment variables.
- Sets up the service safe and agent wallet (asking for required funds).
- Mints the service in the registry and deploy it.
- Downloads the agent's docker image.
- Sets up and starts the docker container.


### 2. Using the Pearl App
To run the agent using {{ olas_operate_app }}, follow these steps:

#### 1. Build the binaries

You also have the option to build a standalone executable binary of your agent and use it in place of Docker containers. While the process of creating the binary is at the discretion of the agent developers, it is essential to adhere to the same specifications outlined in the [requirements](#step-1-build-the-agent-supporting-the-following-requirements).

[Here's an example](https://github.com/valory-xyz/agents-fun-eliza/blob/main/docs/binary_building.md) of how to build a binary of an Eliza agent. Note that the process can be different depending on the agent framework used.

#### 2. Prepare the Github workflow file

Prepare a Github workflow file to build the standalone binary executables of your agent.
You may find an example of the Eliza agent's GitHub workflow [here](https://github.com/valory-xyz/agents-fun-eliza/blob/main/.github/workflows/binary_builder.yaml).

**Note** Ensure the binaries name follows the format `f"agent_runner_{os_name}_{arch}"`. For example, [here](https://github.com/valory-xyz/trader/releases/tag/v0.0.101) you can find the binaries for the Trader agent.

#### 3. Contact the Pearl team
Reach out to the Pearl team to request the addition of your agent to the {{ olas_operate_app }}.

## Agent examples
Here you can see the examples of two agents built with different frameworks:

- [Langchain Hello World Agent](https://github.com/valory-xyz/langchain_hello_world)

- [Eliza Memeooorr Agent](https://github.com/valory-xyz/agents-fun-eliza)
