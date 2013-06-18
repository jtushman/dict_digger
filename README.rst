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
         },
         'b': {}
    }

    result = dict_digger.dig(h, 'a','b')
    print result  # prints 'tuna'

    result = dict_digger.dig(h, 'c','a')
    print result # prints None
    # Important!!  Does not through an error, just returns None


Testing
-------

We are using nose

.. code-block:: bash

    $ nosetests

