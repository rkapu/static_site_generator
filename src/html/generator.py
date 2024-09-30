import os
from pathlib import Path
from src.markdown.conversion import markdown_to_html

def generate_page(from_path, template_path, dest_path):
    print(f" * {from_path} to {dest_path} using {template_path}")

    markdown = Path(from_path).read_text()
    template = Path(template_path).read_text()

    title, content = markdown_to_html(markdown)

    html = template.replace("{{ Title }}", title).replace("{{ Content }}", content)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    Path(dest_path).write_text(html)

def generate_pages_recursively(dir_path_content, template_path, dest_dir_path):
    with os.scandir(dir_path_content) as it:
        for entry in it:
            from_path = os.path.join(dir_path_content, entry.name)
            if entry.is_file():
                file_name, file_extension = os.path.splitext(entry.name)
                if file_extension == ".md":
                    to_path = os.path.join(dest_dir_path, f"{file_name}.html")
                    generate_page(from_path, template_path, to_path)
            elif entry.is_dir():
                to_path = os.path.join(dest_dir_path, entry.name)
                generate_pages_recursively(from_path, template_path, to_path)
