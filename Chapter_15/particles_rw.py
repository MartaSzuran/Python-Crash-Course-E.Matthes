# adding points

import matplotlib.pyplot as plt

from random_walk import RandomWalk

# generate random walks till user decide to stop
while True:
    rw = RandomWalk(50000)
    rw.fill_walk()

    # set the size of the plotting window
    # figure() control width, height, resolution (rozdzielczość) and background colour
    # figsize() take as argument a tuple of window size in inches
    plt.figure(dpi=128, figsize=(10, 6))

    plt.plot(rw.x_values, rw.y_values, linewidth=15)

    # hide axis
    plt.gca().get_xaxis().set_visible(False)
    plt.gca().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Create another random walk? (y/n)")
    if keep_running == "n":
        break
