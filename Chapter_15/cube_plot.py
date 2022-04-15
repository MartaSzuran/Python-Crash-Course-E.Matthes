import matplotlib.pyplot as plt

x_values = list(range(1, 5001))

y_values = []
for x in x_values:
    x = x**3
    y_values.append(x)

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Greys, s=50)

plt.title("Number cubes", fontsize=20)
plt.xlabel("Cubes", fontsize=20)
plt.ylabel("Numbers", fontsize=20)

plt.tick_params(axis="both", which="major", labelsize=20)

plt.show()
