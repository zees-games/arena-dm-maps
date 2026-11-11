"""pack_licence.py PACKDIR ID REPO : make PACKDIR/licence.json carry the credit and licence the repo records for map ID.

The pack's licence.json is copied from the derived maps/<id>/ directory, which the converter's `store` step wrote with
"none stated" for a map whose credit it could not read. The repo's licence.json (one entry per maps/<id>) is the owner-approved
record, so its licence, exception, title, author and source_url replace the map entry of the pack file; the root entry
(the repo's own MIT content) is kept. A map with no repo entry is left as it is.
"""
import json
import os
import sys

FIELDS = ("licence", "exception", "title", "author", "source_url")


def merge(pack_entries, repo_entries, pid):
    """(entries, found): pack_entries with the map entry of pid overlaid by the repo's entry for maps/<pid>."""
    src = next((e for e in repo_entries if "maps/" + pid in e.get("paths", [])), None)
    if src is None:
        return pack_entries, False
    out, hit = [], False
    for e in pack_entries:
        if pid in e.get("paths", []):
            e = dict(e)
            e.update({k: src[k] for k in FIELDS if k in src})
            hit = True
        out.append(e)
    if not hit:
        e = {k: src[k] for k in FIELDS if k in src}
        e["paths"] = [pid, "textures/", "worlds/"]
        e["removal_contact"] = src.get("removal_contact", "")
        out.append(e)
    return out, True


def main(argv):
    pack, pid, repo = argv[1:4]
    with open(os.path.join(repo, "licence.json"), encoding="utf-8") as f:
        repo_entries = json.load(f)
    path = os.path.join(pack, "licence.json")
    cur = []
    if os.path.isfile(path):
        with open(path, encoding="utf-8") as f:
            cur = json.load(f)
    out, found = merge(cur, repo_entries, pid)
    if found:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(out, f, indent=2)
            f.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
