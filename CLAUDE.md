# arena-dm-maps

Deathmatch and gun game maps for game-arena, a sibling of arena-surf-dm-maps. Read `../../CLAUDE.md`, `../game-arena/CLAUDE.md`, game-arena's `docs/imported-maps.md` and `../arena-surf-dm-maps/CLAUDE.md`: the layout, pack-per-map rule, `provides.json` per map and tag-to-release flow are the same.

Maps come from the 16 GameBanana mods in nightly item `map-suggestions-1`; the conversion is `maps-conv-arena-dm-1`. They go through the global importer in dot-map, never per-map patches. Every map needs an author and a source page in `maps.json` and the README table. Skip any map whose author forbids sharing or whose licence is outside the art rules.

**Map content is not in git** (`/maps/*` is ignored): it is delivered through the CDN publish flow. What is committed is `maps.json`, the README credits, `zones/<id>.json` (the importer's attribution and `kind` per map, passed with `--zones-dir`) and `tools/`. Import: `python3 ../game-g2gfast/tools/bsp_import.py <bsp> maps --id <id> --zones-dir zones`.
