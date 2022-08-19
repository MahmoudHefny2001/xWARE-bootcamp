# dictionary comprehension = create dictionaries using an expression
#                            can replace loops and certain lambda functions
#
# dictionary = {key: expression for (key, value) in iterable}
# dictionary = {key: expression for (key, value) in iterable if conditional}
# dictionary = {key: (if/else) for (key, value) in iterable}
# dictionary = {key: function(value) for (key, value) in iterable}
# -----------------------------------------------------------------------
cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}  ## short for fehernheit
cities_in_C = {key: round((value-32)*(5/9)) for (key, value) in cities_in_F.items()}
print(cities_in_C)

# ------------------------------------------------------------------------------
weather = {'New York': "snowing", 'Boston': "sunny", 'Los Angles': "sunny", 'Chicago': "cloudy"}
sunny_weather = {key: value for (key, value) in weather.items() if value == "sunny"}
print(sunny_weather)

# ------------------------------------------------------------------------

cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
desc_cities = {key: ("Warm" if value >= 40 else "Cold") for (key, value) in cities.items()}
print(desc_cities)
print("")
# -------------------------------------------------------------------------------------
cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
def check_temp(temp):
    if temp >= 70:
        return "Hot"
    elif 69 >= temp >= 46 :
        return "Warm"
    else:
        return "Cold"
desc_cities = {key: check_temp(value) for (key, value) in cities.items()}
print(desc_cities)
