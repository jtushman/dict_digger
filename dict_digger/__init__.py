

def dig(your_dict, *keys):
    """
    digs into an dict, if anything along the way is None, then simply return None
    """
    end_of_chain = your_dict
    for key in keys:
        if isinstance(end_of_chain, dict) and key in end_of_chain:
            end_of_chain = end_of_chain[key]
        else:
            return None

    return end_of_chain
