import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a line plot
plt.plot(x, y, label='Simple Line Plot')

# Add labels to the plot
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Add a title to the plot
plt.title('Simple Matplotlib Example')

# Add a legend
plt.legend()

# Display the plot
plt.show()
