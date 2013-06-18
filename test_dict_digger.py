import nose
from nose.tools import *
import dict_digger


TEST_HASH = {
    'a': {
        'b': 'tuna',
        'c': 'fish'
    },
    'b': {}
}


def test_nested_find():
    result = dict_digger.dig(TEST_HASH,'a','b')
    eq_("tuna", result)


def test_toplevel_find():
    result = dict_digger.dig(TEST_HASH,'a')
    eq_({'b': 'tuna', 'c': 'fish'}, result)


def test_nested_miss():
    result = dict_digger.dig(TEST_HASH,'c','b')
    eq_(None, result)


def test_end_point_miss():
    result = dict_digger.dig(TEST_HASH,'a','z')
    eq_(None, result)


if __name__ == "__main__":
    nose.run()