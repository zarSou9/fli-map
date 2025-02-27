import json
import os
import re
from pathlib import Path


def desanitize_filename(filename):
    """Convert a sanitized filename back to a title by replacing underscores with spaces."""
    return filename.replace("_", " ")


def convert_markdown_to_html(text):
    """Convert markdown formatting back to HTML."""
    if not text:
        return text

    # Convert markdown links to HTML links with target="_blank"
    # Pattern: [text](url)
    link_pattern = r"\[(.*?)\]\((.*?)\)"
    html_text = re.sub(link_pattern, r'<a href="\2" target="_blank">\1</a>', text)

    # Convert newlines to <br> tags
    html_text = html_text.replace("\n", "<br>")

    # Convert *text* to <i>text</i>
    italic_pattern = r"\*(.*?)\*"
    html_text = re.sub(italic_pattern, r"<i>\1</i>", html_text)

    return html_text


def parse_markdown_file(file_path):
    """Parse a markdown file to extract node information."""
    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return {}

    node = {"title": desanitize_filename(file_path.stem)}

    # Extract sections using improved regex patterns that handle multiline content properly
    sections = re.split(r"^###\s+(.*?)$", content, flags=re.MULTILINE)

    if len(sections) > 1:  # If sections were found
        for i in range(1, len(sections), 2):
            section_title = sections[i].strip()
            section_content = sections[i + 1].strip() if i + 1 < len(sections) else ""

            if section_title == "Mini Description":
                node["mini_description"] = convert_markdown_to_html(section_content)
            elif section_title == "Description":
                node["description"] = convert_markdown_to_html(section_content)
            elif section_title == "Related Nodes":
                links = []
                link_pattern = r"- \[(.*?)\]\((.*?)\)(?:\n\t- Reason: (.*?))?(?:\n|$)"
                for match in re.finditer(link_pattern, section_content):
                    path = match.group(2).lstrip("/")
                    reason = match.group(3) if match.group(3) else None

                    # Store the path for now, we'll convert to IDs later
                    link = {"path": path}
                    if reason:
                        link["reason"] = reason

                    links.append(link)

                if links:
                    node["links"] = links

    return node


def format_index(idx):
    """Format an index according to the rules: if > 9, surround with dots."""
    return f".{idx}." if idx > 9 else str(idx)


def build_directory_map(root_path):
    """Build a map of directories to their node information."""
    directory_map = {}
    path_to_id_map = {}

    # First, collect all valid node directories
    valid_dirs = []
    for dirpath, dirnames, filenames in os.walk(root_path):
        dir_path = Path(dirpath)

        # Skip if not a valid node directory
        md_files = [f for f in filenames if f.endswith(".md")]
        if not md_files:
            continue

        # Find markdown file with same name as directory
        dir_name = dir_path.name
        matching_md = [f for f in md_files if Path(f).stem == dir_name]

        if matching_md:
            valid_dirs.append(dir_path)

    # Now build the hierarchy and generate IDs correctly
    # Start with root
    root_id = "0"
    root_dir = root_path
    path_to_id_map[str(root_dir)] = root_id

    # Process all directories level by level
    process_directory(root_dir, root_id, directory_map, path_to_id_map)

    # Update all links to use IDs instead of paths
    for node_id, node_info in directory_map.items():
        if "links" in node_info:
            for i, link in enumerate(node_info["links"]):
                if "path" in link:
                    path = link["path"]
                    # Extract the path without the filename
                    path_parts = path.split("/")
                    dir_path = "/".join(path_parts[:-1])

                    # Look up the ID in our path mapping
                    if dir_path in path_to_id_map:
                        # Create a new link object with just id (and reason if present)
                        new_link = {"id": path_to_id_map[dir_path]}
                        if "reason" in link:
                            new_link["reason"] = link["reason"]
                        node_info["links"][i] = new_link
                    else:
                        # Keep the original link if we couldn't resolve it
                        print(
                            f"Warning: Could not resolve path {dir_path} to a node ID"
                        )

    return directory_map


def process_directory(dir_path, node_id, directory_map, path_to_id_map):
    """Process a directory and recursively process its subdirectories."""
    # Find the markdown file for this directory
    dir_name = dir_path.name
    md_file = dir_path / f"{dir_name}.md"

    if md_file.exists():
        # Parse the markdown file
        node_info = parse_markdown_file(md_file)
        node_info["id"] = node_id
        directory_map[node_id] = node_info

        # Get subdirectories and sort them alphabetically
        subdirs = sorted([d for d in dir_path.iterdir() if d.is_dir()])

        if subdirs:
            # Create breakdown for this node
            breakdown_id = f"{node_id}0"
            node_info["breakdowns"] = [{"id": breakdown_id, "sub_nodes": []}]

            # Process each subdirectory
            for idx, subdir in enumerate(subdirs):
                # Generate the child node ID
                child_node_id = f"{node_id}0{format_index(idx)}"
                # Add mapping from path to ID
                path_to_id_map[str(subdir)] = child_node_id
                # Process the subdirectory
                process_directory(subdir, child_node_id, directory_map, path_to_id_map)

                # If the subdirectory was processed (has an entry in directory_map)
                if child_node_id in directory_map:
                    # Add the child node to the parent's sub_nodes
                    node_info["breakdowns"][0]["sub_nodes"].append(
                        directory_map[child_node_id]
                    )


def main():
    root_path = Path("Value_Alignment")

    if not root_path.exists() or not root_path.is_dir():
        print(f"Error: Root directory '{root_path}' not found.")
        return

    # Build the directory map and generate the JSON structure in one step
    directory_map = build_directory_map(root_path)

    # Get the root node
    root_node = directory_map.get("0")
    if not root_node:
        print("Error: Could not find the root node.")
        return

    output_file = Path("fli-map.json")
    output_file.write_text(json.dumps(root_node), encoding="utf-8")

    print(f"JSON structure reconstructed successfully to '{output_file}'")


if __name__ == "__main__":
    main()
