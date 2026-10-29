# arena-dm-maps

Deathmatch and gun game maps [game-arena](https://github.com/zees-games/game-arena) plays, as a repository of their own: the imported maps in `maps/` and the list of them with their authors in `maps.json`.

Every map here is somebody else's work, imported so it can be played again, and credited in `maps.json`, below and on screen whenever a server changes to it. If you made one of these maps and want it credited differently or taken down, open an issue and it will be done.

Each map is its own signed pack, `gamemann/<map id>`, released by tagging this repository (see `.github/workflows/release.yml`). `maps/` is linked at game-arena's `maps/imported_dm` (a `# bootstrap-link:` line in its `.gitignore`), beside the surf maps; `headless_dm_maps` checks them.

## Credits

All sixteen are GameBanana uploads under the site's default licence, CC BY-NC-ND 4.0, credited here with the author and source page. They are published under the credited-community-map exception (`licence.json`), with this credit, the link and the removal offer.

| Map | Author | Source |
| --- | --- | --- |
| `aim_forts` | NoBuxs | https://gamebanana.com/mods/116937 |
| `blackhawkdown` | Cc_NIPPER | https://gamebanana.com/mods/116994 |
| `dm_hot_cn_v1` | seigneurdesombres | https://gamebanana.com/mods/117417 |
| `dm_industrial_gamma` | warhawk3407 | https://gamebanana.com/mods/117427 |
| `dm_morpheus` | mr-thermaltake | https://gamebanana.com/mods/117486 |
| `dm_overwatch` | LikeMike213 | https://gamebanana.com/mods/117534 |
| `dm_scarletdevilmansion` | Deity Link | https://gamebanana.com/mods/117571 |
| `gg_canyon` | Devi8 | https://gamebanana.com/mods/134054 |
| `gg_fy_snow` | s1nk0 | https://gamebanana.com/mods/135022 |
| `gg_garage` | SGT_kick_ur_ass | https://gamebanana.com/mods/135049 |
| `gg_krusty_krab` | FireWavezZ | https://gamebanana.com/mods/135508 |
| `gg_lego_arena` | Jevan | https://gamebanana.com/mods/135558 |
| `gg_punishment` | Karatekaefer | https://gamebanana.com/mods/136211 |
| `gg_simpsons_x` | BasicAir | https://gamebanana.com/mods/136613 |
| `gg_woods` | X-tr3m3r | https://gamebanana.com/mods/137426 |
| `welcometomexicov6` | zaki90 | https://gamebanana.com/mods/117984 |

## Naming them on a server

A server offers them when its `cfg/server/content/overrides.yml` names them under `game-arena` (dot-server-deploy's `cfg.example` does, so a new box has them), one line per map in `maps.json`. All sixteen are on the development CDN at 1.0.1; production has only `blackhawkdown` and `welcometomexicov6` so far.

The map files are not in git. `content.lock.json` pins each map's pack (kind `store`, `into: maps/<id>`), so `../dot-bootstrap/bootstrap.sh` (or `./fetch-content.sh` here) fills `maps/` and with it game-arena's `maps/imported_dm`.

```yaml
games:
  game-arena:
    maps:
      add:
        - gamemann/aim_forts
        - gamemann/blackhawkdown
        - gamemann/dm_hot_cn_v1
        - gamemann/dm_industrial_gamma
        - gamemann/dm_morpheus
        - gamemann/dm_overwatch
        - gamemann/dm_scarletdevilmansion
        - gamemann/gg_canyon
        - gamemann/gg_fy_snow
        - gamemann/gg_garage
        - gamemann/gg_krusty_krab
        - gamemann/gg_lego_arena
        - gamemann/gg_punishment
        - gamemann/gg_simpsons_x
        - gamemann/gg_woods
        - gamemann/welcometomexicov6
```
