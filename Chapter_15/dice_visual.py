# simulation of rolling 2 dice
import pygal

from die import Die

# create two dice
die_1 = Die()
die_2 = Die()

# make some numbers of moves
results = []

for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# print(results)

# results analysis
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(1, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# print(frequencies)

# results visualisation
# histogram
hist = pygal.Bar()
hist.force_uri_protocol = "http"

hist.title = "Results of rolling cubes dice 1000 times."
hist.x_labels = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
hist.x_title = "result"
hist.y_title = "frequency"

# label and values to render
hist.add("D6 + D6", frequencies)
hist.render_to_file("dice_visual.svg")
