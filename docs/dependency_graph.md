# Valory Repository Dependency Graph

```mermaid
flowchart LR

    %% Nodes
    agent_scan["agent-scan"]
    agent_ui_monorepo["agent-ui-monorepo"]
    agents_fun_eliza["agents-fun-eliza"]
    autonolas_frontend_mono["autonolas-frontend-mono"]
    autonolas_governance["autonolas-governance"]
    autonolas_marketplace["autonolas-marketplace"]
    autonolas_registries["autonolas-registries"]
    autonolas_staking_programmes["autonolas-staking-programmes"]
    autonolas_subgraph["autonolas-subgraph"]
    autonolas_subgraph_studio["autonolas-subgraph-studio"]
    autonolas_tokenomics["autonolas-tokenomics"]
    autonolas_v1["autonolas-v1"]
    brand_and_press_kit_agents_unleashed["brand-and-press-kit-agents-unleashed"]
    dev_template["dev-template"]
    docs["docs"]
    dynamic_contribution["dynamic-contribution"]
    eliza_memeooorr_olas_sdk["eliza-memeooorr-olas-sdk"]
    governance_near["governance-near"]
    hello_world["hello-world"]
    IEKit["IEKit"]
    langchain_trader["langchain-trader"]
    langchain_hello_world["langchain_hello_world"]
    lockbox_governor_solana["lockbox-governor-solana"]
    lockbox_solana["lockbox-solana"]
    market_creator["market-creator"]
    mech["mech"]
    mech_agents_fun["mech-agents-fun"]
    mech_client["mech-client"]
    mech_interact["mech-interact"]
    mech_legacy["mech-legacy"]
    mech_marketplace_legacy["mech-marketplace-legacy"]
    mech_predict["mech-predict"]
    mech_tools_dev["mech-tools-dev"]
    meme_ooorr["meme-ooorr"]
    meme_ooorr_test["meme-ooorr-test"]
    mock_mech["mock-mech"]
    nevermined_sdk_js["nevermined-sdk-js"]
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
    plugin_memeooorr["plugin-memeooorr"]
    price_oracle["price-oracle"]
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
    click agent_scan "https://github.com/valory-xyz/agent-scan" _blank
    click agent_ui_monorepo "https://github.com/valory-xyz/agent-ui-monorepo" _blank
    click agents_fun_eliza "https://github.com/valory-xyz/agents-fun-eliza" _blank
    click autonolas_frontend_mono "https://github.com/valory-xyz/autonolas-frontend-mono" _blank
    click autonolas_governance "https://github.com/valory-xyz/autonolas-governance" _blank
    click autonolas_marketplace "https://github.com/valory-xyz/autonolas-marketplace" _blank
    click autonolas_registries "https://github.com/valory-xyz/autonolas-registries" _blank
    click autonolas_staking_programmes "https://github.com/valory-xyz/autonolas-staking-programmes" _blank
    click autonolas_subgraph "https://github.com/valory-xyz/autonolas-subgraph" _blank
    click autonolas_subgraph_studio "https://github.com/valory-xyz/autonolas-subgraph-studio" _blank
    click autonolas_tokenomics "https://github.com/valory-xyz/autonolas-tokenomics" _blank
    click autonolas_v1 "https://github.com/valory-xyz/autonolas-v1" _blank
    click brand_and_press_kit_agents_unleashed "https://github.com/valory-xyz/brand-and-press-kit-agents-unleashed" _blank
    click dev_template "https://github.com/valory-xyz/dev-template" _blank
    click docs "https://github.com/valory-xyz/docs" _blank
    click dynamic_contribution "https://github.com/valory-xyz/dynamic-contribution" _blank
    click eliza_memeooorr_olas_sdk "https://github.com/valory-xyz/eliza-memeooorr-olas-sdk" _blank
    click governance_near "https://github.com/valory-xyz/governance-near" _blank
    click hello_world "https://github.com/valory-xyz/hello-world" _blank
    click IEKit "https://github.com/valory-xyz/IEKit" _blank
    click langchain_trader "https://github.com/valory-xyz/langchain-trader" _blank
    click langchain_hello_world "https://github.com/valory-xyz/langchain_hello_world" _blank
    click lockbox_governor_solana "https://github.com/valory-xyz/lockbox-governor-solana" _blank
    click lockbox_solana "https://github.com/valory-xyz/lockbox-solana" _blank
    click market_creator "https://github.com/valory-xyz/market-creator" _blank
    click mech "https://github.com/valory-xyz/mech" _blank
    click mech_agents_fun "https://github.com/valory-xyz/mech-agents-fun" _blank
    click mech_client "https://github.com/valory-xyz/mech-client" _blank
    click mech_interact "https://github.com/valory-xyz/mech-interact" _blank
    click mech_legacy "https://github.com/valory-xyz/mech-legacy" _blank
    click mech_marketplace_legacy "https://github.com/valory-xyz/mech-marketplace-legacy" _blank
    click mech_predict "https://github.com/valory-xyz/mech-predict" _blank
    click mech_tools_dev "https://github.com/valory-xyz/mech-tools-dev" _blank
    click meme_ooorr "https://github.com/valory-xyz/meme-ooorr" _blank
    click meme_ooorr_test "https://github.com/valory-xyz/meme-ooorr-test" _blank
    click mock_mech "https://github.com/valory-xyz/mock-mech" _blank
    click nevermined_sdk_js "https://github.com/valory-xyz/nevermined-sdk-js" _blank
    click olas "https://github.com/valory-xyz/olas" _blank
    click olas_operate_app "https://github.com/valory-xyz/olas-operate-app" _blank
    click olas_operate_middleware "https://github.com/valory-xyz/olas-operate-middleware" _blank
    click olas_predict "https://github.com/valory-xyz/olas-predict" _blank
    click olas_sdk_starter "https://github.com/valory-xyz/olas-sdk-starter" _blank
    click olas_website "https://github.com/valory-xyz/olas-website" _blank
    click open_acn "https://github.com/valory-xyz/open-acn" _blank
    click open_aea "https://github.com/valory-xyz/open-aea" _blank
    click open_aea_cosmpy "https://github.com/valory-xyz/open-aea-cosmpy" _blank
    click open_aea_flashbots "https://github.com/valory-xyz/open-aea-flashbots" _blank
    click open_autonomy "https://github.com/valory-xyz/open-autonomy" _blank
    click open_autonomy_client "https://github.com/valory-xyz/open-autonomy-client" _blank
    click optimus "https://github.com/valory-xyz/optimus" _blank
    click pettai_agent "https://github.com/valory-xyz/pettai-agent" _blank
    click plugin_memeooorr "https://github.com/valory-xyz/plugin-memeooorr" _blank
    click price_oracle "https://github.com/valory-xyz/price-oracle" _blank
    click propel_client "https://github.com/valory-xyz/propel-client" _blank
    click quickstart "https://github.com/valory-xyz/quickstart" _blank
    click registries_near "https://github.com/valory-xyz/registries-near" _blank
    click registries_solana "https://github.com/valory-xyz/registries-solana" _blank
    click tomte "https://github.com/valory-xyz/tomte" _blank
    click trader "https://github.com/valory-xyz/trader" _blank
    click triton_bot "https://github.com/valory-xyz/triton-bot" _blank
    click valory_website "https://github.com/valory-xyz/valory-website" _blank
    click wormhole_sdk_vaa "https://github.com/valory-xyz/wormhole-sdk-vaa" _blank
    click x402 "https://github.com/valory-xyz/x402" _blank

    %% Dependencies
    agents_fun_eliza -->|<a href="https://github.com/valory-xyz/agents-fun-eliza/blob/main/agents-fun/package.json#L15" target="_blank">Link</a>| plugin_memeooorr
    autonolas_marketplace -->|<a href="https://github.com/valory-xyz/autonolas-marketplace/blob/main/.gitmodules#L1" target="_blank">Link</a>| autonolas_registries
    autonolas_staking_programmes -->|<a href="https://github.com/valory-xyz/autonolas-staking-programmes/blob/main/.gitmodules#L1" target="_blank">Link</a>| autonolas_registries
    autonolas_subgraph -->|<a href="https://github.com/valory-xyz/autonolas-subgraph/blob/main/.gitmodules#L1" target="_blank">Link</a>| autonolas_registries
    autonolas_v1 -->|<a href="https://github.com/valory-xyz/autonolas-v1/blob/main/remappings.txt#L3" target="_blank">Link</a>| autonolas_governance
    autonolas_v1 -->|<a href="https://github.com/valory-xyz/autonolas-v1/blob/main/.gitmodules#L13" target="_blank">Link</a>| autonolas_marketplace
    autonolas_v1 -->|<a href="https://github.com/valory-xyz/autonolas-v1/blob/main/remappings.txt#L4" target="_blank">Link</a>| autonolas_registries
    autonolas_v1 -->|<a href="https://github.com/valory-xyz/autonolas-v1/blob/main/.gitmodules#L16" target="_blank">Link</a>| autonolas_staking_programmes
    autonolas_v1 -->|<a href="https://github.com/valory-xyz/autonolas-v1/blob/main/remappings.txt#L2" target="_blank">Link</a>| autonolas_tokenomics
    dev_template -->|<a href="https://github.com/valory-xyz/dev-template/blob/main/pyproject.toml#L19" target="_blank">Link</a>| open_autonomy
    dev_template -->|<a href="https://github.com/valory-xyz/dev-template/blob/main/pyproject.toml#L22" target="_blank">Link</a>| tomte
    docs -->|<a href="https://github.com/valory-xyz/docs/blob/main/.gitmodules#L16" target="_blank">Link</a>| hello_world
    docs -->|<a href="https://github.com/valory-xyz/docs/blob/main/.gitmodules#L10" target="_blank">Link</a>| mech
    docs -->|<a href="https://github.com/valory-xyz/docs/blob/main/.gitmodules#L22" target="_blank">Link</a>| mech_tools_dev
    docs -->|<a href="https://github.com/valory-xyz/docs/blob/main/.gitmodules#L13" target="_blank">Link</a>| open_acn
    docs -->|<a href="https://github.com/valory-xyz/docs/blob/main/.gitmodules#L19" target="_blank">Link</a>| open_aea
    docs -->|<a href="https://github.com/valory-xyz/docs/blob/main/.gitmodules#L1" target="_blank">Link</a>| open_autonomy
    docs -->|<a href="https://github.com/valory-xyz/docs/blob/main/.gitmodules#L4" target="_blank">Link</a>| price_oracle
    docs -->|<a href="https://github.com/valory-xyz/docs/blob/main/pyproject.toml#L10" target="_blank">Link</a>| tomte
    eliza_memeooorr_olas_sdk -->|<a href="https://github.com/valory-xyz/eliza-memeooorr-olas-sdk/blob/main/Pipfile#L7" target="_blank">Link</a>| open_aea
    eliza_memeooorr_olas_sdk -->|<a href="https://github.com/valory-xyz/eliza-memeooorr-olas-sdk/blob/main/Pipfile#L9" target="_blank">Link</a>| open_aea_cosmpy
    eliza_memeooorr_olas_sdk -->|<a href="https://github.com/valory-xyz/eliza-memeooorr-olas-sdk/blob/main/Pipfile#L15" target="_blank">Link</a>| open_autonomy
    eliza_memeooorr_olas_sdk -->|<a href="https://github.com/valory-xyz/eliza-memeooorr-olas-sdk/blob/main/Pipfile#L48" target="_blank">Link</a>| tomte
    hello_world -->|<a href="https://github.com/valory-xyz/hello-world/blob/main/packages/packages.json#L8" target="_blank">Link</a>| mech_legacy
    hello_world -->|<a href="https://github.com/valory-xyz/hello-world/blob/main/packages/packages.json#L8" target="_blank">Link</a>| mech_marketplace_legacy
    hello_world -->|<a href="https://github.com/valory-xyz/hello-world/blob/main/Pipfile#L7" target="_blank">Link</a>| open_aea
    hello_world -->|<a href="https://github.com/valory-xyz/hello-world/blob/main/Pipfile#L9" target="_blank">Link</a>| open_aea_cosmpy
    hello_world -->|<a href="https://github.com/valory-xyz/hello-world/blob/main/Pipfile#L15" target="_blank">Link</a>| open_autonomy
    hello_world -->|<a href="https://github.com/valory-xyz/hello-world/blob/main/Pipfile#L48" target="_blank">Link</a>| tomte
    IEKit -->|<a href="https://github.com/valory-xyz/IEKit/blob/main/packages/packages.json#L49" target="_blank">Link</a>| mech
    IEKit -->|<a href="https://github.com/valory-xyz/IEKit/blob/main/packages/packages.json#L47" target="_blank">Link</a>| mech_interact
    IEKit -->|<a href="https://github.com/valory-xyz/IEKit/blob/main/packages/packages.json#L34" target="_blank">Link</a>| mech_legacy
    IEKit -->|<a href="https://github.com/valory-xyz/IEKit/blob/main/packages/packages.json#L34" target="_blank">Link</a>| mech_marketplace_legacy
    IEKit -->|<a href="https://github.com/valory-xyz/IEKit/blob/main/Pipfile#L32" target="_blank">Link</a>| open_aea
    IEKit -->|<a href="https://github.com/valory-xyz/IEKit/blob/main/Pipfile#L37" target="_blank">Link</a>| open_autonomy
    IEKit -->|<a href="https://github.com/valory-xyz/IEKit/blob/main/packages/packages.json#L52" target="_blank">Link</a>| optimus
    IEKit -->|<a href="https://github.com/valory-xyz/IEKit/blob/main/Pipfile#L38" target="_blank">Link</a>| tomte
    langchain_trader -->|<a href="https://github.com/valory-xyz/langchain-trader/blob/master/packages/packages.json#L22" target="_blank">Link</a>| mech
    langchain_trader -->|<a href="https://github.com/valory-xyz/langchain-trader/blob/master/packages/packages.json#L21" target="_blank">Link</a>| mech_interact
    langchain_trader -->|<a href="https://github.com/valory-xyz/langchain-trader/blob/master/packages/packages.json#L9" target="_blank">Link</a>| mech_legacy
    langchain_trader -->|<a href="https://github.com/valory-xyz/langchain-trader/blob/master/packages/packages.json#L9" target="_blank">Link</a>| mech_marketplace_legacy
    langchain_trader -->|<a href="https://github.com/valory-xyz/langchain-trader/blob/master/pyproject.toml#L20" target="_blank">Link</a>| open_aea
    langchain_trader -->|<a href="https://github.com/valory-xyz/langchain-trader/blob/master/pyproject.toml#L19" target="_blank">Link</a>| open_autonomy
    langchain_trader -->|<a href="https://github.com/valory-xyz/langchain-trader/blob/master/packages/packages.json#L22" target="_blank">Link</a>| optimus
    langchain_trader -->|<a href="https://github.com/valory-xyz/langchain-trader/blob/master/pyproject.toml#L24" target="_blank">Link</a>| tomte
    market_creator -->|<a href="https://github.com/valory-xyz/market-creator/blob/main/packages/packages.json#L19" target="_blank">Link</a>| IEKit
    market_creator -->|<a href="https://github.com/valory-xyz/market-creator/blob/main/packages/packages.json#L29" target="_blank">Link</a>| mech
    market_creator -->|<a href="https://github.com/valory-xyz/market-creator/blob/main/packages/packages.json#L28" target="_blank">Link</a>| mech_interact
    market_creator -->|<a href="https://github.com/valory-xyz/market-creator/blob/main/packages/packages.json#L11" target="_blank">Link</a>| mech_legacy
    market_creator -->|<a href="https://github.com/valory-xyz/market-creator/blob/main/packages/packages.json#L11" target="_blank">Link</a>| mech_marketplace_legacy
    market_creator -->|<a href="https://github.com/valory-xyz/market-creator/blob/main/packages/packages.json#L11" target="_blank">Link</a>| open_aea
    market_creator -->|<a href="https://github.com/valory-xyz/market-creator/blob/main/pyproject.toml#L19" target="_blank">Link</a>| open_autonomy
    market_creator -->|<a href="https://github.com/valory-xyz/market-creator/blob/main/packages/packages.json#L29" target="_blank">Link</a>| optimus
    market_creator -->|<a href="https://github.com/valory-xyz/market-creator/blob/main/pyproject.toml#L46" target="_blank">Link</a>| tomte
    market_creator -->|<a href="https://github.com/valory-xyz/market-creator/blob/main/packages/packages.json#L25" target="_blank">Link</a>| trader
    mech -->|<a href="https://github.com/valory-xyz/mech/blob/main/packages/packages.json#L21" target="_blank">Link</a>| mech_legacy
    mech -->|<a href="https://github.com/valory-xyz/mech/blob/main/packages/packages.json#L21" target="_blank">Link</a>| mech_marketplace_legacy
    mech -->|<a href="https://github.com/valory-xyz/mech/blob/main/packages/packages.json#L21" target="_blank">Link</a>| open_aea
    mech -->|<a href="https://github.com/valory-xyz/mech/blob/main/pyproject.toml#L19" target="_blank">Link</a>| open_autonomy
    mech_agents_fun -->|<a href="https://github.com/valory-xyz/mech-agents-fun/blob/main/packages/packages.json#L13" target="_blank">Link</a>| mech
    mech_agents_fun -->|<a href="https://github.com/valory-xyz/mech-agents-fun/blob/main/packages/packages.json#L26" target="_blank">Link</a>| mech_interact
    mech_agents_fun -->|<a href="https://github.com/valory-xyz/mech-agents-fun/blob/main/packages/packages.json#L12" target="_blank">Link</a>| mech_legacy
    mech_agents_fun -->|<a href="https://github.com/valory-xyz/mech-agents-fun/blob/main/packages/packages.json#L12" target="_blank">Link</a>| mech_marketplace_legacy
    mech_agents_fun -->|<a href="https://github.com/valory-xyz/mech-agents-fun/blob/main/packages/packages.json#L15" target="_blank">Link</a>| open_aea
    mech_agents_fun -->|<a href="https://github.com/valory-xyz/mech-agents-fun/blob/main/pyproject.toml#L19" target="_blank">Link</a>| open_autonomy
    mech_agents_fun -->|<a href="https://github.com/valory-xyz/mech-agents-fun/blob/main/packages/packages.json#L28" target="_blank">Link</a>| optimus
    mech_client -->|<a href="https://github.com/valory-xyz/mech-client/blob/main/packages/packages.json#L7" target="_blank">Link</a>| mech_legacy
    mech_client -->|<a href="https://github.com/valory-xyz/mech-client/blob/main/packages/packages.json#L7" target="_blank">Link</a>| mech_marketplace_legacy
    mech_client -->|<a href="https://github.com/valory-xyz/mech-client/blob/main/pyproject.toml#L17" target="_blank">Link</a>| olas_operate_middleware
    mech_client -->|<a href="https://github.com/valory-xyz/mech-client/blob/main/packages/packages.json#L8" target="_blank">Link</a>| open_aea
    mech_client -->|<a href="https://github.com/valory-xyz/mech-client/blob/main/packages/packages.json#L7" target="_blank">Link</a>| open_autonomy
    mech_interact -->|<a href="https://github.com/valory-xyz/mech-interact/blob/main/packages/packages.json#L22" target="_blank">Link</a>| mech_legacy
    mech_interact -->|<a href="https://github.com/valory-xyz/mech-interact/blob/main/packages/packages.json#L22" target="_blank">Link</a>| mech_marketplace_legacy
    mech_interact -->|<a href="https://github.com/valory-xyz/mech-interact/blob/main/Pipfile#L25" target="_blank">Link</a>| open_aea
    mech_interact -->|<a href="https://github.com/valory-xyz/mech-interact/blob/main/Pipfile#L30" target="_blank">Link</a>| open_autonomy
    mech_interact -->|<a href="https://github.com/valory-xyz/mech-interact/blob/main/Pipfile#L31" target="_blank">Link</a>| tomte
    mech_legacy -->|<a href="https://github.com/valory-xyz/mech-legacy/blob/main/pyproject.toml#L22" target="_blank">Link</a>| mech_client
    mech_legacy -->|<a href="https://github.com/valory-xyz/mech-legacy/blob/main/pyproject.toml#L19" target="_blank">Link</a>| open_autonomy
    mech_marketplace_legacy -->|<a href="https://github.com/valory-xyz/mech-marketplace-legacy/blob/main/pyproject.toml#L22" target="_blank">Link</a>| mech_client
    mech_marketplace_legacy -->|<a href="https://github.com/valory-xyz/mech-marketplace-legacy/blob/main/pyproject.toml#L19" target="_blank">Link</a>| open_autonomy
    mech_predict -->|<a href="https://github.com/valory-xyz/mech-predict/blob/main/packages/packages.json#L35" target="_blank">Link</a>| mech
    mech_predict -->|<a href="https://github.com/valory-xyz/mech-predict/blob/main/packages/packages.json#L43" target="_blank">Link</a>| mech_interact
    mech_predict -->|<a href="https://github.com/valory-xyz/mech-predict/blob/main/packages/packages.json#L26" target="_blank">Link</a>| mech_legacy
    mech_predict -->|<a href="https://github.com/valory-xyz/mech-predict/blob/main/packages/packages.json#L26" target="_blank">Link</a>| mech_marketplace_legacy
    mech_predict -->|<a href="https://github.com/valory-xyz/mech-predict/blob/main/packages/packages.json#L26" target="_blank">Link</a>| open_aea
    mech_predict -->|<a href="https://github.com/valory-xyz/mech-predict/blob/main/pyproject.toml#L19" target="_blank">Link</a>| open_autonomy
    mech_predict -->|<a href="https://github.com/valory-xyz/mech-predict/blob/main/packages/packages.json#L45" target="_blank">Link</a>| optimus
    mech_tools_dev -->|<a href="https://github.com/valory-xyz/mech-tools-dev/blob/main/packages/packages.json#L9" target="_blank">Link</a>| mech
    mech_tools_dev -->|<a href="https://github.com/valory-xyz/mech-tools-dev/blob/main/pyproject.toml#L54" target="_blank">Link</a>| mech_client
    mech_tools_dev -->|<a href="https://github.com/valory-xyz/mech-tools-dev/blob/main/packages/packages.json#L21" target="_blank">Link</a>| mech_interact
    mech_tools_dev -->|<a href="https://github.com/valory-xyz/mech-tools-dev/blob/main/packages/packages.json#L8" target="_blank">Link</a>| mech_legacy
    mech_tools_dev -->|<a href="https://github.com/valory-xyz/mech-tools-dev/blob/main/packages/packages.json#L8" target="_blank">Link</a>| mech_marketplace_legacy
    mech_tools_dev -->|<a href="https://github.com/valory-xyz/mech-tools-dev/blob/main/pyproject.toml#L55" target="_blank">Link</a>| olas_operate_middleware
    mech_tools_dev -->|<a href="https://github.com/valory-xyz/mech-tools-dev/blob/main/packages/packages.json#L10" target="_blank">Link</a>| open_aea
    mech_tools_dev -->|<a href="https://github.com/valory-xyz/mech-tools-dev/blob/main/pyproject.toml#L19" target="_blank">Link</a>| open_autonomy
    mech_tools_dev -->|<a href="https://github.com/valory-xyz/mech-tools-dev/blob/main/packages/packages.json#L23" target="_blank">Link</a>| optimus
    meme_ooorr -->|<a href="https://github.com/valory-xyz/meme-ooorr/blob/main/packages/packages.json#L27" target="_blank">Link</a>| IEKit
    meme_ooorr -->|<a href="https://github.com/valory-xyz/meme-ooorr/blob/main/packages/packages.json#L31" target="_blank">Link</a>| mech
    meme_ooorr -->|<a href="https://github.com/valory-xyz/meme-ooorr/blob/main/packages/packages.json#L29" target="_blank">Link</a>| mech_interact
    meme_ooorr -->|<a href="https://github.com/valory-xyz/meme-ooorr/blob/main/packages/packages.json#L18" target="_blank">Link</a>| mech_legacy
    meme_ooorr -->|<a href="https://github.com/valory-xyz/meme-ooorr/blob/main/packages/packages.json#L18" target="_blank">Link</a>| mech_marketplace_legacy
    meme_ooorr -->|<a href="https://github.com/valory-xyz/meme-ooorr/blob/main/packages/packages.json#L49" target="_blank">Link</a>| meme_ooorr_test
    meme_ooorr -->|<a href="https://github.com/valory-xyz/meme-ooorr/blob/main/pyproject.toml#L20" target="_blank">Link</a>| open_aea
    meme_ooorr -->|<a href="https://github.com/valory-xyz/meme-ooorr/blob/main/pyproject.toml#L19" target="_blank">Link</a>| open_autonomy
    meme_ooorr -->|<a href="https://github.com/valory-xyz/meme-ooorr/blob/main/packages/packages.json#L41" target="_blank">Link</a>| optimus
    meme_ooorr -->|<a href="https://github.com/valory-xyz/meme-ooorr/blob/main/pyproject.toml#L24" target="_blank">Link</a>| tomte
    meme_ooorr_test -->|<a href="https://github.com/valory-xyz/meme-ooorr-test/blob/main/packages/packages.json#L28" target="_blank">Link</a>| IEKit
    meme_ooorr_test -->|<a href="https://github.com/valory-xyz/meme-ooorr-test/blob/main/packages/packages.json#L31" target="_blank">Link</a>| mech
    meme_ooorr_test -->|<a href="https://github.com/valory-xyz/meme-ooorr-test/blob/main/packages/packages.json#L30" target="_blank">Link</a>| mech_interact
    meme_ooorr_test -->|<a href="https://github.com/valory-xyz/meme-ooorr-test/blob/main/packages/packages.json#L19" target="_blank">Link</a>| mech_legacy
    meme_ooorr_test -->|<a href="https://github.com/valory-xyz/meme-ooorr-test/blob/main/packages/packages.json#L19" target="_blank">Link</a>| mech_marketplace_legacy
    meme_ooorr_test -->|<a href="https://github.com/valory-xyz/meme-ooorr-test/blob/main/pyproject.toml#L20" target="_blank">Link</a>| open_aea
    meme_ooorr_test -->|<a href="https://github.com/valory-xyz/meme-ooorr-test/blob/main/pyproject.toml#L19" target="_blank">Link</a>| open_autonomy
    meme_ooorr_test -->|<a href="https://github.com/valory-xyz/meme-ooorr-test/blob/main/packages/packages.json#L37" target="_blank">Link</a>| optimus
    meme_ooorr_test -->|<a href="https://github.com/valory-xyz/meme-ooorr-test/blob/main/pyproject.toml#L24" target="_blank">Link</a>| tomte
    olas_operate_app -->|<a href="https://github.com/valory-xyz/olas-operate-app/blob/main/pyproject.toml#L13" target="_blank">Link</a>| olas_operate_middleware
    olas_operate_middleware -->|<a href="https://github.com/valory-xyz/olas-operate-middleware/blob/main/pyproject.toml#L22" target="_blank">Link</a>| open_autonomy
    olas_sdk_starter -->|<a href="https://github.com/valory-xyz/olas-sdk-starter/blob/main/packages/packages.json#L7" target="_blank">Link</a>| mech_legacy
    olas_sdk_starter -->|<a href="https://github.com/valory-xyz/olas-sdk-starter/blob/main/packages/packages.json#L7" target="_blank">Link</a>| mech_marketplace_legacy
    olas_sdk_starter -->|<a href="https://github.com/valory-xyz/olas-sdk-starter/blob/main/Pipfile#L7" target="_blank">Link</a>| open_aea
    olas_sdk_starter -->|<a href="https://github.com/valory-xyz/olas-sdk-starter/blob/main/Pipfile#L9" target="_blank">Link</a>| open_aea_cosmpy
    olas_sdk_starter -->|<a href="https://github.com/valory-xyz/olas-sdk-starter/blob/main/Pipfile#L15" target="_blank">Link</a>| open_autonomy
    olas_sdk_starter -->|<a href="https://github.com/valory-xyz/olas-sdk-starter/blob/main/Pipfile#L48" target="_blank">Link</a>| tomte
    open_aea -->|<a href="https://github.com/valory-xyz/open-aea/blob/main/plugins/aea-ledger-ethereum-flashbots/setup.py#L45" target="_blank">Link</a>| open_aea_flashbots
    open_aea -->|<a href="https://github.com/valory-xyz/open-aea/blob/main/Pipfile#L52" target="_blank">Link</a>| tomte
    open_autonomy -->|<a href="https://github.com/valory-xyz/open-autonomy/blob/main/packages/packages.json#L59" target="_blank">Link</a>| mech_legacy
    open_autonomy -->|<a href="https://github.com/valory-xyz/open-autonomy/blob/main/packages/packages.json#L59" target="_blank">Link</a>| mech_marketplace_legacy
    open_autonomy -->|<a href="https://github.com/valory-xyz/open-autonomy/blob/main/setup.py#L35" target="_blank">Link</a>| open_aea
    open_autonomy -->|<a href="https://github.com/valory-xyz/open-autonomy/blob/main/Pipfile#L37" target="_blank">Link</a>| open_aea_cosmpy
    open_autonomy -->|<a href="https://github.com/valory-xyz/open-autonomy/blob/main/pyproject.toml#L23" target="_blank">Link</a>| tomte
    optimus -->|<a href="https://github.com/valory-xyz/optimus/blob/main/packages/packages.json#L44" target="_blank">Link</a>| IEKit
    optimus -->|<a href="https://github.com/valory-xyz/optimus/blob/main/packages/packages.json#L36" target="_blank">Link</a>| mech_legacy
    optimus -->|<a href="https://github.com/valory-xyz/optimus/blob/main/packages/packages.json#L36" target="_blank">Link</a>| mech_marketplace_legacy
    optimus -->|<a href="https://github.com/valory-xyz/optimus/blob/main/packages/packages.json#L50" target="_blank">Link</a>| meme_ooorr_test
    optimus -->|<a href="https://github.com/valory-xyz/optimus/blob/main/pyproject.toml#L20" target="_blank">Link</a>| open_aea
    optimus -->|<a href="https://github.com/valory-xyz/optimus/blob/main/pyproject.toml#L19" target="_blank">Link</a>| open_autonomy
    optimus -->|<a href="https://github.com/valory-xyz/optimus/blob/main/pyproject.toml#L26" target="_blank">Link</a>| tomte
    pettai_agent -->|<a href="https://github.com/valory-xyz/pettai-agent/blob/main/olas-sdk-starter/Pipfile#L7" target="_blank">Link</a>| open_aea
    pettai_agent -->|<a href="https://github.com/valory-xyz/pettai-agent/blob/main/olas-sdk-starter/Pipfile#L9" target="_blank">Link</a>| open_aea_cosmpy
    pettai_agent -->|<a href="https://github.com/valory-xyz/pettai-agent/blob/main/olas-sdk-starter/Pipfile#L48" target="_blank">Link</a>| tomte
    price_oracle -->|<a href="https://github.com/valory-xyz/price-oracle/blob/main/packages/packages.json#L11" target="_blank">Link</a>| mech_legacy
    price_oracle -->|<a href="https://github.com/valory-xyz/price-oracle/blob/main/packages/packages.json#L11" target="_blank">Link</a>| mech_marketplace_legacy
    price_oracle -->|<a href="https://github.com/valory-xyz/price-oracle/blob/main/Pipfile#L18" target="_blank">Link</a>| open_aea
    price_oracle -->|<a href="https://github.com/valory-xyz/price-oracle/blob/main/Pipfile#L23" target="_blank">Link</a>| open_autonomy
    price_oracle -->|<a href="https://github.com/valory-xyz/price-oracle/blob/main/Pipfile#L28" target="_blank">Link</a>| tomte
    propel_client -->|<a href="https://github.com/valory-xyz/propel-client/blob/main/pyproject.toml#L14" target="_blank">Link</a>| open_autonomy
    quickstart -->|<a href="https://github.com/valory-xyz/quickstart/blob/main/pyproject.toml#L13" target="_blank">Link</a>| olas_operate_middleware
    trader -->|<a href="https://github.com/valory-xyz/trader/blob/main/packages/packages.json#L40" target="_blank">Link</a>| IEKit
    trader -->|<a href="https://github.com/valory-xyz/trader/blob/main/packages/packages.json#L45" target="_blank">Link</a>| mech
    trader -->|<a href="https://github.com/valory-xyz/trader/blob/main/packages/packages.json#L41" target="_blank">Link</a>| mech_interact
    trader -->|<a href="https://github.com/valory-xyz/trader/blob/main/packages/packages.json#L31" target="_blank">Link</a>| mech_legacy
    trader -->|<a href="https://github.com/valory-xyz/trader/blob/main/packages/packages.json#L31" target="_blank">Link</a>| mech_marketplace_legacy
    trader -->|<a href="https://github.com/valory-xyz/trader/blob/main/packages/packages.json#L68" target="_blank">Link</a>| meme_ooorr_test
    trader -->|<a href="https://github.com/valory-xyz/trader/blob/main/packages/packages.json#L32" target="_blank">Link</a>| open_aea
    trader -->|<a href="https://github.com/valory-xyz/trader/blob/main/pyproject.toml#L47" target="_blank">Link</a>| open_autonomy
    trader -->|<a href="https://github.com/valory-xyz/trader/blob/main/packages/packages.json#L49" target="_blank">Link</a>| optimus
    trader -->|<a href="https://github.com/valory-xyz/trader/blob/main/pyproject.toml#L94" target="_blank">Link</a>| tomte
    triton_bot -->|<a href="https://github.com/valory-xyz/triton-bot/blob/main/pyproject.toml#L12" target="_blank">Link</a>| olas_operate_middleware

```
