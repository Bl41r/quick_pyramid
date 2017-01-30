"""Test module for various functions.

These functions are prototypes for the main project.
"""


import os
import shutil


THIS_DIR = os.path.dirname(os.path.realpath(__file__))


TEST_GENERICS_TEXT = """
@view_config(route_name="[ROUTE_NAME]", renderer="[TEMPLATE]",
             permission="[PERMISSION]")
def [ROUTE_NAME](request):

    return {}
"""

TEST_GENERICS_REPLACED1 = """
@view_config(route_name="test_route", renderer="templates/test_temp.jinja2",
             permission="test")
def test_route(request):

    return {}
"""

TEST_GENERICS_REPLACED2 = """
@view_config(route_name="test_route", renderer="",
             permission="")
def test_route(request):

    return {}
"""

# Unit tests


def test_replace_placeholders():
    """Test the replace_placeholders function replaces all keywords."""
    from main_funcs import replace_placeholders
    assert replace_placeholders(
        TEST_GENERICS_TEXT, ROUTE_NAME='test_route',
        TEMPLATE='templates/test_temp.jinja2',
        PERMISSION='test') == TEST_GENERICS_REPLACED1


def test_replace_placeholders_some_empty():
    """Test the replace_placeholders function replaces all keywords."""
    from main_funcs import replace_placeholders
    assert replace_placeholders(
        TEST_GENERICS_TEXT, ROUTE_NAME='test_route',
        TEMPLATE='',
        PERMISSION='') == TEST_GENERICS_REPLACED2


def test_create_directories():
    """Test creation of directories."""
    from main_funcs import create_directories

    test_directories = ['test1', 'test2']
    create_directories(test_directories)
    for directory in test_directories:
        assert os.path.exists(directory)

    # cleanup
    for directory in test_directories:
        shutil.rmtree(directory)


def test_grab_section_text():
    """Test section text is grabbed correctly."""
    from main_funcs import grab_section_text
    expected = '@view_config(route_name=\'[ROUTE_NAME]\', renderer=\'[TEMPLATE]\',\n             permission=\'[PERMISSION]\')\ndef [ROUTE_NAME](request):\n    """Route for [ROUTE_NAME]."""\n\n    return {}\n'
    assert expected == grab_section_text('generic-route', 'generics')
