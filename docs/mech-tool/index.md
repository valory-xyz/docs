## **Mechs**

Mechs are Olas agents that provide on-chain services to other agents in exchange for small payments.
They allow agents to access a wide range of tools—such as LLM subscriptions or prediction services—without the need to implement ad-hoc integrations.
All interactions with Mechs happen through a common API using on-chain requests and responses, enabling agents to access multiple tools via a unified interface.

You can think of Mechs as subscription-free tool libraries with a standard interface. Each Mech can offer multiple services, each of which is called a tool.
Anyone can create and deploy their own Mechs and register them in the Olas Registry. Once registered, a Mech contract can be created via the Mech Marketplace.


## **The Mech Marketplace**

The Mech Marketplace is a collection of smart contracts that facilitate seamless, on-chain interactions between requesters (agents or applications) and Mech agents providing task-based services.
It acts as a relay, ensuring secure payments and efficient task execution.
Specifically, the Mech Marketplace enables:

- **Effortless Mech Deployment**
Any agent registered in the Olas Service Registry can deploy a Mech contract with minimal inputs, allowing rapid service offering and on-chain payment collection.

- **Seamless Task Requests**
Requesters can submit service requests directly through the Mech Marketplace. On-chain contracts handle payments and service delivery transparently between requesters and Mechs.

- **Guaranteed Task Completion**
If a designated Mech fails to respond within the requester’s specified deadline, a take-over mechanism allows other available Mechs to complete the task, ensuring high reliability and fulfillment rates.

- **Karma Reputation System**
Each Mech’s performance is tracked via the Karma contract, which maintains a reputation score based on successful task completions and failures. High Karma scores signal trustworthiness to requesters under honest participation assumptions.

- **A Competitive Environment**
Mechs are incentivized to complete tasks promptly and reliably to maintain high Karma scores, improving their chances of receiving more tasks over time.

Through Mechs and the Mech Marketplace, agents in the Olas ecosystem gain modular, on-chain access to advanced tooling without managing subscriptions or complex integrations, supporting scalable and decentralized agent economies.


## Payment models

When creating a Mech, deployers can select between the following payment models:

- **Native**: a fixed-price model where the requester pays using the chain with native token for each delivered service.

- **Token**: similar to the Native model, but payments are made using a specified ERC20 token.

- **Nevermined subscription native**: a dynamic pricing model that allows flexible pricing across different services with native token.

- **Nevermined subscription token**: a dynamic pricing model that allows flexible pricing across different services using a specified ERC20 token.


## How the request-response flow works

Here's a simplified version of the mech request-response:

![Mech flow](imgs/mech.png)

1. Write request data: the requester writes the request data to IPFS. The request data must contain the attributes `nonce`, `tool`, and `prompt`. Additional attributes can be passed depending on the specific tool:

    ```json
    {
      "nonce": 15,
      "tool": "prediction_request",
      "prompt": "Will my favourite football team win this week's match?"
    }
    ```

2. The application gets the request data IPFS hash from the IPFS node.

3. The application writes the request's IPFS hash to the Mech Marketplace contract, including a small payment. Alternatively, the payment could be done separately through a Nevermined subscription.

4. The Mech service is constantly monitoring request events, and therefore gets the request hash.

5. The Mech reads the request data from IPFS using its hash.

6. The Mech selects the appropriate tool to handle the request from the `tool` entry in the metadata, and runs the tool with the given arguments, usually a prompt.

7. The Mech gets a response from the tool.

8. The Mech writes the response to IPFS.

9. The Mech receives the response IPFS hash.

10. The Mech writes the response hash to the Mech Marketplace contract.

11. The requester monitors for response events and reads the response hash from the associated transaction.

12. The application gets the response metadata from IPFS:

    ```json
    {
      "requestId": 68039248068127180134548324138158983719531519331279563637951550269130775,
      "result": "{\"p_yes\": 0.35, \"p_no\": 0.65, \"confidence\": 0.85, \"info_utility\": 0.75}"
    }
    ```

See some examples of requests and responses on the [Mech Hub](https://mech.olas.network/gnosis/mech/0x77af31de935740567cf4ff1986d04b2c964a786a?legacy=true).



## Mech Hello World: running a Mech with a dummy tool

In this example, we will locally run a Mech with a dummy "echo" tool.


1. First, clone the following repository:
    ```bash
    git clone git@github.com:valory-xyz/mech-tools-dev.git
    cd mech-tools-dev/
    ```

2. Prepare the virtual environment and install all the Python dependencies:
    ```bash
    poetry shell
    poetry install
    ```

3. Download all the mech packages from IPFS:
    ```bash
    autonomy packages sync --update-packages
    ```

4. Run the `setup.py` script:
    ```bash
    python utils/setup.py
    ```

    You will be prompted to fill in some details, including a Gnosis Chain RPC. Here, you can get one from a provider like [Quiknode](https://www.quicknode.com/) but we encourage you to first test against a virtual network using [Tenderly](https://tenderly.co/). This way, you can also use the faucet to fund the required wallets.

5. Push the tool metadata to IPFS:
    ```bash
    python utils/update_metadata.py
    ```

6. And just run your agent:
    ```bash
    ./run_agent.sh
    ```
    This option is recommended to quickly test or debug agents, so it's the one we recommend the first time you run this tutorial.
    The next time you use this command, it will ask you for your sudo password to remove the previous build.

7. Alternatively, you can also run the full dockerized service with:
    ```bash
    ./run_service.sh
    ```

    You can check your Mech's logs with:
    ```bash
    docker logs -f mechw_Me_abci_0
    ```

    Replace the Mech name with the one that appears after the `run_service.sh` script has finished.
    This option is recommended when your service is ready to be deployed.

8. Once your agent is running, and from another terminal (within the same virtual environment), send a request to it. First, let's export the required RPCs for the mechx library to read and write to the chain.
    You can reuse the RPC you provided during the setup plus you will need a WSS RPC. If you are using Tenderly, as recommended, you can get both of them from the Explorer section.

    ```bash
    export MECHX_RPC_URL=<your_http_rpc>
    export MECHX_LEDGER_ADDRESS=<your_http_rpc>
    export MECHX_WSS_ENDPOINT=<your_wss_rpc>
    ```

    Now, get your mech address from the `.env` file. You will see the following variable containing it:
     ```bash
    MECH_TO_CONFIG='{"<your_mech_address>":{"use_dynamic_pricing":false,"is_marketplace_mech":true}}'
    ```

    Finally, send the request (replacing your mech address):

    ```bash
    poetry run mechx interact --prompts "hello, mech!" --priority-mech <your_mech_address> --tools echo --chain-config gnosis
    ```

    The echo tool will respond with the same text from the request. You will see something like:
    ```bash
    Fetching Mech Info...
    Sending Mech Marketplace request...
    - Prompt uploaded: https://gateway.autonolas.tech/ipfs/f01701220fe7480a472cc8dffe481d5883e235346793a20a25415160ad2feade0d809f9db
    - Transaction sent: https://gnosisscan.io/tx/0x7bb3b734b5936e72c84749431081c8416c3f4c64a75f9f6c61291b47f141fd3d
    - Waiting for transaction receipt...
    - Created on-chain request with ID 63113231565093422774445497789782682647110838977840831205387629469951062204223
    ```

    In your agent logs, you will see something like:
    ```bash
    [2025-07-24 16:41:58,679][INFO] [agent] Task result for request 63113231565093422774445497789782682647110838977840831205387629469951062204223: ('Echo: hello, mech!', 'hello, mech!', None, None)
    ```
    Which means that the Mech has successfully received the request and ran the tool. After some time (give it a minute or so) you will see the response in the terminal you sent the request from:

    ```bash
    Off chain to be implemented
    - Data arrived: https://gateway.autonolas.tech/ipfs/f0170122068f1ed6661ac9c7f067c998d12ccf0bd29367c4373f4d91bf61ed98a068e3528
    - Data from agent:
    {
    "requestId": 28039871184902372191260032967003278816287653243679554051485992027223235273470,
    "result": "Echo: hello, mech!",
    "prompt": "hello, mech!",
    "cost_dict": {},
    "metadata": {
        "model": null,
        "tool": "echo",
        "params": {}
    },
    "is_offchain": false
    }
    ```

## Creating and publishing a tool

In order to contribute to Mechs' abilities, one can create and publish a tool. In order to do so, follow the instructions below.

### 1. Creating a tool

**Requirements**:
  - [Python](https://www.python.org/) `>=3.10`
  - [Poetry](https://python-poetry.org/docs/) `>=1.4.0 && <2.x`

In order to create a tool, the steps are as follows:

1. Ensure you have followed the instructions from the previous section to setup the `mech-tools-dev` repository.


2. Create the tool's structure by using the following command, after replacing the values for the `AUTHOR_NAME` and `TOOL_NAME` variables:

```bash
mtd add-tool -d AUTHOR_NAME TOOL_NAME
```

You will be asked whether this is a dev or a third-party package. Select dev package.
After the command finishes, it will generate the following structure, with template code:

```
packages/
 ├── author_name/
 │   ├── customs/
 │   │   ├── tool_name/
 │   │   │   ├── component.yaml
 │   │   │   ├── tool_name.py
 │   │   │   ├── __init__.py
```

For more options, use the tool helper:
```bash
mtd --help
```

3. Now that your tool's structure is set up, all that's left is to configure the tool component and implement the tool's functionality in Python.
The [component.yaml](https://github.com/valory-xyz/mech-tools-dev/blob/main/mtd/templates/config.template) file contains the tool's configuration and looks as follows:

    Here is an explanation of its fields:
    - `name`: the name of the tool.
    - `author`: the author's name.
    - `version`: the version of the tool.
    - `type`: the component type of the `open-autonomy` framework. This should be `custom`.
    - `description`: the description of the tool.
    - `license`: the licencing of the tool. It should be Apache-2.0.
    - `aea_version`: the supported `open-aea` version.
    - `fingerprint`: unique hash of the tool. This is auto-generated by the framework's `autonomy packages lock` command.
    - `fingerprint_ignore_patterns`: ignore patterns for the fingerprint's generation.
    - `entry_point`: the module which contains the tool's implementation.
    - `callable`: points to the function which is called in the tool's module.
    - `dependencies`: the module's dependencies. You may specify them in the following format:

    ```
    dependencies:
        dependency_1:
            version: ==0.5.3
        dependency_2:
            version: '>=2.20.0'
    ```

    The main function in your tool (the one referenced in the callable field in  `component.yaml`) should follow the following signature:

    ```python
    def run(**kwargs) -> Tuple[Optional[str], Optional[Dict[str, Any]], Any, Any]:
    ```

    Where the first return value is the tool response and the second one is the request. As reference, you could do the following at the end of the tool execution:

    ```python
    return response, prompt, None, None, None
    ```

### 2. Publishing the tool

1. Before proceeding, make sure that you are inside the poetry environment:
    ```bash
    poetry shell
    ```

2. Update the package hash, by running the following commands, from the root:

    ```bash
    autonomy packages lock
    ```

3. Push the packages to IPFS:

    ```bash
    autonomy push-all
    ```

4.  Mint the tool [here](https://registry.olas.network/ethereum/components/mint) as a component on the Olas Registry;
    For this is needed: an address (EOA) and the hash of the meta-data file.
    In order to generate this hash, click on “Generate Hash & File” and provide the following information:
    - name (name of the tool)
    - description (of the tool)
    - version (this needs to match the version in the file `component.yaml`)
    - package hash (this can be found in `packages.json` under the `packages` folder)
    - Optionally, NFT image URL. You can push an image to IPFS and use the corresponding hash.

    In order to push an image on IPFS, use the [mech-client](https://github.com/valory-xyz/mech-client.git) cli tool, replacing `<file_name>` with the name of your file:

        ```bash
        mechx push-to-ipfs ./<file_name>
        ```

After this, the tool can be deployed to be used by a Mech as shown in steps outlined below.


## Deploying a Mech with custom tools

In order to test a tool you developed, let's update the Mech you created in the previous sections.


1. Create the `metadata.json` for your mech:
    ```bash
    python utils/generate_metadata.py
    ```

2. Upload the `metadata.json` to IPFS:
    ```bash
    python utils/publish_metadata.py
    ```

3. Copy your tool hash from `packages/packages.json` and add it to the `TOOLS_TO_PACKAGE_HASH` variable, both in your `.env` and `config/config_mech_gnosis.json`.
   This variable is a dictionary, so you need to add a new entry with your tool name as key and the tool hash as value.


4. Run your mech using `run_agent.sh` or `run_service.sh` as seen in the previous sections.


## Sending a request to your custom Mech

1. Copy your Mech's address from the `.env` file. There should be a variable called `MECH_TO_CONFIG` that includes it.

2. Send the request similarly to how you did it in the first section:
    ```bash
    source .env
    poetry run mechx interact --prompts <your_prompt> --priority-mech <your_mech_address> --tools <your_tool_name> --chain-config gnosis
    ```

3. Wait for some time and you will receive the response. If there's an error in the tool, you will see it in the Mech's logs.


## How to accrue the payments

In order to accrue the payments of your Mech, find [here](https://github.com/valory-xyz/ai-registry-mech/blob/v0.4.0/docs/configuration.json) the BalanceTracker contract which corresponds to the payment model of your Mech. The key is the following for each of the three payment models:

- Native: BalanceTrackerFixedPriceNative

- Token: BalanceTrackerFixedPriceToken

- Nevermined native: BalanceTrackerNvmSubscriptionNative

- Nevermined token: BalanceTrackerNvmSubscriptionToken

Enter its address in the scan of the chosen network (i.e. [GnosisScan](https://gnosisscan.io/)). Click on "Contract" and then "Write Contract" and trigger the function processPaymentByMultisig. Enter the address of your Mech and click on "Write". This will transfer the funds stored in the Mech Marketplace to the address of your Mech contract.


## Troubleshooting

1. **Issue**: `0xa25d624C49eE3691a2B25223e3a899c77738FDa3` not in list of participants: "[`0xc062E6cfdCb48700de374905BF66A0BAD1Ef36E7`]"
**Solution**: Make sure the private keys inside keys.json match the address in ALL_PARTICIPANTS env

2. **Issue**: Exception raised while executing task: No module named 'anthropic'
**Solution**: Make sure the deps are listed in tool/component.yaml and aea-config.yaml and are pinned

3. **Issue**: Tool changes not being reflected <br>
**Solution**: Update the tool hash if there are any changes inside the tools or configs. To update run autonomy packages lock and update the tool hash (if needed) inside TOOLS_TO_PACKAGE_HASH

4. **Issue**: env formatting issues <br>
**Solution**: Make sure there are no whitespaces in dicts and lists and are represented as a string. So example this is the correct format. Also pay attention to utf coding of the " in str fields.
    ```
    MECH_TO_CONFIG='{"0xbead38e4C4777341bB3FD44e8cd4D1ba1a7Ad9D7":{"use_dynamic_pricing":false,"is_marketplace_mech":true}}'
    ```
    ⚠️ It is possible sometimes for the env to contain \\u201c or \\u201d. This means it is using a quotation mark character that is not accepted, replace the quotation mark character " for a compatible one.

5. **Issue**: ValueError: {'code': -32603, 'message': 'Filter with id: 1950087 does not exist.'}. Error when requesting transaction digest: {'code': -32010, 'message': 'AlreadyKnown'} <br>
**Solution**: Please check RPC is correct or change to a different provider

6. **Issue**: Service `\'\'api_key\'\'` not found in KeyChain. <br>
**Solution**: Make sure to add proper key names inside API_KEYS env

7. **Issue**: Error: Number of agents cannot be greater than available keys.
**Solution**: It's possible the code editor is formatting env files so double check the format of the keys and values.
So for example, for 1 agent system

    ```txt
    Wrong:
    ETHEREUM_LEDGER_RPC_0 = (
        "https://rpc.gnosischain.com/"
    )

    Right: ETHEREUM_LEDGER_RPC_0="https://rpc.gnosischain.com/"
    ```

8. **Issue**: Client.__init__() got an unexpected keyword argument 'proxies'"
**Solution**: Try to pin httpx to 0.25.2 inside tool's component.yaml and aea-config.yaml

9. **Issue**: Tool  <tool_name>  is not supported. <br>
**Solution**: Make sure the tool_name is inside the ALLOWED_TOOLS inside the tool.py

10. **Issue**: Incompatible counter_callback. <br>
**Solution**: If your tool is going to use the counter_callback function available at the run template and your tool is using a model that is not in [this](https://github.com/valory-xyz/mech/blob/main/packages/valory/skills/task_execution/utils/benchmarks.py#L31) list, please contact the mech developers for your model to be included, otherwise do not use the counter_callback function

11. **Issue**: Port already in use. <br>
**Solution**: When running locally the mech agent if you face an error of the type
`ERROR: failed to start node: failed to listen on 127.0.0.1:26658: listen tcp 127.0.0.1:26658: bind: address already in use` <br>
Then check at the CLI which process is using the port:
    ```bash
    $ lsof -i :26658
    ```
    and kill the process with:
    ```bash
    $ kill -9 process_id
    ```