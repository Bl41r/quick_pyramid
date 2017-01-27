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
    
    x = re.match('\$\$generic-route\$\$\\n(.+?)(?=\$\$-\$\$)', text, re.DOTALL)
    return x.group(1)


def run_pyramid_scaffold(appname, sqlalchemy=True):
    """Create normal pyramid scaffold."""
    subprocess.Popen(['pip', 'install', '-U', 'pip', 'setuptools'])
    subprocess.Popen(['pip', 'install', 'pyramid', 'pyramid_ipython'])

    if sqlalchemy:
        subprocess.Popen(['pip', 'install', 'sqlalchemy'])
        alchemy = 'alchemy'
    else:
        alchemy = ''

    subprocess.Popen(['pcreate', '-s', alchemy, appname])


def create_generic_route(route_name, renderer=None, permission=None):
    """Return text for a route."""
    pass
