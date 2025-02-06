## **Summary** 

This guide contains practical guidelines for integrating Mechs to an application, by sending them requests, in [terminal](#1-how-to-send-a-request-to-a-mech-from-terminal), via a [python script](#2-script-for-automatizing-request-sending), via a [web interface](#3-sending-requests-through-the-web-interface), and receiving the responses to these requests.  

## 1. How to Send a request to a Mech from Terminal

### 1.1. Setup

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

**3.** Choose a Mech:

- The list of chains in which the Mechs are deployed on can be found [here](https://github.com/valory-xyz/mech?tab=readme-ov-file#examples-of-deployed-mechs). Choose the chain and the Mech (column "Mech Instance (Fixed Pricing)"), and note its id;  

- Add funds corresponding to the network of the Mech (column “Network” of the table) in the EOA account created above, in order to pay the mech for requests. The price per request can be found as follows. Find the contract of the Mech. For instance, [here](https://gnosisscan.io/address/0x77af31De935740567Cf4fF1986D04B2c964A786a#readContract) is the contract for a Mech on Gnosis chain. Click on "Contract", then "Read contract" and find and click on "price" in the list which appears below. Divide the displayed number by 10^8 in order to obtain the price per request (here 0.01 xDAI).

### 1.2. Sending requests

**1.** Send a request: 
    
- Use the command mechx in terminal, which is structured as follows: 
        
```
mechx interact <prompt> <agent_id>
```

Replace `<agent_id>` with the following: the number (as an integer, not string) after the character “-” in the column “Mech Instance (Fixed Pricing) - Agent Id” of the table [here](https://github.com/valory-xyz/mech?tab=readme-ov-file#examples-of-deployed-mechs) for the chosen mech; Replace `<prompt>` by a string which corresponds to the request to send to the Mech. 

- It is possible (and optional) to specify which tool should be used by the mech. The command line is then:  

```
mechx interact <prompt> <agent_id> --tool <tool>
```

In this case, replace `<tool>` by the name of the tool. 

- Tools available for the chosen agent can be found as follows (the tools names are listed in the column “Tool Name” in the output table):

```
mechx tools-for-agents --agent-id <agent_id>
```

- In order to select a tool, it is possible to find the description of a tool using the following, where `<unique_identifier>` is replaced by the tool’s identifier which can be found in the table obtained by the previous line.  

```
mechx tool-description <unique_identifier>
```

**2.** Receive the response: 

- In response to the request, a json file is printed below "Data for agent", in which the key ‘result’ corresponds to the mech’s response to the request. For instance, with the command  

```
mechx interact "write a short poem" 6 --tool openai-gpt-3.5-turbo
``` 

you should receive a response as follows: 
        ![screenshot_response](./imgs/screenshot_request.png)

- Remark: If an "Out of gas" error is encountered, an increase of the gas limit, can solve the problem, using the following line: 

```
export MECHX_GAS_LIMIT=200000
```

## 2. Script for automatizing request sending

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


## 3. Sending requests through the web interface

**1.** Create a wallet (for instance with [Metamask](https://metamask.io/)) and connect it to the web interface by clicking on the button “Connect wallet” on the webpage. This wallet must be provided with xDAI in order to pay the Mechs for the requests.

**2.** Go to the webpage [here](https://aimechs.autonolas.network/mech/0x77af31De935740567Cf4fF1986D04B2c964A786a).

**3.** Click on "New Request". The following pop-up will appear: 
![screenshot](./imgs/screenshot.png)

**4.** Enter a prompt and select the tool, then click on "Request". 

**5.** A window like the one as follows will appear: 
![confirmation](./imgs/confirmation.png)
Click on "Confirm".

**6.** You can find the request by searching for your wallet's address in the column "Sender". When the request is delivered, you can access the delivered data in the column "Delivers data" in the corresponding row.