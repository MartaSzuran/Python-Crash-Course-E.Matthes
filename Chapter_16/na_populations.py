from pygal.maps.world import World

wm = World()
wm.force_uri_protocol = "http"
wm.title = "Population in North America"

# each add has different color so it will be one color for each america
wm.add("North America", {"ca": 34126000, "mx": 113423000, "us": 309349000})

wm.render_to_file("na_population.svg")
