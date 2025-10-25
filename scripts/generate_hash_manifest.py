#!/usr/bin/env python3
"""
Auto-generate SHA256 hash manifests for the keep4o-research repo.

 • Scans all files (except >100 MB) in the directories listed in INCLUDE_DIRS.
 • Writes:
     metadata/hash_manifest.json   – machine-readable map  {relative path: sha256}
     metadata/hash_manifest.md     – human-readable table  | file | sha256 |
"""

import os, hashlib, json, argparse, datetime

# ── Adjust these paths to whatever you want hashed in *research* ──
INCLUDE_DIRS = [
    "papers",        # PDFs, LaTeX, Markdown drafts
    "figures",       # PNG / SVG / Mermaid source
    "analysis",      # scripts, notebooks, csv outputs
    "timeline",      # monthly timeline markdown / csv
    "docs",          # quickstart, ethics, FAQ
]

# Hash files larger than this?  (100 MB default skip)
LARGE_FILE_SKIP = 100 * 1024 * 1024

# Output locations
OUTPUT_JSON = "metadata/hash_manifest.json"
OUTPUT_MD   = "metadata/hash_manifest.md"


# ──────────────────────────────────────────────────────────────────
def sha256_of(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def iter_files(dirs):
    for d in dirs:
        if not os.path.exists(d):
            continue
        for root, _, files in os.walk(d):
            for fname in files:
                full = os.path.join(root, fname)
                yield os.path.relpath(full, ".")


def main():
    manifest = {}
    for rel in iter_files(INCLUDE_DIRS):
        if os.path.getsize(rel) > LARGE_FILE_SKIP:
            continue                              # skip giant binaries
        manifest[rel] = sha256_of(rel)

    # ensure metadata/ exists
    os.makedirs(os.path.dirname(OUTPUT_JSON), exist_ok=True)

    # JSON
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)
    print(f"Wrote {OUTPUT_JSON} ({len(manifest)} files)")

    # Markdown
    with open(OUTPUT_MD, "w", encoding="utf-8") as f:
        f.write("# Hash Manifest (auto-generated)\n")
        f.write(f"*Generated*: {datetime.datetime.utcnow().isoformat()}Z\n\n")
        f.write("| File | SHA256 hash |\n|---|---|\n")
        for rel, h in manifest.items():
            f.write(f"| {rel} | {h} |\n")
    print(f"Wrote {OUTPUT_MD}")


if __name__ == "__main__":
    main()
