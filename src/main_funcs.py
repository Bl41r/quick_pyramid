"""Utility functions for the main application."""


import os


def create_directories(directory_names):
    """Create directories from a given list of directory names."""
    for directory in directory_names:
        if not os.path.exists(directory):
            os.makedirs(directory)


def create_route(route_name):
    """Return text for a route."""
    return '@view_config(route_name="' + route_name + '")\n' + 'def ' +\
        route_name + '(request):\n    ' + 'return {}\n\n'
