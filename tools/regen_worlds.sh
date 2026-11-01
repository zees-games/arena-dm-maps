#!/bin/bash
# Rebuild worlds/<id> through the shared converter; sources go in sources/ (git-ignored).
exec "${DOTBSP_PATH:-$(dirname "$0")/../../dot-map-convert}/tools/regen_worlds.sh" "$(dirname "$0")/.." "$@"
