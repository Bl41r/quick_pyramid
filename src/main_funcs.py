"""Utility functions for the main application."""


import os
import subprocess


def create_directories(directory_names):
    """Create directories from a given list of directory names."""
    for directory in directory_names:
        if not os.path.exists(directory):
            os.makedirs(directory)


def create_generic_route(route_name, renderer=None, permission=None):
    """Return text for a route."""
    pass


def run_pyramid_scaffold(appname, sqlalchemy=True):
    """Create normal pyramid scaffold."""
    subprocess.Popen(['pip', 'install', '-U', 'pip', 'setuptools'])
    subprocess.Popen(['pip', 'install', 'pyramid'])

    if sqlalchemy:
        subprocess.Popen(['pip', 'install', 'sqlalchemy'])
        alchemy = 'alchemy'
    else:
        alchemy = ''

    subprocess.Popen(['pcreate', '-s', alchemy, appname])
