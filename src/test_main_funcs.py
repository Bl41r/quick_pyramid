"""Test module for various functions.

These functions are prototypes for the main project.
"""


import os
import shutil


THIS_DIR = os.path.dirname(os.path.realpath(__file__))


def test_create_directories():
    """Test creation of directories."""
    test_directories = ['test1', 'test2']
    from main_funcs import create_directories
    create_directories(test_directories)
    for directory in test_directories:
        assert os.path.exists(directory)

    for directory in test_directories:
        shutil.rmtree(directory)
