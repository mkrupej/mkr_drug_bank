"""
This module is used to generate drug defined within database.
"""
from lxml.etree import iterparse


def load(filename, path):
    """
    Function returns generator which generates each single drug defined within DB.
    :param filename: path to DB file
    :param path: name of searched selector
    :return: single drug element as elem item
    """
    path_parts = path.split('/')  # replace path with list
    doc = iterparse(filename, ('start', 'end'))  # lxml iterparse is used
    next(doc)  # skip root elem

    tag_stack = []
    elem_stack = []
    for event, elem in doc:
        if event == 'start':
            tag_stack.append(elem.tag)
            elem_stack.append(elem)
        elif event == 'end':
            if tag_stack == path_parts:
                del event
                yield elem  # yield drug
                elem_stack.pop()
                del elem
            try:
                tag_stack.pop()
                elem_stack.pop()
            except IndexError:
                pass
