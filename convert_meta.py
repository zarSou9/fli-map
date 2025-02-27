import json
from pathlib import Path

from convert_from_directories import convert_markdown_to_html


def main():
    meta = json.loads(Path("meta.json").read_text(encoding="utf-8"))
    for section in ["note", "cover_root_description"]:
        if meta.get(section):
            meta[section] = convert_markdown_to_html(meta[section])

    Path("meta-converted.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
