# simulation of rolling different dice
import pygal

from die import Die

# create two dice
die_1 = Die()
die_2 = Die(10)

# make some numbers of moves
results = []

for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# print(results)

# results analysis
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# print(frequencies)

# results visualisation
# histogram
hist = pygal.Bar()
hist.force_uri_protocol = "http"

hist.title = "Results of rolling dice D6 and D10 50 000 times."
x_labels = []
for value in range(2, max_result + 1):
    x_labels.append(value)

hist.x_labels = x_labels
hist.x_title = "result"
hist.y_title = "frequency"

# label and values to render
hist.add("D6 + D10", frequencies)
hist.render_to_file("different_dice_visual.svg")
