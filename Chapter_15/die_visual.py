# simulation of rolling one die

import pygal
# pygal
# A Python svg graph plotting library
# it is very helpful to work with web app because visualisations adjust to the different screens automatically
# www.pygal.org

from die import Die

# create one die
die = Die()

# make some numbers of moves
results = []

for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# print(results)

# results analysis
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# print(frequencies)

# results visualisation
# histogram
hist = pygal.Bar()
hist.force_uri_protocol = "http"

hist.title = "Results of rolling cube die 1000 times."
hist.x_labels = ["1", "2", "3", "4", "5", "6"]
hist.x_title = "result"
hist.y_title = "frequency"

# label and values to render
hist.add("D6", frequencies)
hist.render_to_file("die_visual.svg")
