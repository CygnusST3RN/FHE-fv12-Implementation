
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Addition', 'Multiplication', 'Encryption', 'Decryption']
a1 = [0.243, 1896.328, 0.321, 0.116]
b1 = [0.784, 1.415, 1.485, 0.374]



# Set the width of the bars
bar_width = 0.25

# Create an array of positions for each category
positions = np.arange(len(categories))

# Create a bar graph
plt.bar(positions - bar_width/2, a1, label='BFV', width=bar_width, color='blue', alpha=0.7)
plt.bar(positions + bar_width/2, b1, label='CKKS', width=bar_width, color='green', alpha=0.7)

# Labeling the axes
plt.xlabel('Values')
plt.ylabel('Time in μs')
plt.title('Time')

# Adding a legend
plt.legend()

# Adjust x-axis ticks and labels
plt.xticks(positions, categories)

plt.ylim(0, 10)

# Show the plot
plt.show()
