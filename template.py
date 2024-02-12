"""Template setup file."""

import os
import shutil
import argparse
import subprocess


def convert_placeholders(path: str, project_name: str):

    for root, _, files in os.walk(path):

        for f in files:
            if f.startswith('.'):
                continue

            file_path = os.path.join(root, f)

            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            content = content.replace('projectslug', project_name)

            with open(file_path, 'w') as f:
                f.write(content)


    for root, dirs, _ in os.walk(path):
        for d in dirs:
            if 'projectslug' not in d:
                continue

            os.rename(
                os.path.join(root, d),
                os.path.join(root, d.replace('projectslug', project_name))
            )

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
    
    if os.path.exists(out):
        shutil.rmtree(out)

    shutil.copytree(
        os.path.dirname(os.path.abspath(__file__)), out,
        ignore=shutil.ignore_patterns(
            ARGS.path, '__pycache__', '.git', '.venv', 'template.py', 
            '*.lock'
        ), dirs_exist_ok=True
    )

    for root, dirs, files in os.walk(out):
        for f in files:
            if f.endswith('.pyc'):
                print('➡ file_path:', f)

    convert_placeholders(out, ARGS.name)

