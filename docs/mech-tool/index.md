## **Summary** 

This guide contains guidelines for contributing to the development of Mechs, by [creating and publishing tools](#1-creating-and-publishing-a-tool) which can be then used by Mechs, [testing a Mech locally](#2-testing-mech-locally) by running the Mech with abstract funds and [deploying a Mech](#4-deploying-a-mech) into production. 

## 1. Creating and publishing a tool

### 1. 1. Creating a tool

**Requirements**: [Python](https://www.python.org/) >= 3.8; [Pip](https://pip.pypa.io/en/stable/installation/); [Pipenv](https://pipenv.pypa.io/en/latest/installation.html) >= 2001.x.xx ; [Docker Engine](https://docs.docker.com/engine/install/) ; [Docker Compose](https://docs.docker.com/compose/install/) 

In order to create a tool, the steps are as follows: 

**1.** Fork the repository https://github.com/valory-xyz/mech and clone the forked copy;

**2.** In the main folder, in terminal:

```
pip install open-autonomy
autonomy init --remote --ipfs --author <author_name> 
autonomy packages sync
```

**3.** Create a folder "username" [replace with your username] in the folder “packages”, inside this create a folder "customs", and inside this folder create a folder whose name corresponds to the tool. This folder should contain the following files : `component.yaml`, `tool_name.py` and `__init__.py`. For the second file, replace `tool_name` by the name of the tool.

```
cd packages
mkdir <username>
cd <username>
mkdir customs 
cd customs
mkdir <tool_name> 
cd <tool_name>
touch component.yaml
touch tool_name.py
touch __init__.py
```

For the third file, copy and paste the following copyright text found for instance [here](https://github.com/KahanMajmudar/mech/blob/main/packages/valory/connections/__init__.py). 

**4.** In `component.yaml`, copy and paste the following template (or the content of the `component.yaml` of any other tool), and replace the following fields: name (name of the module), author (name of the author), entry_point (this points at the python file in which the executable function is), callable (points at the function which is called in the entry_point), description (simple description of the module). In fingerprint, replace tool_name.py by the chosen entry point file.

```
name: tool_name
author: author_name
version: 0.1.0
type: custom
description: Tool description
license: Apache-2.0
aea_version: '>=1.0.0, <2.0.0'
fingerprint:
    __init__.py:
    tool_name.py:
fingerprint_ignore_patterns: []
entry_point: tool_name.py
callable: run
dependencies: {}
```

If the module has any dependencies, remove `{}` and add them in the following format: 

```
dependencies: 
    dependency_1:
        version: ==0.5.3
    dependency_2:
        version: '>=2.20.0'
```

**5.** Create the code for the tool in the file `tool_name.py` (following the examples of tools found [here](https://github.com/valory-xyz/mech-predict/tree/main/packages), for instance https://github.com/valory-xyz/mech-predict/tree/main/packages/gnosis/customs/ofv_market_resolver); the only requirement is to implement the function specified in callable of the `component.yaml` file; a minimal file would be the following for the template in the previous step for instance: 

```
def run(**kwargs):
    pass
```
	
This function needs to return the result of using the tool.

### 1. 2. Publishing the tool

**1.** Create the package hash, by running the following commands, from the root:

```
autonomy packages lock
```

At this point you will be prompted to choose "dev" or "third-part". Choose "dev".

**2.** Push the packages to IPFS: 

```
autonomy push-all
```

**3.** Mint the tool [here](https://registry.olas.network/ethereum/components/mint) as a component on the Olas Registry; For this is 
needed: an address (EOA), and the hash of the meta-data file. In order to generate this hash, click on “Generate Hash & File” and providing the following information: name (name of the tool); description (of the tool); version (this is found in the file `component.yaml`); package hash (this can be found in package.json in the packages folder, in the entry which corresponds to the created tool); NFT image URL (for instance on IPFS, supported domains are listed in the window); in order to push an image on IPFS, this [script](https://github.com/dvilelaf/tsunami/blob/main/scripts/ipfs_pin.py) can be used.

After this the tool can be deployed to be used by a [Mech](#2-testing-mech-locally). 


## 2. Testing Mech locally 

### 2. 1. Setup 

**Requirements**: [Python](https://www.python.org/) == `3.10`; [Poetry](https://python-poetry.org/docs/) >= `1.4.0` ; [Docker Engine](https://docs.docker.com/engine/install/) ; [Docker Compose](https://docs.docker.com/compose/install/) ; [Yarn](https://yarnpkg.com/) == `1.22.19` ; [Node](https://nodejs.org/en) == `20.18.1`; npx/npm == `10.8.2` ;

**1.** Run the followings in the terminal: 
```
docker pull valory/open-autonomy-tendermint:0.18.3
docker pull valory/oar-mech:bafybeicg5ioivs2ryaim6uf3cws2ashc5ldxtrvxgbjbhv3y2ic63qx324
```

**2.** Clone the mech-quickstart repository:

```
git clone https://github.com/valory-xyz/mech-quickstart.git
```

**3.** Rename the file `.api_keys.json.example` into `.api_keys.json` (don't change the dummy keys), and the file `.tools_to_packages_hash.json.example` into `.tools_to_packages_hash`. You can modify this example by adding your tool (name and hash).

**4.** Create a tenderly virtual testnet, following these steps: 

- Create an account/connect to Tenderly: https://dashboard.tenderly.co/. 

- Click on “Project” and then “Create project”, as on the following picture. 

      ![create_project](./imgs/screenshot_create_project.png "Create Project")

      Give a name to the project and click again on “Create project”. 
    
- Then click on "Virtual Test Nets" on the left menu (or on the following icon if the menu bar is collapsed): 
      ![testnet](./imgs/testnet.png "Testnet")
    
- Then click on “Create Virtual TestNet”.

- Choose “Gnosis chain” as the parent network, give a name to the virtual testnet and un-mark “Use latest block” in the State Sync section in order to enter the following custom block: 36619660.
    
- Finally, click on the “Create” button.

- After you are redirected to the TestNet "Explorer" page, copy the RPC Admin HTTPS link, it will be used later.

**5.** Setup the virtual testnet, by following these steps: 

- In a separate folder, clone the ai-registry-mech repository: 
        ```
        git clone https://github.com/KahanMajmudar/ai-registry-mech.git
        ```
- Run the following: 
        ```
        git submodule update --init --recursive
        ```
- Then change the branch to "testnet-setup".

- Crate an access token on Tenderly, by clicking on the profile icon (top-right), then on "Account settings", "Access tokens" in the left menu, then "Generate access token". Choose a label (it is only informative) and then click on "Generate". Copy the generated token.  

- Connect to tenderly in the terminal: 
        ```
        tenderly login --access-key <access_token>
        ```
where `<access_token>` has to be replaced with the access key created as before.

- In the file `hardhat.config.js`, change the url of `virtual_testnet` (line 47) to the RPC of the testnet created on tenderly. On lines 141 and 142, change "project" and "username" strings with the ones found on tenderly in the opened project. This can be found by clicking on "Project" on the tenderly dashboard, then selecting the opened project, and "Settings" on the right menu. The "project" corresponds to "Project slug" and "username" corresponds to "Account slug".

- In the file `globals.json`, change "networkURL" on line 6 to the RPC of the testnet and "privateKey" (line 7) to the private key of your wallet. 

- Install the dependencies using the following: 
    ```
    yarn install
    ```

- Fund the EOA address in tenderly (with the default amount). In order to do so, click on “Fund account” on the webpage of the virtual testnet created before, enter the address to fund, the quantity and the token. For a custom token, click on “Use custom token address” and enter the token address. Then click on “Fund”.

- Run the script to deploy the contracts which are necessary to test the Mech locally: 
```
bash setup-tdly.sh
``` 
- From the file `globals.json` in the ai-registry-mech folder, copy the following values and paste them in the corresponding lines of the `utils.py` file of the mech-quickstart folder: 

    **a.** "mechMarketplaceProxyAddress" -> line 490 ; 

    **b.** "mechFactoryFixedPriceNativeAddress" -> line 495 ; 

    **c.** "mechFactoryFixedPriceTokenAddress" -> line 500.

**6.** Change folder to the mech-quickstart one and then create environment (in terminal): 

```
poetry shell
poetry install
```

### 2. 2. Running the Mech

**1.** Run the mech service (in terminal):

```
bash run_service.sh
```

**2.** Provide information when prompted, in particular: 

- "Please enter a GNOSIS RPC URL" -> enter the RPC endpoint (https address copied earlier). 

- "Which type of mech do you want to deploy?" -> this corresponds to the payment model of the Mech (Native: native token ; Token: ERC20 tokens; Nevermined: subscription); default is Native. 

Other values can be left to default (by pressing enter when prompted).

**3.** When prompted to do so, add funds to the required address. 

**4.** Logs are visible with: 
```
docker logs mech_abci_0 --follow
```

The activity of the Mech is visible on the virtual testnet.

**5.** Stop the mech service: 

```
./stop_service.sh
```

### 2. 3. Sending a request

**1.** In another folder, clone the mech-client repository: 

```
git clone https://github.com/valory-xyz/mech-client.git
```

**2.** Install the mech-client package: 

```
pip install -e.
```

**3.** If the mech-client folder does not contain a file `ethereum_private_key.txt` already, create it and paste in it the private key of your EOA.

**4.** Add the following at the end of the dictionary in `mech_client/configs/mechs.json`: 

```
"tdly": {
    "agent_registry_contract": "0x9dEc6B62c197268242A768dc3b153AE7a2701396",
    "service_registry_contract": "0x9338b5153ae39bb89f50468e608ed9d764b755fd",
    "rpc_url": ,
    "wss_endpoint": "wss://gnosis-chiado-rpc.publicnode.com",
    "ledger_config": {
        "address": ,
        "chain_id": 10200,
        "poa_chain": false,
        "default_gas_price_strategy": "eip1559",
        "is_gas_estimation_enabled": false
    },
    "mech_marketplace_config": {
        "mech_marketplace_contract": "0x9efde57bcc6495c7f9a9844d31b8cd1f04100346",
        "priority_mech_service_id": 981,
        "response_timeout": 300,
        "payment_data": "0x"
    },
    "gas_limit": 500000,
    "price": 10000000000000000,
    "contract_abi_url": ,
    "transaction_url": ,
    "subgraph_url": ""
}
```


where the urls are as follows: 

![alt text](./imgs/url1.png)
![alt text](./imgs/url2.png)

Replace line 210 and line 213 with the RPC endpoint address, and line 220 with the mech marketplace address found in tenderly. 

**5.** Comment lines 560 to 566 in `mech_client/marketplace_interact.py`.

**6.** Run the following command in terminal in the mech-client repository: 

```
mechx interact <prompt> --tool <tool_name> --chain-config tdly
```

where `<prompt>` is replaced by the chosen prompt and `<tool_name>` by the name of your tool.

**7.** You can see the data of the request in the testnet page on tenderly, in the tab "Explorer".


## 4. Deploying a Mech with quickstart

### 4. 1. Setup 

**Requirements**: [Python](https://www.python.org/) == 3.10; [Poetry](https://python-poetry.org/docs/) >= 1.4.0 ; [Docker Engine](https://docs.docker.com/engine/install/) ; [Docker Compose](https://docs.docker.com/compose/install/) 

**1.** Run the followings in the terminal: 

```
docker pull valory/open-autonomy-tendermint:0.18.3
docker pull valory/oar-mech:bafybeicg5ioivs2ryaim6uf3cws2ashc5ldxtrvxgbjbhv3y2ic63qx324
```

**2.** Create an EOA (add xDAI amounts on this account whenever requested). 

**3.** Create a RPC endpoint, for instance using https://www.nodies.app/. The steps are the following ones: 

- Create an account; 

- Create a project; 

- Add an app to this project (choose the Gnosis chain); 

- Copy the HTTPS link (under “Endpoint networks”) → this will be requested later; 

**5.** Create a Google API Key and an OpenAI API key. 

**6.** Clone the mech-quickstart repository:

```
git clone https://github.com/valory-xyz/mech-quickstart.git
```

**7.** Rename the file `.api_keys.json.example` into `.api_keys.json` and add OpenAI and Google API keys in the file. Also rename the file `.tools_to_packages_hash.json.example` into `.tools_to_packages_hash`. You can modify this example by adding your tool (name and hash).

**8.** Change folder to mech-quickstart and create environment (in terminal): 

```
cd mech-quickstart
poetry shell
poetry install
```

### 4.2. Running the mech service

**1.** Run the mech service (in terminal):

```
bash run_service.sh
```

**2.** Provide information when prompted (in particular for the RPC endpoint, provide the https address copied earlier).

**3.** In order to send a request to it, follow the steps in the [section 2.3](#2-3-sending-a-request) above, replacing the RPC endpoint with the one created here. 

**4.** Logs are visible with: 

```
docker logs mech_abci_0 --follow
```

**5.** Stop the mech service: 

```
./stop_service.sh
```
