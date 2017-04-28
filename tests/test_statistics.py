# -*- coding: utf-8 -*-
"""Statistics unit tests."""

from pdb import set_trace  # noqa
import unittest
from random import seed
from collections import defaultdict
# from mock import Mock
# from mock import PropertyMock
# from mock import mock_open
# from mock import patch
from npcseed.statistics import weighted_choice


class StatisticsTest(unittest.TestCase):
    @classmethod
    def setup_class(cls):
        """Called once for this class."""
        pass

    def setUp(self):
        """Called before any teste.

        Make sure we can repeat the randomness."""
        seed(0)

    def test_weighted_choice_single(self):
        values = (('xUnit Tets', 1.0), )
        self.assertEqual('xUnit Tets', weighted_choice(values))

    def test_weighted_choice_uniform(self):
        values = (('one', 0.25), ('two', 0.25), ('three', 0.25), ('four',
                                                                  0.25), )
        results = {}
        results = defaultdict(lambda: 0, results)
        for x in range(0, 10000):
            results[weighted_choice(values)] += 1
        expected = {'three': 2524, 'four': 2496, 'two': 2512, 'one': 2468}
        self.assertEqual(expected, results)

    def test_weighted_choice_increasing(self):
        values = (('one', 1), ('two', 2), ('three', 3), ('four', 4), )
        results = {}
        results = defaultdict(lambda: 0, results)
        for x in range(0, 10000):
            results[weighted_choice(values)] += 1
        expected = {
            'one': 1026,
            'two': 1923,
            'three': 3028,
            'four': 4023,
        }
        self.assertEqual(expected, results)

    def tearDown(self):
        """Tidy after each tests."""
        pass

    @classmethod
    def teardown_class(cls):
        """Tidy after the class."""
        pass


# eof
