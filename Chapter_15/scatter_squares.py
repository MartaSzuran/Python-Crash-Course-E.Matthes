import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

# plt.scatter(2, 4, s=200)
plt.scatter(x_values, y_values, s=100)

# define title and labels
plt.title("Numbers square", fontsize=24)
plt.xlabel("Value", fontsize=24)
plt.ylabel("Square values", fontsize=24)

# define size of label
plt.tick_params(axis="both", which="major", labelsize=14)

plt.show()
