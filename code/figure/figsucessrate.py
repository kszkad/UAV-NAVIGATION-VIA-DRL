import matplotlib.pyplot as plt
import numpy as np

# 设置全局字体为新罗马字体
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Times New Roman'
# 设置全局字体大小
plt.rcParams.update({'font.size': 12})

# Data
scenarios = ['Playground', 'City', 'Canyon']
methods = ['SAC+RAE', 'SAC+CFS', 'Our method']
success_rates = [
    [0.75, 0.94, 0.99],  # Success rates for Scenario 1
    [0.17, 0.61, 0.97],  # Success rates for Scenario 2
    [0.06, 0.69, 0.84]   # Success rates for Scenario 3
]

# Bar width
bar_width = 0.2

# X-axis positions
x = np.arange(len(scenarios))

# Plotting
fig, ax = plt.subplots()
for i, method in enumerate(methods):
    ax.bar(x + i * bar_width, [success_rates[j][i] for j in range(len(scenarios))], bar_width, label=method)

# X-axis ticks and labels
ax.set_xticks(x + bar_width)
ax.set_xticklabels(scenarios)

# Y-axis label
ax.set_ylabel('Success Rate')

# Legend
ax.legend(loc='upper left', framealpha=0.5)

# Title
# ax.set_title('Success Rate Comparison Across Scenarios and Methods')

# Save the chart as a JPG file
plt.savefig('./figure/successrate.tif', format='tif', dpi=500)

# Display the plot
plt.show()