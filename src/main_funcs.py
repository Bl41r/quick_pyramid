"""Utility functions for the main application."""


import os


def create_directories(directory_names):
    """Create directories from a given list of directory names."""
    for directory in directory_names:
        if not os.path.exists(directory):
            os.makedirs(directory)


def create_generic_route(route_name, renderer=None, permission=None):
    """Return text for a route."""
    pass
