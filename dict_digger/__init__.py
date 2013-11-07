

def dig(your_dict, *keys, **kwargs):
    """
    digs into an dict, if anything along the way is None, then simply return None

    **now supports dicts, lists and tupples!!

    pass fail=True if you want to through an IndexError vs just returing None

    """
    end_of_chain = your_dict
    for key in keys:
        if isinstance(end_of_chain, dict) and key in end_of_chain:
            end_of_chain = end_of_chain[key]
        elif isinstance(end_of_chain, (list, tuple)) and isinstance(key, int):
            end_of_chain = end_of_chain[key]
        else:
            if 'fail' in kwargs and kwargs['fail'] is True:
                if isinstance(end_of_chain,dict):
                    raise KeyError
                else:
                    raise IndexError
            else:
                return None

    return end_of_chain
