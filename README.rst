dict_digger
===========

Digs into Dicts (or Lists, or Tuples or Complex objects)

Useful syntax for digging into nested dictionaries, lists and tuples, and removes the need to check if a key or index exists, or handling of
KeyError or IndexError


Installation
------------

.. code-block:: bash

    $ pip install dict_digger


Usage
-----

.. code-block:: python

    from dict_digger import dig

    h = {
        'a': {
             'b': 'tuna',
             'c': 'fish'
         },
         'b': {}
    }

    result = dig(h, 'a','b')
    print result  # prints 'tuna'

    result = dig(h, 'c','a')
    print result # prints None
    # Important!!  Does not throw an error, just returns None

    # but if you like
    result = dig(h, 'c','a', fail=True)
    # raises a KeyError

    # also supports complex objects so ...

    complex = {
        'a': {
             ['tuna','fish']
         },
         'b': {}
    }
    result = dig(complex, 'a',0)
    print result #prints tuna



Alternatives
------------

.. code-block:: python

    try:
        result = h['c']['a']
    except KeyError:
        result = None

Testing
-------

We are using nose

.. code-block:: bash

    $ nosetests

