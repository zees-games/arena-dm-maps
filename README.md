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
