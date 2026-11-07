# arena-dm-maps

Deathmatch and gun game maps [game-arena](https://github.com/zees-games/game-arena) plays, as a repository of their own: the imported maps in `maps/` and the list of them with their authors in `maps.json`.

Every map here is somebody else's work, imported so it can be played again, and credited in `maps.json`, below and on screen whenever a server changes to it. If you made one of these maps and want it credited differently or taken down, open an issue and it will be done.

Each map is its own signed pack, `gamemann/<map id>`, released by tagging this repository (see `.github/workflows/release.yml`). `maps/` is linked at game-arena's `maps/imported_dm` (a `# bootstrap-link:` line in its `.gitignore`), beside the surf maps; `headless_dm_maps` checks them.

## Credits

All sixteen are GameBanana uploads under the site's default licence, CC BY-NC-ND 4.0, credited here with the author and source page. They are published under the credited-community-map exception (`licence.json`), with this credit, the link and the removal offer.

| Map | Author | Source |
| --- | --- | --- |
| `aim-forts` | NoBuxs | https://gamebanana.com/mods/116937 |
| `blackhawkdown` | Cc_NIPPER | https://gamebanana.com/mods/116994 |
| `crackhouse` | unknown (no readme in the archive; published with credit and a removal offer) | user-supplied archive |
| `dm-hot-cn-v1` | seigneurdesombres | https://gamebanana.com/mods/117417 |
| `dm-industrial-gamma` | warhawk3407 | https://gamebanana.com/mods/117427 |
| `dm-morpheus` | mr-thermaltake | https://gamebanana.com/mods/117486 |
| `dm-overwatch` | LikeMike213 | https://gamebanana.com/mods/117534 |
| `dm-scarletdevilmansion` | Deity Link | https://gamebanana.com/mods/117571 |
| `gg-canyon` | Devi8 | https://gamebanana.com/mods/134054 |
| `gg-fy-snow` | s1nk0 | https://gamebanana.com/mods/135022 |
| `gg-garage` | SGT_kick_ur_ass | https://gamebanana.com/mods/135049 |
| `gg-krusty-krab` | FireWavezZ | https://gamebanana.com/mods/135508 |
| `gg-lego-arena` | Jevan | https://gamebanana.com/mods/135558 |
| `gg-punishment` | Karatekaefer | https://gamebanana.com/mods/136211 |
| `gg-simpsons-x` | BasicAir | https://gamebanana.com/mods/136613 |
| `gg-woods` | X-tr3m3r | https://gamebanana.com/mods/137426 |
| `welcometomexicov6` | zaki90 | https://gamebanana.com/mods/117984 |

## cp_orange_x3 (not published)

`cp-orange-x3` is a commercial control point map, imported for deathmatch, team deathmatch and capture the flag. It is commercial content used by the owner's decision: it is **not** in `licence.json`, not in `content.lock.json`, never published to a CDN, and its converted files stay out of git like the rest. Its source BSP lives in `sources/` (git-ignored). The importer keeps what the original map says: its team spawns (teams 2 and 3) become `red` and `blue` spawns, the five control points and the resupply volumes are kept as `control_points` and `resupply` in the manifest, and `zones/cp-orange-x3.json` authors a `flag_spawns` marker at each side's last control point. Textures the pakfile does not carry fall back to the free PBR library or flat colour.

## Which maps host which modes

A map's manifest carries `modes` (from `zones/<id>.json`, mirrored in `maps.json`): the mode ids it can host. Without the list a map hosts the modes its spawns allow (free-for-all and gun game; a team mode needs tagged spawns), and an imported map hosts no objective mode. With it, `ArenaMaps.supports_mode` answers from the list, so a map only offers a mode it is big enough for.

| Map | Modes |
| --- | --- |
| `cp-orange-x3` | `ffa`, `gungame`, `snipers`, `tdm`, `ctf` (about 100 by 130 m, two bases 70 m apart) |
| the sixteen above | free-for-all and gun game (no team spawns, too small for flags) |

The size rule for `ctf`: both bases need their own spawn block and a flag home, and the walk between the flags should take over 20 seconds at run speed, so roughly 60 m between homes. The stock `dm_` maps and the sixteen above are below that.

## Naming them on a server

A server offers them when its `cfg/server/content/overrides.yml` names them under `game-arena` (dot-server-deploy's `cfg.example` does, so a new box has them), one line per map in `maps.json`. All sixteen are on the production CDN (the fourteen hyphenated ids at 1.0.3, `blackhawkdown` and `welcometomexicov6` at 1.0.1). Ids are hyphenated because the production site refuses an underscore in the repo segment.

The map files are not in git. `content.lock.json` pins each map's pack (kind `store`, `into: maps/<id>`), so `../dot-bootstrap/bootstrap.sh` (or `./fetch-content.sh` here) fills `maps/` and with it game-arena's `maps/imported_dm`.

```yaml
games:
  game-arena:
    maps:
      add:
        - gamemann/aim-forts
        - gamemann/blackhawkdown
        - gamemann/dm-hot-cn-v1
        - gamemann/dm-industrial-gamma
        - gamemann/dm-morpheus
        - gamemann/dm-overwatch
        - gamemann/dm-scarletdevilmansion
        - gamemann/gg-canyon
        - gamemann/gg-fy-snow
        - gamemann/gg-garage
        - gamemann/gg-krusty-krab
        - gamemann/gg-lego-arena
        - gamemann/gg-punishment
        - gamemann/gg-simpsons-x
        - gamemann/gg-woods
        - gamemann/welcometomexicov6
```
