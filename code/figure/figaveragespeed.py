import matplotlib.pyplot as plt
import numpy as np

# Function to read data from a file and calculate mean, min, and max
def calculate_stats(file_path):
    with open('./date/'+file_path, 'r') as file:
        data = [float(line.strip()) for line in file if line.strip()]
    mean = np.mean(data)
    min_val = np.min(data)
    max_val = np.max(data)
    return mean, min_val, max_val

# 设置全局字体为新罗马字体
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Times New Roman'
# 设置全局字体大小
plt.rcParams.update({'font.size': 12})

# File paths (replace with your actual file paths)
file_paths = []

file_paths.append('method3map13averagespeed.txt')
file_paths.append('method2map13averagespeed.txt')
file_paths.append('method1map13averagespeed.txt')
file_paths.append('method3map12averagespeed.txt')
file_paths.append('method2map12averagespeed.txt')
file_paths.append('method1map12averagespeed.txt')
file_paths.append('method3map11averagespeed.txt')
file_paths.append('method2map11averagespeed.txt')
file_paths.append('method1map11averagespeed.txt')

# Initialize lists to store statistics
means = []
mins = []
maxs = []

# Calculate statistics for each file
for file_path in file_paths:
    mean, min_val, max_val = calculate_stats(file_path)
    means.append(mean)
    mins.append(min_val)
    maxs.append(max_val)

# Reshape the data into 3 scenarios and 3 methods
means = np.array(means).reshape(3, 3)
mins = np.array(mins).reshape(3, 3)
maxs = np.array(maxs).reshape(3, 3)

# Scenarios and methods
scenarios = ['Playground', 'City', 'Canyon']
methods = ['SAC+RAE', 'SAC+CFS', 'Our method']
colors = ['red', 'green', 'blue']

# Bar width
bar_width = 0.2

# X-axis positions
x = np.arange(len(scenarios))

# Plotting
fig, ax = plt.subplots()
for i, method in enumerate(methods):
    # Calculate the positions for each method's bars
    positions = x + i * bar_width
    # Plot bars (mean values)
    ax.bar(positions, means[:, i], bar_width, label=method)
    # Add error bars (min and max)
    ax.errorbar(positions, means[:, i],
                yerr=[means[:, i] - mins[:, i], maxs[:, i] - means[:, i]],
                fmt='none', ecolor='black', capsize=5)

# X-axis ticks and labels
ax.set_xticks(x + bar_width)
ax.set_xticklabels(scenarios)

# Y-axis label
ax.set_ylabel('Average Speed')

# Legend in the top-right corner with a transparent background
ax.legend(loc='upper left', framealpha=0.5)

# Title
# ax.set_title('Average Speed Across Scenarios and Methods')
# Save the chart as a JPG file
plt.savefig('./figure/averagespeed.tif', format='tif', dpi=500)
# Display the plot
plt.show()