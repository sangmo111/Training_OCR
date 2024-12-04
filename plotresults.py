import matplotlib.pyplot as plt

# Data
iterations = [100, 495, 995]
bcer_train = [12.441, 9.897, 29.964]
mean_rms = [1.5, 1.359, 2.356]
delta = [7.183, 6.184, 16.583]
bwer_train = [36.875, 27.562, 52.102]

# Plot BCER (train)
plt.figure(figsize=(10, 6))
plt.plot(iterations, bcer_train, marker='o', linestyle='-', color='b', label='BCER (train)')
plt.xlabel('Iterations')
plt.ylabel('BCER (train) %')
plt.title('BCER (train) at Key Iterations')
plt.legend()
plt.grid(True)
plt.show()

# Plot Mean RMS and Delta
plt.figure(figsize=(10, 6))
plt.plot(iterations, mean_rms, marker='o', linestyle='-', color='g', label='Mean RMS')
plt.plot(iterations, delta, marker='o', linestyle='-', color='r', label='Delta')
plt.xlabel('Iterations')
plt.ylabel('Value (%)')
plt.title('Mean RMS and Delta at Key Iterations')
plt.legend()
plt.grid(True)
plt.show()

# Plot BWER (train)
plt.figure(figsize=(10, 6))
plt.plot(iterations, bwer_train, marker='o', linestyle='-', color='m', label='BWER (train)')
plt.xlabel('Iterations')
plt.ylabel('BWER (train) %')
plt.title('BWER (train) at Key Iterations')
plt.legend()
plt.grid(True)
plt.show()
