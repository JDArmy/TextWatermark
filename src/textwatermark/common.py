'''Some common functions here'''


def add_head_n_tial_to_dict(the_dict: dict, head: str, tail: str):
    '''Add head and tail to a dict, will directly effect to origin dict.

    Args:
        the_dict (dict): dict to add head and tail to
        head (str): head string to add
        tail (str): tail string to add

    '''
    for _, ival in the_dict.items():
        for jkey, _ in enumerate(ival):
            ival[jkey] = head + ival[jkey] + tail
