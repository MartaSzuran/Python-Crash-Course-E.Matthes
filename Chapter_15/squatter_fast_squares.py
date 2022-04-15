import matplotlib.pyplot as plt

# counting squares up to 1000 points
x_values = list(range(1001))
y_values = [x**2 for x in x_values]

# plt.scatter(2, 4, s=200)
# edgecolor removes color from points edges
# c changes points colour name or RGB from 0 to 1 (0, 0, 0.8)
# plt.scatter(x_values, y_values, c="yellow", edgecolor="none", s=40)

# using colour map
# all colour maps which pyplot has is one the web = matplotlib.org in the gallery, on the bottom in colormaps_reference
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor="none", s=40)

# define title and labels
plt.title("Numbers square", fontsize=24)
plt.xlabel("Value", fontsize=24)
plt.ylabel("Square values", fontsize=24)

# define size of label
plt.tick_params(axis="both", which="major", labelsize=14)

# define range for each axis
plt.axis([0, 1100, 0, 1100000])

# if I would like to automatically save my plot use instead of plt.show()
# bbox_inches removes additional white spaces - it can be omitted
plt.savefig("squares_plot.png", bbox_inches="tight")
# plt.show()
