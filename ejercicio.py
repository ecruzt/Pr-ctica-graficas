import numpy as np
import matplotlib.pyplot as plt

vector = np.random.rand(720)
matrix = vector.reshape((120, 6))
matrix_T_F = matrix.T.copy(order='F')
matrix_T_C = matrix.T.copy(order='C')

fig, axs = plt.subplots(2, 3, figsize=(12, 8), gridspec_kw={'width_ratios': [2, 1, 1], 'height_ratios': [1, 1]})

for i, ax in enumerate(axs.flat):
    row = matrix[i, :]
    if i == 0:
        ax.plot(row)
        ax.set_title('Plot')
    elif i == 1:
        ax.scatter(range(6), row)
        ax.set_title('Scatter')
    elif i == 2:
        ax.bar(range(6), row)
        ax.set_title('Bar')
    elif i == 3:
        ax.hist(row, bins=10)
        ax.set_title('Histogram')
    elif i == 4:
        ax.pie(row, labels=[f'Category {j}' for j in range(6)])
        ax.set_title('Pie Chart')
    elif i == 5:
        ax.plot(row, 'o-')
        ax.set_title('Line Plot with Markers')
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.grid(True)
    ax.legend()

plt.show()