import os
from pathlib import Path
from src.markdown.conversion import markdown_to_html

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    markdown = Path(from_path).read_text()
    template = Path(template_path).read_text()

    title, content = markdown_to_html(markdown)

    html = template.replace("{{ Title }}", title).replace("{{ Content }}", content)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    Path(dest_path).write_text(html)
