import os
import shutil

def copy_files_recursively(src_dir_path, dst_dir_path):
    if not os.path.exists(dst_dir_path):
        os.mkdir(dst_dir_path)

    with os.scandir(src_dir_path) as it:
        for entry in it:
            from_path = os.path.join(src_dir_path, entry.name)
            to_path = os.path.join(dst_dir_path, entry.name)
            print(f" * {from_path} -> {to_path}")
            if entry.is_file():
                shutil.copy(from_path, to_path)
            else:
                copy_files_recursively(from_path, to_path)
