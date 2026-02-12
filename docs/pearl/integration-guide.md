# Pearl Integration Guide

This guide explains how to add your agent blueprint to Pearl App, allowing users to run your autonomous agents.

## Overview

Pearl is a desktop application that allows users to run autonomous agents powered by the Olas protocol. To make your agent blueprint available in Pearl, you need to follow the integration process outlined below.

## Prerequisites

Before contacting the Pearl team, ensure you have completed:

1. **Built your agent blueprint** following the [Olas SDK requirements](../olas-sdk/index.md#step-1-build-the-agent-blueprint-supporting-the-following-requirements)
2. **Built the binaries** as standalone executables following the [binary building process](../olas-sdk/index.md#1-build-the-binaries)
3. **Prepared the GitHub workflow file** to build standalone binary executables following the [workflow preparation guide](../olas-sdk/index.md#2-prepare-the-github-workflow-file)

## Request Integration

**Reach out to the Pearl team to request the addition of your agent blueprint to the Pearl App.**

When reaching out, please provide:

- Link to your agent blueprint repository
- Link to your binary releases
- Agent blueprint details (name, description, capabilities)
- Any specific configuration requirements

## Testing Your Agent Locally (For Integrated Teams)

If you're already integrated with Pearl and want to test updates to your agent locally without requesting a dev version, follow these steps:

1. **Fork and setup Pearl**: Fork the [Pearl repository](https://github.com/valory-xyz/olas-operate-app), follow the _README_ guide for setup (specifically, [this section](https://github.com/valory-xyz/olas-operate-app/blob/main/README.md#for-developers)), and run it locally. You may use Tenderly RPC for the needed chain in environment variables or any public RPC.

2. **Release your agent updates**: Implement any necessary modifications to your agent and release it in your own repository, providing the binary, release version, and hash.

3. **Update your Pearl fork**: Update the code in your Pearl fork with the new version and hash (if required) following [this instruction](https://github.com/valory-xyz/olas-operate-app/blob/main/README.md#customizing-the-service-hash), run the agent from Pearl locally, and conduct testing on your own.

4. **Submit for review**: If the outcome is satisfactory, notify the Pearl team in the relevant channel. The team will conduct an audit, create a new version in their fork of your agent, integrate it into Pearl, perform testing, and proceed with the release.

## Support

For questions or issues regarding Pearl integration, reach out on [Discord](https://discord.com/invite/z2PT65jKqQ).
