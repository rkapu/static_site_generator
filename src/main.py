import os
import shutil

from copy_helper import copy_files_recursively

def main():
    main_dir = os.path.dirname(os.path.dirname(__file__))
    static_dir = os.path.join(main_dir, "static")
    public_dir = os.path.join(main_dir, "public")

    if os.path.exists(public_dir):
        print("Deleting public directory...")
        shutil.rmtree(public_dir)

    print("Copying static files into public directory...")
    copy_files_recursively(static_dir, public_dir)

main()
