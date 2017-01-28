"""Utility functions for the main application."""


import os
import subprocess
import re


def create_directories(directory_names):
    """Create directories from a given list of directory names."""
    for directory in directory_names:
        if not os.path.exists(directory):
            os.makedirs(directory)


def grab_section_text(section_name, filename):
    """Return the text from a section.

    Sections are marked begining with $$section_name$$ and ending with
    $$-$$.  This function returns all text in-between these markers.
    """
    with open(filename, 'r') as f:
        text = f.read()

    return re.match(
        '\$\$generic-route\$\$\\n(.+?)(?=\$\$-\$\$)',
        text,
        re.DOTALL
    ).group(1)


def replace_placeholder(body_text, **kwargs):
    """Replace keywords in text marked like [KEYWORD]."""
    for key, value in kwargs.items():
        body_text = re.sub('\[' + key + ']', value, body_text, 0, re.DOTALL)
    return body_text


def create_venv(folder_name='ENV'):
    """Create and update a virtual environment."""
    p = subprocess.Popen(['python3', '-m', 'venv', folder_name])
    subprocess.Popen.wait(p)
    p = subprocess.Popen(['pip', 'install', '-U', 'pip', 'setuptools'])
    subprocess.Popen.wait(p)


def run_pyramid_scaffold(appname, sqlalchemy=True):
    """Create normal pyramid scaffold."""
    p = subprocess.Popen(['pip', 'install', 'pyramid', 'pyramid_ipython'])
    subprocess.Popen.wait(p)

    if sqlalchemy:
        p = subprocess.Popen(['pip', 'install', 'sqlalchemy'])
        subprocess.Popen.wait(p)
        alchemy = 'alchemy'
    else:
        alchemy = ''

    p = subprocess.Popen(['pcreate', '-s', alchemy, appname])
    subprocess.Popen.wait(p)


def create_generic_route(route_name, renderer=None, permission=None):
    """Return text for a generic route."""
    pass


if __name__ == '__main__':
    run_pyramid_scaffold('testapp1')
