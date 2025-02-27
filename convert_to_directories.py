import json
import re
from pathlib import Path


def get_node_id_idxs(node_id: str, only_node_ids: bool = True) -> list[int]:
    idxs = []
    in_closure = None
    for char in node_id[1:]:
        if in_closure is not None:
            if char == ".":
                idxs.append(int(in_closure))
                in_closure = None
            else:
                in_closure += char
        else:
            if char == ".":
                in_closure = ""
            else:
                idxs.append(int(char))

    return [idx for i, idx in enumerate(idxs) if not only_node_ids or i % 2 != 0]


def get_node_from_id(node_id: str | None, root: dict | None) -> dict | None:
    if not root or not node_id:
        return

    current_node = root
    for idx in get_node_id_idxs(node_id):
        if not current_node or not current_node.get("breakdowns"):
            return
        if idx >= len(current_node["breakdowns"][0]["sub_nodes"]):
            return
        current_node = current_node["breakdowns"][0]["sub_nodes"][idx]

    return current_node


def sanitize_filename(name):
    """Convert a string to a valid filename by removing invalid characters."""
    # Replace spaces with underscores and remove other invalid characters
    return re.sub(r"[^\w\-\.]", "_", name.replace(" ", "_"))


def convert_html_to_markdown(text, convert=True):
    if not text:
        return text
    pattern = (
        r"<a\s+href=['\"]([^'\"]+)['\"](?:\s+target=['\"][^'\"]*['\"])?\s*>([^<]+)</a>"
    )
    markdown_text = re.sub(pattern, r"[\2](\1)", text)
    # Remove spaces before or after <br> tags
    markdown_text = re.sub(r"\s*<br\s*\/?>\s*", "<br>", markdown_text)
    markdown_text = re.sub(r"<br\s*\/?>", "\n", markdown_text)

    markdown_text = re.sub(r"(\S)<i>", r"\1 <i>", markdown_text)
    markdown_text = re.sub(r"</i>(\S)", r"</i> \1", markdown_text)
    markdown_text = re.sub(
        r"<i>\s*(.*?)\s*</i>", lambda m: f"*{m.group(1).strip()}*", markdown_text
    )

    return markdown_text


def get_node_path(node_id: str, root: dict) -> str | None:
    """Convert a node ID to its path in the tree structure."""
    # First, we need to build the complete path from root to the node
    path_parts = []

    # Start with the root node
    if not root or "title" not in root:
        return None

    # Parse the node ID to get the sequence of indices
    indices = get_node_id_idxs(node_id)
    if not indices:
        return None

    # Start with the root node
    current_node = root
    path_parts.append(sanitize_filename(current_node.get("title", "Root")))

    # Follow the path through the tree
    for idx in indices:
        if (
            not current_node
            or not current_node.get("breakdowns")
            or not current_node["breakdowns"][0].get("sub_nodes")
            or idx >= len(current_node["breakdowns"][0]["sub_nodes"])
        ):
            return None

        # Move to the next node in the path
        current_node = current_node["breakdowns"][0]["sub_nodes"][idx]
        if "title" in current_node:
            path_parts.append(sanitize_filename(current_node["title"]))

    return "/".join(path_parts) if path_parts else None


def get_node_title(node_id: str, root: dict) -> str | None:
    """Get the title of a node from its ID."""
    node = get_node_from_id(node_id, root)
    if node and "title" in node:
        return node["title"]
    return None


def convert_links_to_paths(links: list, root: dict) -> list:
    """Convert link IDs to paths in the tree structure."""
    converted_links = []
    for link in links:
        new_link = link.copy()
        if "id" in new_link:
            path = get_node_path(new_link["id"], root)
            title = get_node_title(new_link["id"], root)

            if path:
                dir_name = path.split("/")[-1]
                new_link["path"] = f"{path}/{dir_name}.md"
                if title:
                    new_link["title"] = title
                del new_link["id"]
            else:
                # Keep the ID if path couldn't be resolved
                new_link["path"] = f"Unknown path (ID: {new_link['id']})"
                new_link["title"] = "Unknown Node"
                del new_link["id"]
        converted_links.append(new_link)
    return converted_links


def create_directory_structure(node, root, parent_path=Path(), convert_html=False):
    """Recursively create directories and files for each node."""
    node_title = node.get("title", "Untitled")

    dir_name = sanitize_filename(node_title)
    dir_path = parent_path / dir_name

    dir_path.mkdir(exist_ok=True, parents=True)

    content = ""

    mini_description = node.get("mini_description", "")
    if mini_description:
        content += "### Mini Description\n\n"
        content += f"{convert_html_to_markdown(mini_description, convert_html)}\n\n"

    description = node.get("description", "")
    if description:
        content += "### Description\n\n"
        content += f"{convert_html_to_markdown(description, convert_html)}\n\n"

    links = node.get("links", [])
    if links:
        converted_links = convert_links_to_paths(links, root)
        content += "### Related Nodes\n\n"

        for link in converted_links:
            path = link.get("path", "")
            title = link.get("title", path)

            content += f"- [{title}](/{path})\n"

            if "reason" in link and link["reason"]:
                content += f"\t- Reason: {link['reason']}\n"

        content += "\n"

    (dir_path / f"{dir_name}.md").write_text(content.strip() + "\n", encoding="utf-8")

    if "breakdowns" in node and node["breakdowns"]:
        breakdown = node["breakdowns"][0]
        if "sub_nodes" in breakdown:
            for sub_node in breakdown["sub_nodes"]:
                create_directory_structure(sub_node, root, dir_path, convert_html)


def main():
    json_file = Path("fli-map.json")

    try:
        data = json.loads(json_file.read_text(encoding="utf-8"))
    except FileNotFoundError:
        print("Error: fli-map.json file not found.")
        return
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in fli-map.json.")
        return

    create_directory_structure(data, data, convert_html=True)
    print(
        f"Directory structure created successfully based on '{data.get('title', 'Root')}'"
    )


if __name__ == "__main__":
    main()
