## **Summary.** 

This guide contains guidelines for contributing to the development of Mechs, by [creating and publishing tools](#1-creating-and-publishing-a-tool) which can be then used by Mechs, [testing a Mech locally](#2-testing-mech-locally) by running the Mech with abstract funds and [deploying a Mech](#3-deploying-a-mech) into production. 

# 1. Creating and publishing a tool

## 1. 1. Creating a tool

**Requirements**: [Python](https://www.python.org/) >= 3.8; [Pip](https://pip.pypa.io/en/stable/installation/); [Pipenv](https://pipenv.pypa.io/en/latest/installation.html) >= 2001.x.xx ; [Docker Engine](https://docs.docker.com/engine/install/) ; [Docker Compose](https://docs.docker.com/compose/install/) 

In order to create a tool, the steps are as follows: 

1. Fork the repository https://github.com/valory-xyz/mech and clone the forked copy;
2. In the main folder, in terminal:
    ```
    pip install open-autonomy
    autonomy init --remote --ipfs --author <author_name> 
    autonomy packages sync
    ```
2. Create a folder "username" [replace with your username] in the folder “packages”, inside this create a folder "customs", and inside this folder create a folder whose name corresponds to the tool. This folder should contain the following files : `component.yaml`, `tool_name.py` and `__init__.py`. For the second file, replace `tool_name` by the name of the tool.
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
For the third file, copy and paste the following copyright text: 

```
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2021-2023 Valory AG
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------
```
3. In `component.yaml`, copy and paste the following template (or the content of the `component.yaml` of any other tool), and replace the following fields: name (name of the module), author (name of the author), entry_point (this points at the python file in which the executable function is), callable (points at the function which is called in the entry_point), description (simple description of the module). In fingerprint, replace tool_name.py by the chosen entry point file.
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

4. Create the code for the tool in the file `tool_name.py` (following the examples of tools found [here](https://github.com/valory-xyz/mech-predict/tree/main/packages), for instance https://github.com/valory-xyz/mech-predict/tree/main/packages/gnosis/customs/ofv_market_resolver); the only requirement is to implement the function specified in callable of the `component.yaml` file; a minimal file would be the following for the template in the previous step for instance: 
    ```
        def run(**kwargs):
            pass
    ```
	
    This function needs to return the result of using the tool.

## 1. 2. Publishing the tool

1. Create the package hash, by running the following commands, from the root:

    ```
    autonomy packages lock
    ```
At this point you will be prompted to choose "dev" or "third-part". Choose "dev".
2. Push the packages to IPFS: 
    ```
    autonomy push-all
    ```
3. Mint the tool [here](https://registry.olas.network/ethereum/components/mint) as a component on the Olas Registry; For this is needed: an address (EOA), and the hash of the meta-data file. It is possible to generate this hash by clicking on “Generate Hash & File” and providing the following information: name (name of the author); description (of the tool); version; package hash (this can be found in package.json in the packages folder, in the entry which corresponds to the created tool); NFT image URL (for instance on IPFS, supported domains are listed in the window); in order to push an image on IPFS, this [script](https://github.com/dvilelaf/tsunami/blob/main/scripts/ipfs_pin.py) can be used.

After this the tool can be deployed to be used by a [Mech](#2-testing-mech-locally). 


# 2. Testing Mech locally 

## 2. 1. Setup 

**Requirements**: [Python](https://www.python.org/) == 3.10; [Poetry](https://python-poetry.org/docs/) >= 1.4.0 ; [Docker Engine](https://docs.docker.com/engine/install/) ; [Docker Compose](https://docs.docker.com/compose/install/) 

1. Run the followings in the terminal: 
    ```
    docker pull valory/open-autonomy-tendermint:0.18.3
    docker pull valory/oar-mech:bafybeicg5ioivs2ryaim6uf3cws2ashc5ldxtrvxgbjbhv3y2ic63qx324
    ```

2. Clone the mech-quickstart repository:

    ```
    git clone https://github.com/valory-xyz/mech-quickstart.git
    ```

3. Rename the file `.api_keys.json.example` into `.api_keys.json` (don't change the dummy keys). 
4. Create a tenderly virtual testnet, following these steps: 
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
5. Change folder to mech-quickstart and create environment (in terminal): 
    ```
    cd mech-quickstart
    poetry shell
    poetry install
    ```

## 2. 2. Running the Mech

1. Run the mech service (in terminal):

```
bash run_service.sh
```

2. Provide information when prompted (in particular for the RPC endpoint, provide the https address copied earlier).
3. When prompted to do so, add funds to the required address. In order to do so, click on “Fund account” on the webpage of the virtual testnet created before, enter the address to fund, the quantity and the token. For a custom token, click on “Use custom token address” and enter the token address. Then click on “Fund”.
4. Logs are visible with: 
```
docker logs mech_abci_0 --follow
```

The activity of the Mech is visible on the virtual testnet.

5. Stop the mech service: 

```
./stop_service.sh
```

# 3. Deploying a Mech

## 3. 1. Setup 

**Requirements**: [Python](https://www.python.org/) == 3.10; [Poetry](https://python-poetry.org/docs/) >= 1.4.0 ; [Docker Engine](https://docs.docker.com/engine/install/) ; [Docker Compose](https://docs.docker.com/compose/install/) 

1. Run the followings in the terminal: 

```
docker pull valory/open-autonomy-tendermint:0.18.3
docker pull valory/oar-mech:bafybeicg5ioivs2ryaim6uf3cws2ashc5ldxtrvxgbjbhv3y2ic63qx324
```
2. Create an EOA (add xDAI amounts on this account whenever requested). 
3. Create a RPC endpoint, for instance using https://www.nodies.app/. The steps are the following ones: 
    - Create an account; 
    - Create a project; 
    - Add an app to this project (choose the Gnosis chain); 
    - Copy the HTTPS link (under “Endpoint networks”) → this will be requested later; 
5. Create a Google API Key and an OpenAI API key. 
6. Clone the mech-quickstart repository:

```
git clone git@github.com:valory-xyz/mech-quickstart.git
```

7. Rename the file `.api_keys.json.example` into `.api_keys.json` and add OpenAI and Google API keys in the file. 
8. Change folder to mech-quickstart and create environment (in terminal): 

```
cd mech-quickstart
poetry shell
poetry install
```

## 3.2. Running the mech service

1. Run the mech service (in terminal):

```
bash run_service.sh
```

2. Provide information when prompted (in particular for the RPC endpoint, provide the https address copied earlier) and send funds to the prompted address.
3. Logs are visible with: 

```
docker logs mech_abci_0 --follow
```

4. Stop the mech service: 

```
./stop_service.sh
```
