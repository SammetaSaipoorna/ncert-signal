import matplotlib.pyplot as plt

# Read data from file
with open('data5.txt', 'r') as file:
    data = [int(line.strip()) for line in file]

# Plot the data as a stem plot
plt.stem(range(len(data)), data)
plt.xlabel('n')
plt.ylabel('x(n)')
plt.grid(True)
plt.savefig('plot5.png')
plt.show()

