import matplotlib.pyplot as plt

# Define days and temperatures
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
temperatures = [20, 22, 19, 23, 21, 24, 20]

# Plot the graph
plt.plot(days, temperatures, marker='o', linestyle='-', color='blue')
plt.title('Temperature Readings Over a Week')
plt.xlabel('Days')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.show()
