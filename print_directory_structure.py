import os

def print_directory_structure(root_dir, exclude_dirs=None, level=0):
    if exclude_dirs is None:
        exclude_dirs = ['.venv', '__pycache__', 'node_modules','.git','.github','.idea']

    for item in os.listdir(root_dir):
        item_path = os.path.join(root_dir, item)
        if os.path.isdir(item_path):
            if item in exclude_dirs:
                continue
            print('  ' * level + '|-- ' + item)
            print_directory_structure(item_path, exclude_dirs, level + 1)
        else:
            print('  ' * level + '|-- ' + item)

if __name__ == '__main__':
    project_root = os.path.dirname(os.path.abspath(__file__))
    print_directory_structure(project_root)