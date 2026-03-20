# Valory-xyz Repository Dependency Graph

```mermaid
flowchart LR

    %% Nodes
    agent_scan["agent-scan"]
    agent_ui_monorepo["agent-ui-monorepo"]
    agents_mirror_db["agents-mirror-db"]
    autonolas_frontend_mono["autonolas-frontend-mono"]
    autonolas_governance["autonolas-governance"]
    autonolas_marketplace["autonolas-marketplace"]
    autonolas_registries["autonolas-registries"]
    autonolas_staking_programmes["autonolas-staking-programmes"]
    autonolas_subgraph["autonolas-subgraph"]
    autonolas_subgraph_studio["autonolas-subgraph-studio"]
    autonolas_tokenomics["autonolas-tokenomics"]
    autonolas_v1["autonolas-v1"]
    autonomy_packages_bumper["autonomy-packages-bumper"]
    brand_and_press_kit_agents_unleashed["brand-and-press-kit-agents-unleashed"]
    dev_template["dev-template"]
    docs["docs"]
    dynamic_contribution["dynamic-contribution"]
    funds_manager["funds-manager"]
    genai["genai"]
    governance_near["governance-near"]
    hello_world["hello-world"]
    IEKit["IEKit"]
    kv_store["kv-store"]
    langchain_hello_world["langchain_hello_world"]
    lockbox_governor_solana["lockbox-governor-solana"]
    lockbox_solana["lockbox-solana"]
    market_creator["market-creator"]
    mech["mech"]
    mech_agents_fun["mech-agents-fun"]
    mech_client["mech-client"]
    mech_interact["mech-interact"]
    mech_predict["mech-predict"]
    mech_server["mech-server"]
    meme_ooorr["meme-ooorr"]
    olas["olas"]
    olas_operate_app["olas-operate-app"]
    olas_operate_middleware["olas-operate-middleware"]
    olas_predict["olas-predict"]
    olas_sdk_starter["olas-sdk-starter"]
    olas_website["olas-website"]
    open_acn["open-acn"]
    open_aea["open-aea"]
    open_aea_cosmpy["open-aea-cosmpy"]
    open_aea_flashbots["open-aea-flashbots"]
    open_autonomy["open-autonomy"]
    open_autonomy_client["open-autonomy-client"]
    optimus["optimus"]
    pettai_agent["pettai-agent"]
    propel_client["propel-client"]
    quickstart["quickstart"]
    registries_near["registries-near"]
    registries_solana["registries-solana"]
    tomte["tomte"]
    trader["trader"]
    triton_bot["triton-bot"]
    valory_website["valory-website"]
    wormhole_sdk_vaa["wormhole-sdk-vaa"]
    x402["x402"]

    %% Click events
    click agent_scan "https://github.com/valory-xyz/agent-scan" "Find any agent on agentscan.org!" _blank
    click agent_ui_monorepo "https://github.com/valory-xyz/agent-ui-monorepo" "agent-ui-monorepo repository" _blank
    click agents_mirror_db "https://github.com/valory-xyz/agents-mirror-db" "agents-mirror-db repository" _blank
    click autonolas_frontend_mono "https://github.com/valory-xyz/autonolas-frontend-mono" "Mono repo for all olas.network apps" _blank
    click autonolas_governance "https://github.com/valory-xyz/autonolas-governance" "This repository contains the Autonolas OLAS token and the governance part of the autonolas-v1 protocol." _blank
    click autonolas_marketplace "https://github.com/valory-xyz/autonolas-marketplace" "Reference implementation of Olas' AI agent marketplace" _blank
    click autonolas_registries "https://github.com/valory-xyz/autonolas-registries" "This repository contains the registries for components, agents and services, the second part of the autonolas-v1 protocol." _blank
    click autonolas_staking_programmes "https://github.com/valory-xyz/autonolas-staking-programmes" "Autonolas Staking Programmes" _blank
    click autonolas_subgraph "https://github.com/valory-xyz/autonolas-subgraph" "autonolas-subgraph repository" _blank
    click autonolas_subgraph_studio "https://github.com/valory-xyz/autonolas-subgraph-studio" "Autonolas Subgraphs Monorepo" _blank
    click autonolas_tokenomics "https://github.com/valory-xyz/autonolas-tokenomics" "This repository contains the Autonolas tokenomics part of the autonolas-v1 protocol." _blank
    click autonolas_v1 "https://github.com/valory-xyz/autonolas-v1" "Autonolas on-chain protocol" _blank
    click autonomy_packages_bumper "https://github.com/valory-xyz/autonomy-packages-bumper" "Automation for packages dependencies upgrades downstream of open-aea and open autonomy" _blank
    click brand_and_press_kit_agents_unleashed "https://github.com/valory-xyz/brand-and-press-kit-agents-unleashed" "Press Kit summarizing Brand Guidelines (inc. logos) and Information about Agents Unleashed" _blank
    click dev_template "https://github.com/valory-xyz/dev-template" "A template for development with the open-autonomy framework." _blank
    click docs "https://github.com/valory-xyz/docs" "This repository aggregates the documentation of all the Olas ecosystem products." _blank
    click dynamic_contribution "https://github.com/valory-xyz/dynamic-contribution" "This repository contains the Autonolas dynamic contribution contracts." _blank
    click funds_manager "https://github.com/valory-xyz/funds-manager" "Open Autonomy library skill for funding mechanism" _blank
    click genai "https://github.com/valory-xyz/genai" "Open Autonomy library skill wrapping generative AI" _blank
    click governance_near "https://github.com/valory-xyz/governance-near" "governance-near repository" _blank
    click hello_world "https://github.com/valory-xyz/hello-world" "Example of an autonomous AI agent using the Open Autonomy framework" _blank
    click IEKit "https://github.com/valory-xyz/IEKit" "An autonomous service implementing a decentralized Impact Evaluator" _blank
    click kv_store "https://github.com/valory-xyz/kv-store" "Open Autonomy library skill wrapping an sqlite db" _blank
    click langchain_hello_world "https://github.com/valory-xyz/langchain_hello_world" "langchain_hello_world repository" _blank
    click lockbox_governor_solana "https://github.com/valory-xyz/lockbox-governor-solana" "Timelock governed OLAS and SOL Fee Collector on Solana" _blank
    click lockbox_solana "https://github.com/valory-xyz/lockbox-solana" "Set of lockbox contracts on Solana for Olas protocol." _blank
    click market_creator "https://github.com/valory-xyz/market-creator" "Market creator agent for AI prediction markets on Gnosis" _blank
    click mech "https://github.com/valory-xyz/mech" "Base mech" _blank
    click mech_agents_fun "https://github.com/valory-xyz/mech-agents-fun" "Mech serving agents.fun mech" _blank
    click mech_client "https://github.com/valory-xyz/mech-client" "Client to interact with Olas (Mech) Marketplace" _blank
    click mech_interact "https://github.com/valory-xyz/mech-interact" "Open Autonomy library skills to interact with Olas Marketplace" _blank
    click mech_predict "https://github.com/valory-xyz/mech-predict" "Mech serving Olas Predict" _blank
    click mech_server "https://github.com/valory-xyz/mech-server" "A CLI to create, deploy and manage Mechs — AI agents that execute tasks on-chain for payment — on the Olas Marketplace." _blank
    click meme_ooorr "https://github.com/valory-xyz/meme-ooorr" "An autonomous Olas agent that deploys meme coins." _blank
    click olas "https://github.com/valory-xyz/olas" "Server providing market statistics on OLAS" _blank
    click olas_operate_app "https://github.com/valory-xyz/olas-operate-app" "Pearl - Run agents, stake & earn rewards*" _blank
    click olas_operate_middleware "https://github.com/valory-xyz/olas-operate-middleware" "Olas Operate Middleware - Run agents, stake & earn rewards*" _blank
    click olas_predict "https://github.com/valory-xyz/olas-predict" "Olas Predict" _blank
    click olas_sdk_starter "https://github.com/valory-xyz/olas-sdk-starter" "olas-sdk-starter repository" _blank
    click olas_website "https://github.com/valory-xyz/olas-website" "The home of Olas" _blank
    click open_acn "https://github.com/valory-xyz/open-acn" "Open Agent Communication Network - Fork of acn on fetchai/agents-aea" _blank
    click open_aea "https://github.com/valory-xyz/open-aea" "A framework for open autonomous economic agent (AEA) development - no package vendor is prioritised over other package vendors" _blank
    click open_aea_cosmpy "https://github.com/valory-xyz/open-aea-cosmpy" "A Python client library for interacting with blockchains based on the Cosmos-SDK" _blank
    click open_aea_flashbots "https://github.com/valory-xyz/open-aea-flashbots" "Web3.py plugin for using Flashbots' bundle APIs" _blank
    click open_autonomy "https://github.com/valory-xyz/open-autonomy" "A framework for the creation of autonomous agent services." _blank
    click open_autonomy_client "https://github.com/valory-xyz/open-autonomy-client" "Autonomous Service Client SDK" _blank
    click optimus "https://github.com/valory-xyz/optimus" "BabyDegen agent" _blank
    click pettai_agent "https://github.com/valory-xyz/pettai-agent" "pettai-agent repository" _blank
    click propel_client "https://github.com/valory-xyz/propel-client" "Python client to interact with Valory's PaaS Propel" _blank
    click quickstart "https://github.com/valory-xyz/quickstart" "A quickstart for running agents on Olas" _blank
    click registries_near "https://github.com/valory-xyz/registries-near" "Autonolas registries contracts on Near" _blank
    click registries_solana "https://github.com/valory-xyz/registries-solana" "Set of Autonolas registries contracts on Solana" _blank
    click tomte "https://github.com/valory-xyz/tomte" "A library that wraps many useful tools (linters, analysers, etc) to keep Python code clean, secure, well-documented and optimised." _blank
    click trader "https://github.com/valory-xyz/trader" "AI agent for trading on prediction markets (specifically, Omen on Gnosis and Polymarket on Polygon)" _blank
    click triton_bot "https://github.com/valory-xyz/triton-bot" "A Telegram bot to handle staked Olas services" _blank
    click valory_website "https://github.com/valory-xyz/valory-website" "The home of Valory" _blank
    click wormhole_sdk_vaa "https://github.com/valory-xyz/wormhole-sdk-vaa" "Wormhole VAA management via SDK" _blank
    click x402 "https://github.com/valory-xyz/x402" "A payments protocol for the internet. Built on HTTP." _blank

    %% Dependencies
    autonolas_marketplace -->|<a href="https://github.com/valory-xyz/autonolas-marketplace/blob/main/.gitmodules#L1" target="_blank">Link</a>| autonolas_registries
    autonolas_staking_programmes -->|<a href="https://github.com/valory-xyz/autonolas-staking-programmes/blob/main/.gitmodules#L1" target="_blank">Link</a>| autonolas_registries
    autonolas_v1 -->|<a href="https://github.com/valory-xyz/autonolas-v1/blob/main/remappings.txt#L3" target="_blank">Link</a>| autonolas_governance
    autonolas_v1 -->|<a href="https://github.com/valory-xyz/autonolas-v1/blob/main/.gitmodules#L13" target="_blank">Link</a>| autonolas_marketplace
    autonolas_v1 -->|<a href="https://github.com/valory-xyz/autonolas-v1/blob/main/remappings.txt#L4" target="_blank">Link</a>| autonolas_registries
    autonolas_v1 -->|<a href="https://github.com/valory-xyz/autonolas-v1/blob/main/.gitmodules#L16" target="_blank">Link</a>| autonolas_staking_programmes
    autonolas_v1 -->|<a href="https://github.com/valory-xyz/autonolas-v1/blob/main/remappings.txt#L2" target="_blank">Link</a>| autonolas_tokenomics
    dev_template -->|<a href="https://github.com/valory-xyz/dev-template/blob/main/pyproject.toml#L19" target="_blank">Link</a>| open_autonomy
    docs -->|<a href="https://github.com/valory-xyz/docs/blob/main/.gitmodules#L16" target="_blank">Link</a>| hello_world
    docs -->|<a href="https://github.com/valory-xyz/docs/blob/main/.gitmodules#L10" target="_blank">Link</a>| mech
    docs -->|<a href="https://github.com/valory-xyz/docs/blob/main/.gitmodules#L25" target="_blank">Link</a>| mech_server
    docs -->|<a href="https://github.com/valory-xyz/docs/blob/main/.gitmodules#L13" target="_blank">Link</a>| open_acn
    docs -->|<a href="https://github.com/valory-xyz/docs/blob/main/.gitmodules#L19" target="_blank">Link</a>| open_aea
    docs -->|<a href="https://github.com/valory-xyz/docs/blob/main/.gitmodules#L1" target="_blank">Link</a>| open_autonomy
    docs -->|<a href="https://github.com/valory-xyz/docs/blob/main/pyproject.toml#L11" target="_blank">Link</a>| tomte
    funds_manager -->|<a href="https://github.com/valory-xyz/funds-manager/blob/main/pyproject.toml#L56" target="_blank">Link</a>| open_aea
    funds_manager -->|<a href="https://github.com/valory-xyz/funds-manager/blob/main/pyproject.toml#L49" target="_blank">Link</a>| open_autonomy
    funds_manager -->|<a href="https://github.com/valory-xyz/funds-manager/blob/main/pyproject.toml#L88" target="_blank">Link</a>| tomte
    genai -->|<a href="https://github.com/valory-xyz/genai/blob/main/pyproject.toml#L59" target="_blank">Link</a>| open_aea
    genai -->|<a href="https://github.com/valory-xyz/genai/blob/main/pyproject.toml#L52" target="_blank">Link</a>| open_autonomy
    genai -->|<a href="https://github.com/valory-xyz/genai/blob/main/pyproject.toml#L97" target="_blank">Link</a>| tomte
    hello_world -->|<a href="https://github.com/valory-xyz/hello-world/blob/main/Pipfile#L7" target="_blank">Link</a>| open_aea
    hello_world -->|<a href="https://github.com/valory-xyz/hello-world/blob/main/Pipfile#L12" target="_blank">Link</a>| open_autonomy
    hello_world -->|<a href="https://github.com/valory-xyz/hello-world/blob/main/Pipfile#L46" target="_blank">Link</a>| tomte
    IEKit -->|<a href="https://github.com/valory-xyz/IEKit/blob/main/packages/packages.json#L39" target="_blank">Link</a>| genai
    IEKit -->|<a href="https://github.com/valory-xyz/IEKit/blob/main/packages/packages.json#L49" target="_blank">Link</a>| mech_interact
    IEKit -->|<a href="https://github.com/valory-xyz/IEKit/blob/main/pyproject.toml#L42" target="_blank">Link</a>| open_aea
    IEKit -->|<a href="https://github.com/valory-xyz/IEKit/blob/main/pyproject.toml#L35" target="_blank">Link</a>| open_autonomy
    IEKit -->|<a href="https://github.com/valory-xyz/IEKit/blob/main/pyproject.toml#L90" target="_blank">Link</a>| tomte
    kv_store -->|<a href="https://github.com/valory-xyz/kv-store/blob/main/pyproject.toml#L26" target="_blank">Link</a>| open_aea
    kv_store -->|<a href="https://github.com/valory-xyz/kv-store/blob/main/pyproject.toml#L19" target="_blank">Link</a>| open_autonomy
    kv_store -->|<a href="https://github.com/valory-xyz/kv-store/blob/main/pyproject.toml#L52" target="_blank">Link</a>| tomte
    market_creator -->|<a href="https://github.com/valory-xyz/market-creator/blob/main/packages/packages.json#L20" target="_blank">Link</a>| genai
    market_creator -->|<a href="https://github.com/valory-xyz/market-creator/blob/main/packages/packages.json#L25" target="_blank">Link</a>| mech_interact
    market_creator -->|<a href="https://github.com/valory-xyz/market-creator/blob/main/pyproject.toml#L25" target="_blank">Link</a>| open_aea
    market_creator -->|<a href="https://github.com/valory-xyz/market-creator/blob/main/pyproject.toml#L19" target="_blank">Link</a>| open_autonomy
    market_creator -->|<a href="https://github.com/valory-xyz/market-creator/blob/main/pyproject.toml#L54" target="_blank">Link</a>| tomte
    market_creator -->|<a href="https://github.com/valory-xyz/market-creator/blob/main/packages/packages.json#L38" target="_blank">Link</a>| trader
    mech -->|<a href="https://github.com/valory-xyz/mech/blob/main/pyproject.toml#L26" target="_blank">Link</a>| open_aea
    mech -->|<a href="https://github.com/valory-xyz/mech/blob/main/pyproject.toml#L19" target="_blank">Link</a>| open_autonomy
    mech_agents_fun -->|<a href="https://github.com/valory-xyz/mech-agents-fun/blob/main/packages/packages.json#L21" target="_blank">Link</a>| mech
    mech_agents_fun -->|<a href="https://github.com/valory-xyz/mech-agents-fun/blob/main/pyproject.toml#L26" target="_blank">Link</a>| open_aea
    mech_agents_fun -->|<a href="https://github.com/valory-xyz/mech-agents-fun/blob/main/pyproject.toml#L19" target="_blank">Link</a>| open_autonomy
    mech_client -->|<a href="https://github.com/valory-xyz/mech-client/blob/main/pyproject.toml#L25" target="_blank">Link</a>| olas_operate_middleware
    mech_client -->|<a href="https://github.com/valory-xyz/mech-client/blob/main/packages/packages.json#L8" target="_blank">Link</a>| open_aea
    mech_client -->|<a href="https://github.com/valory-xyz/mech-client/blob/main/packages/packages.json#L7" target="_blank">Link</a>| open_autonomy
    mech_interact -->|<a href="https://github.com/valory-xyz/mech-interact/blob/main/Pipfile#L25" target="_blank">Link</a>| open_aea
    mech_interact -->|<a href="https://github.com/valory-xyz/mech-interact/blob/main/Pipfile#L29" target="_blank">Link</a>| open_autonomy
    mech_interact -->|<a href="https://github.com/valory-xyz/mech-interact/blob/main/Pipfile#L31" target="_blank">Link</a>| tomte
    mech_predict -->|<a href="https://github.com/valory-xyz/mech-predict/blob/main/packages/packages.json#L30" target="_blank">Link</a>| mech
    mech_predict -->|<a href="https://github.com/valory-xyz/mech-predict/blob/main/pyproject.toml#L26" target="_blank">Link</a>| open_aea
    mech_predict -->|<a href="https://github.com/valory-xyz/mech-predict/blob/main/pyproject.toml#L19" target="_blank">Link</a>| open_autonomy
    mech_server -->|<a href="https://github.com/valory-xyz/mech-server/blob/main/packages/packages.json#L8" target="_blank">Link</a>| mech
    mech_server -->|<a href="https://github.com/valory-xyz/mech-server/blob/main/pyproject.toml#L74" target="_blank">Link</a>| mech_client
    mech_server -->|<a href="https://github.com/valory-xyz/mech-server/blob/main/pyproject.toml#L75" target="_blank">Link</a>| olas_operate_middleware
    mech_server -->|<a href="https://github.com/valory-xyz/mech-server/blob/main/pyproject.toml#L45" target="_blank">Link</a>| open_aea
    mech_server -->|<a href="https://github.com/valory-xyz/mech-server/blob/main/pyproject.toml#L38" target="_blank">Link</a>| open_autonomy
    meme_ooorr -->|<a href="https://github.com/valory-xyz/meme-ooorr/blob/main/packages/packages.json#L64" target="_blank">Link</a>| funds_manager
    meme_ooorr -->|<a href="https://github.com/valory-xyz/meme-ooorr/blob/main/packages/packages.json#L25" target="_blank">Link</a>| genai
    meme_ooorr -->|<a href="https://github.com/valory-xyz/meme-ooorr/blob/main/packages/packages.json#L26" target="_blank">Link</a>| kv_store
    meme_ooorr -->|<a href="https://github.com/valory-xyz/meme-ooorr/blob/main/packages/packages.json#L31" target="_blank">Link</a>| mech_interact
    meme_ooorr -->|<a href="https://github.com/valory-xyz/meme-ooorr/blob/main/pyproject.toml#L20" target="_blank">Link</a>| open_aea
    meme_ooorr -->|<a href="https://github.com/valory-xyz/meme-ooorr/blob/main/pyproject.toml#L19" target="_blank">Link</a>| open_autonomy
    meme_ooorr -->|<a href="https://github.com/valory-xyz/meme-ooorr/blob/main/pyproject.toml#L25" target="_blank">Link</a>| tomte
    olas_operate_app -->|<a href="https://github.com/valory-xyz/olas-operate-app/blob/main/pyproject.toml#L13" target="_blank">Link</a>| olas_operate_middleware
    olas_operate_middleware -->|<a href="https://github.com/valory-xyz/olas-operate-middleware/blob/main/pyproject.toml#L23" target="_blank">Link</a>| open_aea
    olas_operate_middleware -->|<a href="https://github.com/valory-xyz/olas-operate-middleware/blob/main/pyproject.toml#L22" target="_blank">Link</a>| open_autonomy
    olas_sdk_starter -->|<a href="https://github.com/valory-xyz/olas-sdk-starter/blob/main/packages/packages.json#L8" target="_blank">Link</a>| open_aea
    olas_sdk_starter -->|<a href="https://github.com/valory-xyz/olas-sdk-starter/blob/main/Pipfile#L7" target="_blank">Link</a>| open_autonomy
    olas_sdk_starter -->|<a href="https://github.com/valory-xyz/olas-sdk-starter/blob/main/Pipfile#L10" target="_blank">Link</a>| tomte
    open_aea -->|<a href="https://github.com/valory-xyz/open-aea/blob/main/plugins/aea-ledger-ethereum-flashbots/setup.py#L44" target="_blank">Link</a>| open_aea_flashbots
    open_aea -->|<a href="https://github.com/valory-xyz/open-aea/blob/main/Pipfile#L51" target="_blank">Link</a>| tomte
    open_autonomy -->|<a href="https://github.com/valory-xyz/open-autonomy/blob/main/setup.py#L33" target="_blank">Link</a>| open_aea
    open_autonomy -->|<a href="https://github.com/valory-xyz/open-autonomy/blob/main/pyproject.toml#L23" target="_blank">Link</a>| tomte
    optimus -->|<a href="https://github.com/valory-xyz/optimus/blob/main/packages/packages.json#L64" target="_blank">Link</a>| funds_manager
    optimus -->|<a href="https://github.com/valory-xyz/optimus/blob/main/packages/packages.json#L40" target="_blank">Link</a>| genai
    optimus -->|<a href="https://github.com/valory-xyz/optimus/blob/main/packages/packages.json#L41" target="_blank">Link</a>| kv_store
    optimus -->|<a href="https://github.com/valory-xyz/optimus/blob/main/pyproject.toml#L20" target="_blank">Link</a>| open_aea
    optimus -->|<a href="https://github.com/valory-xyz/optimus/blob/main/pyproject.toml#L19" target="_blank">Link</a>| open_autonomy
    optimus -->|<a href="https://github.com/valory-xyz/optimus/blob/main/pyproject.toml#L27" target="_blank">Link</a>| tomte
    pettai_agent -->|<a href="https://github.com/valory-xyz/pettai-agent/blob/main/olas-sdk-starter/Pipfile#L7" target="_blank">Link</a>| open_aea
    pettai_agent -->|<a href="https://github.com/valory-xyz/pettai-agent/blob/main/olas-sdk-starter/Pipfile#L9" target="_blank">Link</a>| open_aea_cosmpy
    pettai_agent -->|<a href="https://github.com/valory-xyz/pettai-agent/blob/main/olas-sdk-starter/Pipfile#L13" target="_blank">Link</a>| open_autonomy
    pettai_agent -->|<a href="https://github.com/valory-xyz/pettai-agent/blob/main/olas-sdk-starter/Pipfile#L48" target="_blank">Link</a>| tomte
    propel_client -->|<a href="https://github.com/valory-xyz/propel-client/blob/main/pyproject.toml#L14" target="_blank">Link</a>| open_autonomy
    quickstart -->|<a href="https://github.com/valory-xyz/quickstart/blob/main/pyproject.toml#L13" target="_blank">Link</a>| olas_operate_middleware
    trader -->|<a href="https://github.com/valory-xyz/trader/blob/main/packages/packages.json#L76" target="_blank">Link</a>| funds_manager
    trader -->|<a href="https://github.com/valory-xyz/trader/blob/main/packages/packages.json#L39" target="_blank">Link</a>| genai
    trader -->|<a href="https://github.com/valory-xyz/trader/blob/main/packages/packages.json#L42" target="_blank">Link</a>| mech_interact
    trader -->|<a href="https://github.com/valory-xyz/trader/blob/main/pyproject.toml#L58" target="_blank">Link</a>| open_aea
    trader -->|<a href="https://github.com/valory-xyz/trader/blob/main/pyproject.toml#L51" target="_blank">Link</a>| open_autonomy
    trader -->|<a href="https://github.com/valory-xyz/trader/blob/main/pyproject.toml#L97" target="_blank">Link</a>| tomte
    triton_bot -->|<a href="https://github.com/valory-xyz/triton-bot/blob/main/pyproject.toml#L12" target="_blank">Link</a>| olas_operate_middleware

```
