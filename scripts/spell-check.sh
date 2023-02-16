#!/bin/bash
# This script requires `mdspell`:
#
#    https://www.npmjs.com/package/markdown-spellcheck
#
# Run this script from the root directory.
# Usage:
#   ./scripts/spell-check.sh
#

MDSPELL_PATH="$(which mdspell)"
if [ -z "${MDSPELL_PATH}" ]; then
  echo "Cannot find executable 'mdspell'. Please install it to run this script: npm i markdown-spellcheck -g"
  exit 127
else
  echo "Found 'mdspell' executable at ${MDSPELL_PATH}"
  mdspell -r -n -a --en-gb 'docs/**/*.md' '!agent-academy-1/**/*.md' '!apy-oracle/**/*.md' '!autonomous-fund/**/*.md' '!contribution-service/**/*.md' '!open-autonomy/**/*.md' '!price-oracle/**/*.md'
fi
