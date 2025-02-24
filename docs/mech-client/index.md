## **Overview** 


This guide contains practical guidelines for interacting with Mechs.
The requester - whether it is an agent or an application - can choose between two methods for sending service requests: 

- On-chain, meaning that the request is sent to the Mech contract (relayed by the Mech Marketplace for the Mechs which are registered there); 

- Off-chain: the request is sent directly to the Mech service while delivery is sent by the Mech service to the Mech contract (and then relayed by Mech Marketplace contract for Mechs which are registered there); 

In order to send a request, the workflow is the following: 

**1.** Choose a Mech; 

**2.** Make an on-chain deposit according to the Mech’s [payment model](../mech-tool/index.md#overview).

**3.** Choose a method for sending the request;

**4.** Send the request.
		
The detailed instructions to send a request to a Mech can be found below.

## 1. How to Send a request to a Mech (registered on the Mech MarketPlace)

### 1. 1. Setup

**Requirements**: [Python](https://www.python.org/) >= 3.10, [Poetry](https://github.com/python-poetry/poetry) == 1.8.4

**1.** Install the [Mech client](https://github.com/valory-xyz/mech-client): 
    
- *(Option 1)* Using [Poetry](https://github.com/python-poetry/poetry): 
```
poetry new my_project
cd my_project
poetry shell
poetry add mech-client
```

- *(Option 2)* On local python installation: 

```
pip install mech-client
```

**2.** Setting up an EOA account: 

- *Option 1* (manual creation):

    **a.** Install browser extension of Metamask and open it; 
        
    **b.** Click on the account icon, then on “Add account or hardware wallet”, then “Add a new Ethereum account”, provide a name for the account and then click on “Add account”; 
        
    **c.** Select the newly created account and then click on the top-right menu icon and then “Account details”. You can find the private key by clicking “Show private key”. 
        
    **d.** Copy this key in the file `ethereum_private_key.txt` in your project folder (do not include any leading or trailing spaces, tabs or newlines or any other character); 
    
- *Option 2* (using [open-autonomy](https://github.com/valory-xyz/open-autonomy)): 
        
    **a.** Use the following to generate a private key: 
    ```
    autonomy generate-key ethereum -n 1
    ```
    
    This creates a file keys.json in which the private key can be found on the key “private_key”. 
        
    **b.** Copy this key in the file `ethereum_private_key.txt`.


### 1. 3. Sending requests

#### 1. 3. 1. In terminal

**1.** Send a request: 
    
- Use the command mechx in terminal, which is structured as follows: 
        
```
mechx interact <prompt> --chain-config <chain-config>
```

Replace `<prompt>` by a string which corresponds to the request to send to the Mech, and `<chain-config>` by one of the keys in the dictionary found in the file `.mech_client/configs/mechs.json` (for instance "gnosis"). In the dictionary corresponding to this key, replace the value of `priority_mech_address` with the address of the mech you want to send the request to. 

- If prompted, add funds to EOA account created above in order to be able to deposit on-chain to account for the mech fees. Specifically, add
     - native network token, e.g. xDAI for Gnosis, whether the Mech uses native fixed price
     - OLAS token on the network, whether the Mech uses Olas token fixed price
     - Nevermined plan related to the network, whether the Mech uses Nevermined subscription.
     
      
       It will be indicated how much is needed. You can also find 
the price per request (resp. the maximal price per Mechs with Nevermined subscription) per request as follows. 
Enter the address of the Mech in the scan of the network. Click on "Contract", then "Read contract" and find and click on "maxDeliveryRate" in the list which appears below. Divide the displayed number by 10^8 in order to obtain the price per request.

- It is possible (and optional) to specify which tool should be used by the mech. The command line is then:  

```
mechx interact <prompt> --tool <tool> --chain-config <chain-config>
```

In this case, replace `<tool>` by the name of the tool. 

- If prompted to make a an on-chain deposit to pay for Mech fees, use the following: 

```
python ./scripts/deposit_payment_model.py
```

where `payment_model` is replaced with "native" or "token" depending on the payment model of the Mech. You will be prompted to choose a network. Enter the name of the network which corresponds to the one of the Mech (without single quotes). When prompted enter the amount to deposit. This should be larger than the price of the Mech. This price corresponds to the variable MaxDeliveryRate.

**2.** Receive the response: 

- In response to the request, a json file is printed below "Data for agent", in which the key ‘result’ corresponds to the mech’s response to the request. For instance, with the command  

```
mechx interact "write a short poem" --tool openai-gpt-3.5-turbo --chain-config gnosis
``` 

you should receive a response as follows: 
        ![screenshot_response](./imgs/screenshot_request.png)

- Remark: If an "Out of gas" error is encountered, an increase of the gas limit, can solve the problem, using the following line: 

```
export MECHX_GAS_LIMIT=200000
```

#### 1. 3. 2. Script for automatizing request sending

The following script can be used in order to automatize request sending:

```
from mech_client.interact import interact

PROMPT_TEXT = 'Will Gnosis pay reach 100k cards in 2024?'
TOOL_NAME = "prediction-online"

result = interact(
    prompt=PROMPT_TEXT,
    tool=TOOL_NAME,
    chain-config=CHAIN_CONFIG
)
```

The variables **PROMPT_TEXT**, **CHAIN_CONFIG** and **TOOL_NAME** can be changed. The variable **result** contains the response of the mech. 

## 2. Sending requests to legacy Mechs

It is also possible to send requests to Mechs which were deployed before the Mech Marketplace (we call these _legacy Mechs_). 
This section describes how to do this (note that in this case, you will benefit from Mech Marketplace feature, and in particular not have the guarantee that your request will be answered, or of the quality of the answer).

Follow first the steps in the [setup](#1-1-setup) above.

### 2. 1. Choosing a Mech

- A list of deployed Mechs can be found [here](https://github.com/valory-xyz/mech?tab=readme-ov-file#examples-of-deployed-mechs). Choose the chain and the Mech (column "Mech Instance (Fixed Pricing)"), and note its id;  

- Add funds corresponding to the network of the Mech (column “Network” of the table) in the EOA account created above, in order to pay the mech for requests. The price per request can be found as follows. Find the contract of the Mech. For instance, [here](https://gnosisscan.io/address/0x77af31De935740567Cf4fF1986D04B2c964A786a#readContract) is the contract for a Mech on Gnosis chain. Click on "Contract", then "Read contract" and find and click on "price" in the list which appears below. Divide the displayed number by 10^8 in order to obtain the price per request (here 0.01 xDAI).

### 2. 2. In terminal

**1.** Send a request: 
    
- Use the command mechx in terminal, which is structured as follows: 
        
```
mechx interact <prompt> --agent_id <agent_id>
```

Replace `<agent_id>` with the following: the number (as an integer, not string) after the character “-” in the column “Mech Instance (Fixed Pricing) - Agent Id” of the table [here](https://github.com/valory-xyz/mech?tab=readme-ov-file#examples-of-deployed-mechs) for the chosen mech; Replace `<prompt>` by a string which corresponds to the request to send to the Mech. 

- The list of ids and the names of the tools that the Mech can use will appear. You will be prompted to enter the id of a tool that the Mech will use to respond to the request.

- In order to select a tool, you can use the following to see which tools are used by which agents: 

```
mechx tools-for-agents
```

You can identify which tools are used by a Mech by looking at the "Agent ID" column. Using the unique identifier of the tool, you can find a description of the tool, using the following: 

```
mechx tool-description <unique_identifier> --chain-config <chain_config>
```

where `<unique_identifier>` is replaced by the unique id of the tool and `<chain_config>` by the name of the network.

**2.** Receive the response: 

- In response to the request, a json file is printed below "Data for agent", in which the key ‘result’ corresponds to the mech’s response to the request. For instance, with the command  

```
mechx interact "write a short poem" --agent_id 6
``` 

and after selecting `openai-gpt-3.5-turbo` for the tool, you will receive a response as follows: 
        ![screenshot_response](./imgs/screenshot_request.png)

- Remark: If an "Out of gas" error is encountered, an increase of the gas limit, can solve the problem, using the following line: 

```
export MECHX_GAS_LIMIT=200000
```

### 2. 3. Script for automatizing request sending

The following script can be used in order to automatize request sending:

```
from mech_client.interact import interact

PROMPT_TEXT = 'Will Gnosis pay reach 100k cards in 2024?'
AGENT_ID = 6
TOOL_NAME = "prediction-online"

result = interact(
    prompt=PROMPT_TEXT,
    agent_id=AGENT_ID,
    tool=TOOL_NAME
)
```

The variables **PROMPT_TEXT**, **AGENT_ID** and **TOOL_NAME** can be changed. The variable **result** contains the response of the mech. 

### 2. 4. Sending requests through the web interface

**1.** Create a wallet (for instance with [Metamask](https://metamask.io/)) and connect it to the web interface by clicking on the button “Connect wallet” on the webpage. This wallet must be provided with xDAI in order to pay the Mechs for the requests.

**2.** Go to the webpage [here](https://aimechs.autonolas.network/mech/0x77af31De935740567Cf4fF1986D04B2c964A786a).

**3.** Click on "New Request". The following pop-up will appear: 
![screenshot](./imgs/screenshot.png)

**4.** Enter a prompt and select the tool, then click on "Request". 

**5.** A window like the one as follows will appear: 
![confirmation](./imgs/confirmation.png)
Click on "Confirm".

**6.** You can find the request by searching for your wallet's address in the column "Sender". When the request is delivered, you can access the delivered data in the column "Delivers data" in the corresponding row.