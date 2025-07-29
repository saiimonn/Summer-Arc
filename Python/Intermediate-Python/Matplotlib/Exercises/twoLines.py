import matplotlib.pyplot as plt

x1 = [10, 20, 30]
y1 = [20, 40, 10]

x2 = [10, 20, 30]
y2 = [40, 10, 30]

plt.plot(x1, y1, color = 'blue', label = 'line 1')
plt.plot(x2, y2, color = 'green', label = 'line 2')
plt.title('Two or more lines on same plot with suitable legends')
plt.ylabel('y-axis')
plt.xlabel('x-axis')
plt.legend()
plt.show()