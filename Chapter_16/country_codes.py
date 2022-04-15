from pygal.maps.world import COUNTRIES


def get_country_code(country_name):
    """Returns two letter country code used by Pygal."""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code

# print(get_country_code("Andorra"))
