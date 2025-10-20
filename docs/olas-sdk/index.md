# Bring your AI Agent to the Olas Protocol

Agents built with any framework can now be brought to the Olas Protocol in just a few steps.

This allows you to:

- Monetize your agent by earning [Dev Rewards](https://stack.olas.network/protocol/tokenomics/).
- Start your agent with all of the wallet abstraction necessary to make on-chain transactions.

The Olas SDK is a set of tools and instructions that allows engineers to register autonomous agents built with any framework on the {{ autonolas_protocol_registry_dapp }}. Once registered, you can start your agent using the {{ olas_operate_quickstart }} or the {{ olas_operate_app }}.


## Step 1: Build the agent blueprint supporting the following requirements
- **ENTRYPOINT**: A script file should be used to start the agent instance execution.
- **AGENT EOA**: Agent instance reads the file `ethereum_private_key.txt` from its working directory, which contains the Agent instance EOA private key.
- **AI AGENT SAFE**: Agent instance reads the environment variable `CONNECTION_CONFIGS_CONFIG_SAFE_CONTRACT_ADDRESSES` which contains the addresses of the AI Agent Safe in the relevant chains. Syntax is a JSON object with the chain as the key (e.g., `{ "gnosis": "0xE7CA89bE11A7A3b3d0bF6016d7a09f33c03a0a8f" }`).
- **LOGS**: Agent instance produces a `log.txt` file in its working directory. Log file follows format `[YYYY-MM-DD HH:MM:SS,mmm] [LOG_LEVEL] [agent] Your message`.
- **HEALTHCHECK**: Agent instance exposes the endpoint at `GET http://localhost:8716/healthcheck`. Healthcheck response satisfies the required JSON format (`seconds_since_last_transition`, `is_transitioning_fast`, etc.).
- **AGENT UI** (optional): Agent instance exposes the endpoint at `GET http://localhost:8716/`. Agent instance handles `POST` requests for real-time communication if needed. Endpoints can also return HTML content with appropriate `content-type` headers for agent specific UI.
- **ENVIRONMENT VARIABLES**: Agent instance uses standard environment variables set by the SDK where needed (`ETHEREUM_LEDGER_RPC`, `GNOSIS_LEDGER_RPC`, `BASE_LEDGER_RPC`, etc.). 
All the used environment variables are specified in the AI agent template JSON with the standard schema.
The same environment variables are mentioned in the `service.yaml` of the AI agent package prepared in [Step 2](#step-2-build-olas-ai-agent-configuration), and used by the agent with the prefix path where these variables are mentioned. For example: `CONNECTION_CONFIGS_CONFIG_<variable_name>`.
- **WITHDRAWAL** (optional): Agent instance handles withdrawal of invested funds to AI Agent Safe. Agent instance works in withdrawal mode by reading the environment variable `WITHDRAWAL_MODE=true`.


## Step 2: Build Olas AI Agent Configuration
Check the guide at [Olas SDK Starter](https://github.com/valory-xyz/olas-sdk-starter/blob/main/README.md).


## Step 3: Mint it

To register the agent blueprint in the {{ autonolas_protocol_registry_dapp }}, follow the steps in this guide: [Mint an Agent Blueprint](../protocol/mint_packages_nfts.md#mint-an-agent-blueprint).

**Note 1:** Your Olas Agent blueprint must provide at least one dependency, as default specify the value 1.

**Note 2:** The agent blueprint, AI agent, and component hashes can be found in **`packages/packages.json`** from [Step 2](#step-2-build-olas-ai-agent-configuration).

**Note 3:** Components and Agent Blueprints are minted on ETH mainnet only, and then used as "foreign" IDs in AI Agents on any chosen network, since off-chain agent instances read from any chain and unpack configurations and codes following IPFS hashes.

## Step 4: Execute it

There are two ways to run your Olas AI Agent:

1. Using the {{ olas_operate_quickstart }} - [Steps below](#1-using-the-quickstart).
2. Using the {{ olas_operate_app }} - [Steps below](#2-using-the-pearl-app).

### 1. Using the Quickstart
To run the AI agent using {{ olas_operate_quickstart }}, follow these steps:

#### 1. Publish it
Push the agent blueprint Docker image to [Docker Hub](https://hub.docker.com/).
You can find a docker file example [here](https://github.com/valory-xyz/langchain_hello_world/blob/main/Dockerfile).

- **Image Name**: The image name must be:

    ```
    <author_name>/oar-<agent_blueprint_name>:<agent_package_hash>
    ```
    - **`author_name`** and **`agent_blueprint_name`**: These must match the names defined at [Step 2](#step-2-build-olas-ai-agent-configuration) in the Olas agent blueprint and AI agent configuration.

    - **`agent_package_hash`**: The hash generated when the Olas agent blueprint package was pushed to IPFS. This can be found in **`packages/packages.json`** from [Step 2](#step-2-build-olas-ai-agent-configuration).

#### 2. Clone the {{ olas_operate_quickstart }} repository:
   ```sh
   git clone https://github.com/valory-xyz/quickstart
   ```

#### 3. Add a `ai_agent_config.json` file to the `configs` folder:

Refer to the [README](https://github.com/valory-xyz/quickstart?tab=readme-ov-file#guide-for-the-service-configjson) to create a configuration file for your AI agent.
Refer to the other configuration files in the `configs` folder for examples.

#### 4. Once all the {{ olas_operate_quickstart }} repo requirements are met, start the AI agent by running:
```sh
./run_service.sh <ai_agent_config.json>
```
where `<ai_agent_config.json>` is the path of the configuration file you created in the previous step (e.g., `config_hello_world.json`).

This script will

- Prompts for the RPC URL and required environment variables.
- Sets up the AI agent safe and agent instance wallet (asking for required funds).
- Mints the AI agent in the registry and deploy it.
- Downloads the agent blueprint's docker image.
- Sets up and starts the docker container, running as an instance of the agent blueprint.


### 2. Using the Pearl App
To run the AI agent using {{ olas_operate_app }}, follow these steps:

#### 1. Build the binaries

You can build a standalone executable binary of your agent blueprint and use it in place of Docker containers. While the process of creating the binary is at the discretion of the agent blueprint developers, it is essential to adhere to the same specifications outlined in the [requirements](#step-1-build-the-agent-blueprint-supporting-the-following-requirements).

[Here's an example](https://github.com/valory-xyz/agents-fun-eliza/blob/main/docs/binary_building.md) of how to build a binary of an Eliza agent. Note that the process can be different depending on the agent framework used.

#### 2. Prepare the Github workflow file

Prepare a Github workflow file to build the standalone binary executables of your agent blueprint.
You may find an example of the Eliza agent's GitHub workflow [here](https://github.com/valory-xyz/agents-fun-eliza/blob/main/.github/workflows/binary_builder.yaml).

**Note** Ensure the binaries name follows the format `f"agent_runner_{os_name}_{arch}"`. For example, [here](https://github.com/valory-xyz/trader/releases/tag/v0.27.1) you can find the binaries for the Trader agent blueprint.

#### 3. Contact the Pearl team
Reach out to the Pearl team to request the addition of your agent blueprint to the {{ olas_operate_app }}.

## Agent blueprint examples
Here you can see the examples of two agent blueprints built with different frameworks:

- [Langchain Hello World AI Agent](https://github.com/valory-xyz/langchain_hello_world)

- [Eliza Memeooorr AI Agent](https://github.com/valory-xyz/agents-fun-eliza)
