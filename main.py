import os
import shutil

from src.copy_helper import copy_files_recursively
from src.html.generator import generate_page, generate_pages_recursively

def main():
    main_dir = os.path.dirname(__file__)
    static_dir = os.path.join(main_dir, "static")
    public_dir = os.path.join(main_dir, "public")
    content_dir = os.path.join(main_dir, "content")

    if os.path.exists(public_dir):
        print("Deleting public directory...")
        shutil.rmtree(public_dir)

    print("Copying static files into public directory...")
    copy_files_recursively(static_dir, public_dir)

    generate_pages_recursively(
        content_dir,
        os.path.join(main_dir, "template.html"),
        public_dir
    )

main()
