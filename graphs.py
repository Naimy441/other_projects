import matplotlib.pyplot as plt
import numpy as np

start, stop = -20, 20
plot_range = np.linspace(start, stop, 100)

x = [n for n in plot_range]
y = [(2*n/3)-(5/3) for n in plot_range]

plt.plot(
    x, y,
    color = 'green',
    marker = '.',
    markersize = 6.5,
    markerfacecolor = 'black',
    markeredgecolor = 'black'
)
plt.grid()
plt.xticks(range(start, stop))
plt.yticks(range(start, stop))
plt.xlim(start, stop)
plt.ylim(start, stop)
plt.show()
