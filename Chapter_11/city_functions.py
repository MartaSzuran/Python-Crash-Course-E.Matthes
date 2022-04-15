# create function taking city and country from user and format the output

def get_city_and_country(city, country, population=""):
    """Format data taken from user."""
    if population:
        formatted_data = city + ", " + country + ": " + population
    else:
        formatted_data = city + ", " + country
    return formatted_data.title()
