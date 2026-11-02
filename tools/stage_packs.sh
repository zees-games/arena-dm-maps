#!/bin/bash
# stage_packs.sh OUT [id...] : one directory per map = maps/<id>/ plus worlds/<id>/ with the library models it draws in worlds/<id>/models/.
# A delivered pack has no model-library beside it, so without the bundle every library prop is a box or missing.
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="${1:?usage: stage_packs.sh OUT [id...]}"; shift
CONVERT="${DOT_MAP_CONVERT:-$HERE/../dot-map-convert}"
IDS=("$@"); [ ${#IDS[@]} -gt 0 ] || mapfile -t IDS < <(cd "$HERE/worlds" && ls)
for id in "${IDS[@]}"; do
    [ -d "$HERE/worlds/$id" ] || { echo "no world for $id, skipped" >&2; continue; }
    rm -rf "${OUT:?}/$id"; mkdir -p "$OUT/$id/worlds"
    [ -d "$HERE/maps/$id" ] && cp -r "$HERE/maps/$id/." "$OUT/$id/"
    python3 -I "$CONVERT/bsp.py" bundle "$HERE/worlds/$id" --out "$OUT/$id/worlds" --strict
done
