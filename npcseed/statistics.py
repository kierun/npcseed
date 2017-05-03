# -*- coding: utf-8 -*-
"""Statistical functions and whatnot."""
from random import uniform
from pdb import set_trace  # noqa


def weighted_choice(choices):
    """Like random.choice, but each element can have a different chance of
    being selected.

    Choices can be any iterable containing iterables with two items each.
    Technically, they can have more than two items, the rest will just be
    ignored. The first item is the thing being chosen, the second item is
    its weight. The weights can be any numeric values, what matters is the
    relative differences between them.

    >>> values = (('one', 1), ('two', 2), ('three', 3), ('four', 4), )
    >>> weighted_choice(values)
    'three'

    Taken from this `answer`_ by Ned Batchelder.

    .. _answer: http://stackoverflow.com/a/3679747/232794

    :param iterable choices: An iterable of (value, probability) tuples.
    :returns: A value, whatever that is.
    """
    total = sum(w for c, w in choices)
    r = uniform(0, total)
    upto = 0
    for c, w in choices:  # pragma: no branch
        if upto + w >= r:
            return c
        upto += w

# EOF
