#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(dirname "${BASH_SOURCE[0]}")"
cd "$SCRIPT_DIR" || exit 1

npm run lint
npm run build

# shellcheck disable=SC2086
gsutil rsync -R "$SCRIPT_DIR/dist/" gs://"$(cat $SCRIPT_DIR/custom_domain)"
