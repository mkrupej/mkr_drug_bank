from lxml.etree import iterparse


def load(filename, path):
    """

    :param filename:
    :param path:
    :return:
    """
    path_parts = path.split('/')
    doc = iterparse(filename, ('start', 'end'))
    next(doc)  # skip root elem

    tag_stack = []
    elem_stack = []
    for event, elem in doc:
        if event == 'start':
            tag_stack.append(elem.tag)
            elem_stack.append(elem)
        elif event == 'end':
            if tag_stack == path_parts:
                #    print("WOLAJA")
                del event
                yield elem
                elem_stack.pop()
                del elem
            try:
                tag_stack.pop()
                elem_stack.pop()
            except IndexError:
                pass
