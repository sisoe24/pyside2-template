"""Template setup file."""

from typing import Dict

import os
import shutil
import argparse
import subprocess

from pprint import pprint


def convert_placeholders(path: str, placeholders: Dict[str, str]):
    print('➡ placeholders:', placeholders)
    print('➡ path:', path)
    return
    for root, _, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)

            with open(file_path, 'r') as file:
                content = file.read()

            for old, new in placeholders.items():
                content = content.replace(old, new)

            with open(file_path, 'w') as file:
                file.write(content)



def setup_parser():

    parser = argparse.ArgumentParser(description='Setup projectslug template.')

    parser.add_argument('name', type=str, help='Name of the project.')
    parser.add_argument('path', type=str, help='Path to the project.')
    parser.add_argument('--pyside', type=str, help='PySide2 version to use.')
    parser.add_argument('--git', action='store_true', help='Initialize git repository.')
    parser.add_argument('--init', action='store_true', help='Initialize the project.')

    return parser

if __name__ == '__main__':
    
    ARGS = setup_parser().parse_args()

    if ARGS.init:
        subprocess.run(['poetry', 'install'], cwd=ARGS.path)

    if ARGS.git:
        subprocess.run(['git', 'init'], cwd=ARGS.path)

    placeholders = {
        'projectSlug': ARGS.name,
        '__pysideVersion__': ARGS.pyside or '~5.15',
        '__author__': ARGS.author or os.getenv('USERNAME', os.getenv('USER', 'FIXME: yourname')),
        '__email__': ARGS.email or 'FIXME: your@email.com'
    }

    out = f'{ARGS.path}/{ARGS.name}'
    # shutil.copytree(
    #     os.path.dirname(os.path.abspath(__file__)), out,
    #     # allow for the project to be created in the same directory (why would you do it anyway?)
    #     ignore=shutil.ignore_patterns(ARGS.path)
    # )
    convert_placeholders(out, placeholders)

