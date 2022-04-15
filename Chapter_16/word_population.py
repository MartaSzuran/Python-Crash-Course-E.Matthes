import json

from pygal.maps.world import World
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS

from country_codes import get_country_code


# reading data and put it on the list
filename = "population_data.json"
with open(filename) as f:
    pop_data = json.load(f)

cc_population = {}
# print population for 2010
for pop_dict in pop_data:
    if pop_dict["Year"] == "2010":
        country_name = pop_dict["Country Name"]
        population = int(float(pop_dict["Value"]))
        code = get_country_code(country_name)
        if code:
            cc_population[code] = population

# making groups to work with relation color to population
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_population.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

# RotateStyle take one argument color in sys 16(#regrbl)
wm_style = RS("#336699", base_style=LCS)
wm = World(style=wm_style)
wm.force_uri_protocol = "http"
wm.title = "World population in 2010"
wm.add("0 - 10mln", cc_pops_1)
wm.add("10mln - 1 mld", cc_pops_2)
wm.add(">1mld", cc_pops_3)

wm.render_to_file("world_population.svg")
