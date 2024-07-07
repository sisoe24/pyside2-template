"""Template setup file."""

import os
import subprocess
import sys
import argparse

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

def replace_placeholders(file_path: str, project_name: str):
    with open(file_path, 'r') as file:
        content = file.read()
        content = content.replace('projectslug', project_name)

    with open(file_path, 'w') as file:
        file.write(content)

def convert_placeholders(path: str, project_name: str):
    """
    Converts placeholders in files and directories to the specified project name.

    Args:
        path (str): The root path where the conversion should be performed.
        project_name (str): The name of the project to replace the placeholders with.

    """
    print('Renaming files content...')
    for root, _, files in os.walk('projectslug'):
        for f in files:
            if not f.endswith('.py'):
                continue

            replace_placeholders(os.path.join(root, f), project_name)

    # replace placeholders in pyproject.toml
    replace_placeholders(os.path.join(path, 'pyproject.toml'), project_name)

    # Rename top level directory
    os.rename(
        os.path.join(path, 'projectslug'),
        os.path.join(path, project_name)
    )


def main():

    parser = argparse.ArgumentParser(description='Create a new project from template.')
    parser.add_argument(
        '--init', action='store_true', 
        help='Initialize the project. This will replace placeholders with the project name.'
    )

    ARGS = parser.parse_args()

    if not ARGS.init:
        parser.print_help()
        sys.exit(1)

    package_name = input('Enter package name: ')
    package_name = package_name.lower().replace(' ', '_')

    if input('Replace placeholders with package name? (y/n): ') != 'y':
        sys.exit(0)

    convert_placeholders(ROOT, package_name)

    if input('Initialize poetry? (y/n): ') == 'y':
        subprocess.run(['poetry', 'install'], cwd=ROOT)

    if input('Initialize pre-commit? (y/n): ') == 'y':
        subprocess.run(['pre-commit', 'install'], cwd=ROOT)


if __name__ == '__main__':
    print('Running template setup...')
    main()