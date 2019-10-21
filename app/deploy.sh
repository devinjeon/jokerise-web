#!/usr/bin/env bash
set -euo pipefail

npm run lint
npm run build

gsutil rsync -R ./dist/ gs://"$(cat ./custom_domain)"
