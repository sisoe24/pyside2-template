"""Template setup file."""

import os
import shutil
import argparse
import subprocess


def convert_placeholders(path: str, project_name: str):

    for root, _, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)

            with open(file_path, 'r') as file:
                content = file.read()

            content = content.replace('projectslug', project_name)

            with open(file_path, 'w') as file:
                file.write(content)


def setup_parser():

    parser = argparse.ArgumentParser(description='Setup projectslug template.')

    parser.add_argument('name', type=str, help='Name of the project.')
    parser.add_argument('path', type=str, help='Path to the project.')
    parser.add_argument('--git', action='store_true', help='Initialize git repository.')
    parser.add_argument('--init', action='store_true', help='Initialize the project.')

    return parser

if __name__ == '__main__':
    
    ARGS = setup_parser().parse_args()

    if ARGS.init:
        subprocess.run(['poetry', 'install'], cwd=ARGS.path)

    if ARGS.git:
        subprocess.run(['git', 'init'], cwd=ARGS.path)

    out = f'{ARGS.path}/{ARGS.name}'

    shutil.copytree(
        os.path.dirname(os.path.abspath(__file__)), out,
        ignore=shutil.ignore_patterns(
            ARGS.path, '__pycache__', '.git', '.venv', 'template.py'
        )
    )
    convert_placeholders(out, ARGS.name)

