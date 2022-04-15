import matplotlib.pyplot as plt

from random_walk import RandomWalk

# generate random walks till user decide to stop
while True:
    rw = RandomWalk()
    rw.fill_walk()

    # design changes
    # create variable point_numbers which is list from 1 to 5000
    # so it is a max list of number of points in object rw
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors="none", s=15)

    # first and last point change to be more visible with making them in different colour and size
    plt.scatter(0, 0, c="green", edgecolors="none", s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="none", s=100)

    # hide axis
    # in the book was plt.axes().get_xaxis().set_visible(False) but it didn't work for me
    plt.gca().get_xaxis().set_visible(False)
    plt.gca().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Create another random walk? (y/n)")
    if keep_running == "n":
        break
