from pygal.maps.world import World

wm = World()
wm.force_uri_protocol = "http"
wm.title = "North, Central, South America"

# each add has different color so it will be one color for each america
wm.add("North America", ["ca", "mx", "us"])
wm.add("Central America", ["bz", "cr", "gt", "hn", "ni", "pa", "sv"])
wm.add("South America", ["ar", "bo", "br", "cl", "co", "ec", "gf", "gy", "pe", "py", "sr", "uy", "ve"])

wm.render_to_file("americas.svg")
