import os


def create_project_structure(structure, base_path):
    """Creates files and folders for a given structure"""
    for name, value in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(value, dict):
            os.makedirs(path)
            create_project_structure(value, base_path=path)
        else:
            with open(path, 'w') as f:
                f.write(value)
