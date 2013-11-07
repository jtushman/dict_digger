import nose
from nose.tools import *
from nose.tools import assert_raises
import dict_digger


TEST_HASH = {
    'a': {
        'b': 'tuna',
        'c': 'fish'
    },
    'b': {}
}

TEST_LIST = [
    {
        'b': 'tuna',
        'c': 'fish'
    },
    {}
]

TEST_COMPLEX = {
    'a': {
        'b': 'tuna',
        'c': 'fish',
        'list': [
            {'x': 'peanut butter'},
            {'y': 'jelly'},
        ]
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


def test_complex_find():
    result = dict_digger.dig(TEST_COMPLEX,'a','list',0)
    assert isinstance(result,dict)
    result = dict_digger.dig(TEST_COMPLEX,'a','list',0,'x')
    eq_('peanut butter', result)


def test_list_find():
    result = dict_digger.dig(TEST_LIST,0,'b')
    eq_("tuna", result)


def test_no_exception():
    result = dict_digger.dig(TEST_LIST,0,'b','c')
    assert result is None

@raises(IndexError)
def test_exception():
    dict_digger.dig(TEST_LIST,0,'b','c', fail=True)




if __name__ == "__main__":
    nose.run()