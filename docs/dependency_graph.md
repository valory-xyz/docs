# Valory-xyz Repository Dependency Graph

```mermaid
flowchart LR

    %% ── Style Classes ──────────────────────────────────────────────────────────
    classDef foundation  fill:#4CAF50,color:#fff,stroke:#388E3C,stroke-width:2px
    classDef framework   fill:#2196F3,color:#fff,stroke:#1565C0,stroke-width:2px
    classDef onchain     fill:#FF9800,color:#fff,stroke:#E65100,stroke-width:2px
    classDef operations  fill:#9C27B0,color:#fff,stroke:#6A1B9A,stroke-width:2px
    classDef mecheco     fill:#F44336,color:#fff,stroke:#B71C1C,stroke-width:2px
    classDef agent       fill:#00BCD4,color:#fff,stroke:#006064,stroke-width:2px
    classDef enduser     fill:#E91E63,color:#fff,stroke:#880E4F,stroke-width:2px
    classDef frontend    fill:#607D8B,color:#fff,stroke:#263238,stroke-width:2px
    classDef devtools    fill:#FFC107,color:#000,stroke:#F57F17,stroke-width:2px
    classDef docs        fill:#ECEFF1,color:#000,stroke:#B0BEC5,stroke-width:2px

    %% ── Subgraph: Foundation ───────────────────────────────────────────────────
    subgraph FOUNDATION["🏗️ Foundation"]
        open_aea["open-aea<br>(AEA Framework)"]:::foundation
        open_acn["open-acn<br>(Agent Communication Network)"]:::foundation
        tomte["tomte<br>(Dev Tooling Library)"]:::devtools
        dev_template["dev-template<br>(open-autonomy Project Template)"]:::devtools
    end

    %% ── Subgraph: On-chain Protocol ─────────────────────────────────────────────
    subgraph ONCHAIN["⛓️ On-chain Protocol"]
        governance_near["governance-near<br>(Governance Contracts on Near)"]:::onchain
        autonolas_subgraph_studio["autonolas-subgraph-studio<br>(Subgraphs Monorepo)"]:::onchain
        tok["autonolas-tokenomics<br>(Tokenomics)"]:::onchain
        stk["autonolas-staking-programmes<br>(Staking)"]:::onchain
        gov["autonolas-governance<br>(OLAS Token & Governance)"]:::onchain
        reg["autonolas-registries<br>(Component / Agent / Service Registry)"]:::onchain
        autonolas_v1["autonolas-v1<br>(Autonolas Protocol v1)"]:::onchain
        mkt["autonolas-marketplace<br>(AI Agent Marketplace)"]:::onchain
        near_reg["registries-near<br>(Near Registries)"]:::onchain
        autonolas_subgraph["autonolas-subgraph<br>(On-chain Data Subgraph)"]:::onchain
        dynamic_contribution["dynamic-contribution<br>(Dynamic Contribution Contracts)"]:::onchain
        registries_solana["registries-solana<br>(Registry Contracts on Solana)"]:::onchain
        lockbox_solana["lockbox-solana<br>(Lockbox Contracts on Solana)"]:::onchain
    end

    %% ── Subgraph: Core Agent Services Framework ────────────────────────────────
    subgraph CORE["🤖 Core Agent Services Framework"]
        open_autonomy["open-autonomy<br>(Autonomous Agent Services Framework)"]:::framework
    end

    %% ── Subgraph: Operations & Middleware ──────────────────────────────────────
    subgraph OPS["⚙️ Operations & Middleware"]
        middleware["olas-operate-middleware<br>(Operate Middleware — Run / Stake / Earn)"]:::operations
        propel_client["propel-client<br>(Valory PaaS Propel Client)"]:::operations
    end

    %% ── Subgraph: Mech Ecosystem ───────────────────────────────────────────────
    subgraph MECH["🔧 Mech Ecosystem"]
        mech_tools_dev["mech-tools-dev<br>(Mech Dev Toolkit)"]:::mecheco
        mech_client["mech-client<br>(Mech Client SDK)"]:::mecheco
        mech_predict["mech-predict<br>(Prediction Mech)"]:::mecheco
        mech_agents_fun["mech-agents-fun<br>(Agents.fun Mech)"]:::mecheco
        mock_mech["mock-mech<br>(Mock Mech for Testing)"]:::mecheco
        mech_marketplace_legacy["mech-marketplace-legacy<br>(v0 Mech Marketplace)"]:::mecheco
        mech["mech<br>(Base Mech Agent)"]:::mecheco
        mech_interact["mech-interact<br>(Mech Interaction Helper)"]:::mecheco
    end

    %% ── Subgraph: AI Agent Services & Applications ─────────────────────────────
    subgraph AGENTS["🧠 AI Agent Services & Applications"]
        eliza_memeooorr_sdk["eliza-memeooorr-olas-sdk<br>(Meme-ooorr via Eliza + Olas SDK)"]:::agent
        market_creator["market-creator<br>(Prediction Market Creator)"]:::agent
        memeooorr["meme-ooorr<br>(Meme Coin Deployer)"]:::agent
        iekit["IEKit<br>(Impact Evaluator Service)"]:::agent
        langchain_trader["langchain-trader<br>(LangChain Trader)"]:::agent
        agents_fun_eliza["agents-fun-eliza<br>(Eliza Framework Agent)"]:::agent
        plugin_memeooorr["plugin-memeooorr<br>(Eliza Plugin for Meme-ooorr)"]:::agent
        pettai["pettai-agent<br>(PettAI Agent)"]:::agent
        optimus["optimus<br>(BabyDegen DeFi Agent)"]:::agent
        hello_world["hello-world<br>(Hello World Example)"]:::agent
        price_oracle["price-oracle<br>(Price Oracle Service)"]:::agent
        trader["trader<br>(Prediction Market Trader)"]:::agent
    end

    %% ── Subgraph: End-User Applications & Quickstarts ──────────────────────────
    subgraph ENDUSER["🖥️ End-User Applications & Quickstarts"]
        pearl["olas-operate-app (Pearl)<br>(Run Agents — Stake & Earn)"]:::enduser
        quickstart["quickstart<br>(Olas Agent Quickstart)"]:::enduser
        triton_bot["triton-bot<br>(Telegram Bot for Staked Olas Services)"]:::enduser
        open_autonomy_client["open-autonomy-client<br>(Autonomous Service Client SDK)"]:::enduser
        olas_sdk_starter["olas-sdk-starter<br>(Olas SDK Starter)"]:::enduser
    end

    %% ── Subgraph: Frontends ────────────────────────────────────────────────────
    subgraph FRONTEND["🌐 Frontends"]
        olas_stats["olas<br>(OLAS Market Statistics Server)"]:::frontend
        frontend_mono["autonolas-frontend-mono<br>(Olas Network Apps Monorepo)"]:::frontend
        agent_ui["agent-ui-monorepo<br>(Agent UI Monorepo)"]:::frontend
        olas_website["olas-website<br>(olas.network Website)"]:::frontend
        valory_website["valory-website<br>(valory.xyz Website)"]:::frontend
        olas_predict_fe["olas-predict<br>(Olas Predict UI)"]:::frontend
    end

    %% ── Subgraph: Documentation ────────────────────────────────────────────────
    subgraph DOCS["📚 Documentation"]
        docs["docs<br>(Olas Ecosystem Docs Aggregator)"]:::docs
    end

    %% ═══════════════════════════════════════════════════════════════════════════
    %% Dependencies
    %% ═══════════════════════════════════════════════════════════════════════════

    %% Core framework builds on open-aea
    open_autonomy -->|<a href="https://github.com/valory-xyz/open-autonomy/blob/main/pyproject.toml#L13" target="_blank">Link</a>| open_aea

    %% open-aea uses open-acn for agent communication
    open_aea -->|<a href="https://github.com/valory-xyz/open-aea/blob/main/packages/packages.json#L19-L21" target="_blank">Link</a>| open_acn

    %% dev-template is a project template for open-autonomy
    dev_template -->|<a href="https://github.com/valory-xyz/dev-template/blob/main/README.md#L3" target="_blank">Link</a>| open_autonomy

    %% On-chain contract hierarchy
    %% autonolas-v1 is a meta-repo that aggregates all on-chain protocol repos as submodules (.gitmodules)
    governance_near -->|<a href="https://github.com/valory-xyz/governance-near/blob/main/README.md#L1" target="_blank">Link</a>| gov
    autonolas_subgraph -->|<a href="https://github.com/valory-xyz/autonolas-subgraph/blob/main/.gitmodules#L1" target="_blank">Link</a>| reg
    autonolas_subgraph_studio -->|<a href="https://github.com/valory-xyz/autonolas-subgraph-studio/blob/main/README.md#L1" target="_blank">Link</a>| autonolas_subgraph
    autonolas_subgraph -->|<a href="https://github.com/valory-xyz/autonolas-subgraph/blob/main/subgraphs/autonolas/subgraph.yaml#L1" target="_blank">Link</a>| tok
    autonolas_v1 -->|<a href="https://github.com/valory-xyz/autonolas-v1/blob/main/.gitmodules#L7" target="_blank">Link</a>| tok
    tok -->|<a href="https://github.com/valory-xyz/autonolas-tokenomics/blob/main/contracts/Tokenomics.sol#L16" target="_blank">Link</a>| gov
    reg -->|<a href="https://github.com/valory-xyz/autonolas-registries/blob/main/contracts/GenericManager.sol#L14" target="_blank">Link</a>| gov
    autonolas_v1 -->|<a href="https://github.com/valory-xyz/autonolas-v1/blob/main/.gitmodules#L16" target="_blank">Link</a>| stk
    stk -->|<a href="https://github.com/valory-xyz/autonolas-staking-programmes/blob/main/contracts/contribute/Contributors.sol#L69" target="_blank">Link</a>| tok
    tok -->|<a href="https://github.com/valory-xyz/autonolas-tokenomics/blob/main/contracts/Tokenomics.sol#L43" target="_blank">Link</a>| reg
    stk -->|<a href="https://github.com/valory-xyz/autonolas-staking-programmes/blob/main/.gitmodules#L1" target="_blank">Link</a>| reg
    autonolas_v1 -->|<a href="https://github.com/valory-xyz/autonolas-v1/blob/main/.gitmodules#L13" target="_blank">Link</a>| mkt
    mkt -->|<a href="https://github.com/valory-xyz/autonolas-marketplace/blob/main/.gitmodules#L1" target="_blank">Link</a>| reg
    autonolas_v1 -->|<a href="https://github.com/valory-xyz/autonolas-v1/blob/main/.gitmodules#L4" target="_blank">Link</a>| reg
    registries_solana -->|<a href="https://github.com/valory-xyz/registries-solana/blob/main/README.md#L1" target="_blank">Link</a>| reg
    dynamic_contribution -->|<a href="https://github.com/valory-xyz/dynamic-contribution/blob/main/contracts/DelegateContribute.sol#L4" target="_blank">Link</a>| reg
    autonolas_v1 -->|<a href="https://github.com/valory-xyz/autonolas-v1/blob/main/.gitmodules#L1" target="_blank">Link</a>| gov

    %% Operations middleware builds on open-autonomy
    middleware -->|<a href="https://github.com/valory-xyz/olas-operate-middleware/blob/main/pyproject.toml#L22" target="_blank">Link</a>| open_autonomy
    %% propel-client depends on open-autonomy directly (pyproject.toml: open-autonomy = "==v0.19.7")
    propel_client -->|<a href="https://github.com/valory-xyz/propel-client/blob/main/pyproject.toml#L14" target="_blank">Link</a>| open_autonomy

    %% Mech ecosystem
    %% open-autonomy packages (via third_party in packages.json)
    mech_tools_dev -->|<a href="https://github.com/valory-xyz/mech-tools-dev/blob/main/pyproject.toml#L55" target="_blank">Link</a>| middleware
    mech_tools_dev -->|<a href="https://github.com/valory-xyz/mech-tools-dev/blob/main/pyproject.toml#L19" target="_blank">Link</a>| open_autonomy
    mech_tools_dev -->|<a href="https://github.com/valory-xyz/mech-tools-dev/blob/main/pyproject.toml#L54" target="_blank">Link</a>| mech_client
    mech_client -->|<a href="https://github.com/valory-xyz/mech-client/blob/main/pyproject.toml#L17" target="_blank">Link</a>| middleware
    mech_predict -->|<a href="https://github.com/valory-xyz/mech-predict/blob/main/packages/packages.json#L55" target="_blank">Link</a>| open_autonomy
    mech_predict -->|<a href="https://github.com/valory-xyz/mech-predict/blob/main/packages/packages.json#L34-L60" target="_blank">Link</a>| mech
    mech_agents_fun -->|<a href="https://github.com/valory-xyz/mech-agents-fun/blob/main/packages/packages.json#L48" target="_blank">Link</a>| open_autonomy
    mech_agents_fun -->|<a href="https://github.com/valory-xyz/mech-agents-fun/blob/main/packages/packages.json#L12-L23" target="_blank">Link</a>| mech
    mock_mech -->|<a href="https://github.com/valory-xyz/mock-mech/blob/main/README.md#L1" target="_blank">Link</a>| open_autonomy
    mech_marketplace_legacy -->|<a href="https://github.com/valory-xyz/mech-marketplace-legacy/blob/main/pyproject.toml#L19" target="_blank">Link</a>| open_autonomy
    mech_tools_dev -->|<a href="https://github.com/valory-xyz/mech-tools-dev/blob/main/packages/packages.json#L8-L36" target="_blank">Link</a>| mech
    mech -->|<a href="https://github.com/valory-xyz/mech/blob/main/packages/packages.json#L42" target="_blank">Link</a>| open_autonomy
    %% mech-interact owns mech_interact_abci skill and depends on mech packages
    mech_interact -->|<a href="https://github.com/valory-xyz/mech-interact/blob/main/packages/packages.json#L41" target="_blank">Link</a>| open_autonomy
    mech_interact -->|<a href="https://github.com/valory-xyz/mech-interact/blob/main/packages/packages.json#L22" target="_blank">Link</a>| mech

    %% eliza-memeooorr-olas-sdk is based on olas-sdk-starter (empty packages.json; README is olas-sdk-starter template)
    eliza_memeooorr_sdk -->|<a href="https://github.com/valory-xyz/eliza-memeooorr-olas-sdk/blob/main/packages/packages.json" target="_blank">Link</a>| olas_sdk_starter

    %% AI Agent Services build on open-autonomy (via third_party in packages.json)
    market_creator -->|<a href="https://github.com/valory-xyz/market-creator/blob/main/packages/packages.json#L57" target="_blank">Link</a>| mech_interact
    market_creator -->|<a href="https://github.com/valory-xyz/market-creator/blob/main/packages/packages.json#L20" target="_blank">Link</a>| mech
    market_creator -->|<a href="https://github.com/valory-xyz/market-creator/blob/main/packages/packages.json#L52" target="_blank">Link</a>| open_autonomy
    memeooorr -->|<a href="https://github.com/valory-xyz/meme-ooorr/blob/main/packages/packages.json#L65" target="_blank">Link</a>| mech_interact
    memeooorr -->|<a href="https://github.com/valory-xyz/meme-ooorr/blob/main/packages/packages.json#L24" target="_blank">Link</a>| mech
    memeooorr -->|<a href="https://github.com/valory-xyz/meme-ooorr/blob/main/packages/packages.json#L62" target="_blank">Link</a>| open_autonomy
    iekit -->|<a href="https://github.com/valory-xyz/IEKit/blob/main/packages/packages.json#L75" target="_blank">Link</a>| mech_interact
    iekit -->|<a href="https://github.com/valory-xyz/IEKit/blob/main/packages/packages.json#L42" target="_blank">Link</a>| mech
    iekit -->|<a href="https://github.com/valory-xyz/IEKit/blob/main/packages/packages.json#L72" target="_blank">Link</a>| open_autonomy
    langchain_trader -->|<a href="https://github.com/valory-xyz/langchain-trader/blob/master/packages/packages.json#L35" target="_blank">Link</a>| mech_interact
    langchain_trader -->|<a href="https://github.com/valory-xyz/langchain-trader/blob/master/packages/packages.json#L32" target="_blank">Link</a>| open_autonomy
    hello_world -->|<a href="https://github.com/valory-xyz/hello-world/blob/main/packages/packages.json#L23" target="_blank">Link</a>| open_autonomy
    agents_fun_eliza -->|<a href="https://github.com/valory-xyz/agents-fun-eliza/blob/main/packages/packages.json#L3" target="_blank">Link</a>| open_autonomy
    agents_fun_eliza -->|<a href="https://github.com/valory-xyz/plugin-memeooorr/blob/main/README.md#L1" target="_blank">Link</a>| plugin_memeooorr
    price_oracle -->|<a href="https://github.com/valory-xyz/price-oracle/blob/main/packages/packages.json#L30" target="_blank">Link</a>| open_autonomy
    optimus -->|<a href="https://github.com/valory-xyz/optimus/blob/main/packages/packages.json#L62" target="_blank">Link</a>| open_autonomy
    pettai -->|<a href="https://github.com/valory-xyz/pettai-agent/blob/main/olas-sdk-starter/packages/packages.json#L3" target="_blank">Link</a>| open_autonomy
    trader -->|<a href="https://github.com/valory-xyz/trader/blob/main/packages/packages.json#L76" target="_blank">Link</a>| mech_interact
    trader -->|<a href="https://github.com/valory-xyz/trader/blob/main/packages/packages.json#L31" target="_blank">Link</a>| mech
    trader -->|<a href="https://github.com/valory-xyz/trader/blob/main/packages/packages.json#L71" target="_blank">Link</a>| open_autonomy

    %% End-user apps
    pearl -->|<a href="https://github.com/valory-xyz/olas-operate-app/blob/main/pyproject.toml#L13" target="_blank">Link</a>| middleware
    quickstart -->|<a href="https://github.com/valory-xyz/quickstart/blob/main/pyproject.toml#L13" target="_blank">Link</a>| middleware
    triton_bot -->|<a href="https://github.com/valory-xyz/triton-bot/blob/main/pyproject.toml#L12" target="_blank">Link</a>| middleware
    triton_bot -->|<a href="https://github.com/valory-xyz/triton-bot/blob/main/README.md" target="_blank">Link</a>| quickstart
    olas_sdk_starter -->|<a href="https://github.com/valory-xyz/olas-sdk-starter/blob/main/README.md#L3" target="_blank">Link</a>| open_autonomy
    open_autonomy_client -->|<a href="https://github.com/valory-xyz/open-autonomy-client/blob/main/README.md#L1" target="_blank">Link</a>| open_autonomy

    %% Frontends
    frontend_mono -->|<a href="https://github.com/valory-xyz/autonolas-frontend-mono" target="_blank">Link</a>| olas_predict_fe
    %% olas-predict is the UI for the trader service and queries autonolas-subgraph via GraphQL
    olas_predict_fe -->|<a href="https://github.com/valory-xyz/olas-predict/tree/main/pages" target="_blank">Link</a>| trader
    olas_predict_fe -->|<a href="https://github.com/valory-xyz/olas-predict/blob/main/.env.example#L1-L3" target="_blank">Link</a>| autonolas_subgraph

    %% Documentation aggregates submodules (see docs/.gitmodules)
    docs -->|<a href="https://github.com/valory-xyz/docs/blob/main/.gitmodules#L7" target="_blank">Link</a>| open_acn
    docs -->|<a href="https://github.com/valory-xyz/docs/blob/main/.gitmodules#L1" target="_blank">Link</a>| open_aea
    docs -->|<a href="https://github.com/valory-xyz/docs/blob/main/.gitmodules#L13" target="_blank">Link</a>| mech_tools_dev
    docs -->|<a href="https://github.com/valory-xyz/docs/blob/main/.gitmodules#L16" target="_blank">Link</a>| mech_client
    docs -->|<a href="https://github.com/valory-xyz/docs/blob/main/.gitmodules#L10" target="_blank">Link</a>| mech
    docs -->|<a href="https://github.com/valory-xyz/docs/blob/main/.gitmodules#L4" target="_blank">Link</a>| open_autonomy
    docs -->|<a href="https://github.com/valory-xyz/docs/blob/main/.gitmodules#L19" target="_blank">Link</a>| price_oracle
    docs -->|<a href="https://github.com/valory-xyz/docs/blob/main/.gitmodules#L22" target="_blank">Link</a>| iekit
    docs -->|<a href="https://github.com/valory-xyz/docs/blob/main/.gitmodules#L25" target="_blank">Link</a>| hello_world

    %% ═══════════════════════════════════════════════════════════════════════════
    %% Repositories in the valory-xyz GitHub org NOT included in this diagram
    %% (❌ = archived; others are standalone, experimental, event-specific, or docs-only)
    %%  academy-learning-service             — Academy learning service (no public deps)
    %%  academy-learning-service-template    — Template for the academy learning service
    %%  academy-solutions                    — Academy exercise solutions
    %%  aea-babyagi                          — BabyAGI adaptation in Open AEA (standalone demo)
    %%  agent-academy-1                   ❌ — Agent Academy 1 participant repo
    %%  agent-academy-2                   ❌ — Agent Academy 2 participant repo
    %%  agent-stats                       ❌ — Agent statistics & parameters (JS tool)
    %%  ai-mech                           ❌ — AI Mech (predecessor to mech)
    %%  ai-registry-mech-frontend         ❌ — AI Mech Registry dApp
    %%  ai-registry-mech-graph            ❌ — AI registry mech graph (TypeScript tool)
    %%  airdrop-helper                       — Olas ecosystem participation measurement tool
    %%  apy-oracle                        ❌ — APY Oracle Service (agent service)
    %%  autonolas-aip                        — Autonolas Improvement Proposals (docs only)
    %%  autonolas-build-frontend          ❌ — build.olas.network frontend
    %%  autonolas-contribution-service-frontend ❌ — Contribution dApp
    %%  autonolas-frontend-library        ❌ — Autonolas frontend component library
    %%  autonolas-frontend-template       ❌ — Autonolas frontend template
    %%  autonolas-launch-frontend         ❌ — Autonolas launch frontend
    %%  autonolas-member-frontend         ❌ — member.olas.network frontend
    %%  autonolas-operate-frontend        ❌ — Operate dApp
    %%  autonolas-registry-frontend       ❌ — Registry dApp
    %%  autonolas-tokenomics-frontend     ❌ — Tokenomics dApp
    %%  autonolas-tokenomics-solana       ❌ — Solana Tokenomics contracts
    %%  autonolas-website                 ❌ — autonolas.network website
    %%  autonomous-fund                   ❌ — Autonomous Fund Manager (agent service)
    %%  celo-trader                       ❌ — Celo Trader agent
    %%  ceramic-py                        ❌ — Simple Ceramic Network Python client
    %%  co-owned-ai-website                  — co-owned.ai website
    %%  community-nfts                    ❌ — Community NFT contracts
    %%  contract-utils                    ❌ — Contract utilities
    %%  contracts-amm                     ❌ — AMM contracts
    %%  contracts-aks                     ❌ — Autonomous Keeper Service job registry
    %%  contribution-service              ❌ — Dynamic NFT Contribution Service (agent service)
    %%  decentralized-watchtower          ❌ — Decentralized watchtower service
    %%  dkg-predictions                   ❌ — DKG example on OriginTrail
    %%  el-collectooorr-frontend          ❌ — El Collectooorr front-end
    %%  elcollectooorr-contracts          ❌ — El Collectooorr smart contracts
    %%  erc20-token-bridge                ❌ — ERC-20 token bridge
    %%  eth-lisbon-23                     ❌ — ETH Lisbon 2023 hack (Shorts.wtf)
    %%  ethlisbon                         ❌ — ETH Lisbon ArtBlocks NFT agent
    %%  ethereum-optimism.github.io          — Fork of Optimism token list
    %%  generatooorr                      ❌ — Generatooorr agent service
    %%  gnosis-mech                       ❌ — Copy of gnosis/mech (original deleted)
    %%  governatooorr                     ❌ — AI Governance Delegate (agent service)
    %%  governatooorr-frontend            ❌ — governatooorr.autonolas.network frontend
    %%  governatooorr-solana              ❌ — Governatooorr on Solana
    %%  legacy-lockbox-solana             ❌ — Legacy Solana lockbox contracts
    %%  liquidity-rebalancing             ❌ — Liquidity rebalancing agent
    %%  mech-eth-lisbon-2023              ❌ — Shorts.wtf smart contracts (ETH Lisbon 2023)
    %%  mech-ethdenver-2024               ❌ — Mech extension for ETH Denver 2024
    %%  mech-offchain-eth-lisbon-2023     ❌ — Off-chain mech for ETH Lisbon 2023
    %%  mech-predict-markets              ❌ — Mech predict markets
    %%  mech-quickstart                   ❌ — Mech Quickstart
    %%  mech-tool-template                ❌ — Template for authoring new mech tools
    %%  modius-quickstart                 ❌ — Modius/DeFi Agent Quickstart
    %%  olas-predict-benchmark            ❌ — Olas Predict benchmark of Mech tools
    %%  open-operator-aks                 ❌ — Deploy Autonomous Keeper Agent on AWS
    %%  open-operator-watchtower          ❌ — Open operator watchtower
    %%  optimus-quickstart                ❌ — Optimus Quickstart
    %%  prediction-markets                ❌ — Prediction Markets Demo Monorepo
    %%  press-kit-valory                     — Valory brand guidelines / press kit
    %%  santa-nft                         ❌ — Valory Santa NFT 2021
    %%  scripts                           ❌ — Internal scripts
    %%  shorts-frontend                   ❌ — Shorts.wtf frontend (ETH Lisbon 2023)
    %%  solana-sandbox                    ❌ — Solana sandbox / experiments
    %%  test-deployment-envs              ❌ — Internal test deployment environments
    %%  trader-quickstart                 ❌ — Trader Quickstart
    %%  ZK-ML-Verifier                    ❌ — ZK-ML Verification Service (agent service)
    %% ═══════════════════════════════════════════════════════════════════════════
```