# creating first tests

def get_formatted_name(first, last,  middle=""):
    """Creating formatted users name and lastname."""
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()
