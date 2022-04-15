import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]

squares = [1, 4, 8, 16, 25]
plt.plot(input_values, squares, linewidth=5)

# plt.plot(squares, linewidth=5)

# define title and labels
plt.title("Numbers square", fontsize=24)
plt.xlabel("Value", fontsize=24)
plt.ylabel("Square values", fontsize=24)

# define size of label
plt.tick_params(axis="both", labelsize=14)

plt.show()
