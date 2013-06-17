# Core Imports
from copy import deepcopy


def dig(hash,*keys):
    """
    digs into an dict, if anything along the way is None, then simply return None
    """
    end_of_chain = deepcopy(hash)
    for key in keys:
        if isinstance(end_of_chain, dict) and key in end_of_chain:
            end_of_chain = end_of_chain[key]
        else:
            return None

    return end_of_chain
