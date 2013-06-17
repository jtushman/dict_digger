dict_digger
===========

Digs into Dicts

Useful syntax for digging into nested dictionaries, and removes the need to check if a key exists


Installation
------------

.. code-block:: bash

    $ pip install


Usage
-----

.. code-block:: python

    import dict_digger

    h = {
        'a': {
            'b': 'tuna',
            'c': 'fish'
        }
        'b': {}
    }

    result = dict_digger(h, ['a','b'])
    print result  # prints 'tuna'

    result = dict_digger(h, ['c','a']
    # Does not through an error, just returns None


    print time_ago_in_words()
    #prints "just now"

    print time_ago_in_words(begining_of_day())
    # prints 8 hours ago