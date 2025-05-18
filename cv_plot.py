import glob
import numpy as np
import matplotlib.pyplot as plt

def average_energy_at_temperature(eigenvalues, T):
    eigenvalues = eigenvalues - np.min(eigenvalues)
    boltzmann_factors = np.exp(-eigenvalues / T)
    partition_function = np.sum(boltzmann_factors)
    average_energy = np.sum(eigenvalues * boltzmann_factors) / partition_function
    return average_energy

# Define temperature range and J values
temperatures = np.logspace(-4, 3, 2000)
J_values = [1]

# Load eigenvalues
eigenvalues = {J: [] for J in J_values}
for filename in glob.glob('eigenvalues_nup*_ndown*_kx*_ky*_J*.txt'):
    J_value = int(filename.split('_J')[1].split('.txt')[0])
    eigenvalues_array = np.loadtxt(filename)
    if J_value in eigenvalues:
        eigenvalues[J_value].append(eigenvalues_array)

# Calculate and store specific heat for each J
specific_heat_dict = {}
for J in J_values:
    all_eigenvalues = np.concatenate(eigenvalues[J])
    average_energies = np.array([average_energy_at_temperature(all_eigenvalues, T) for T in temperatures])
    specific_heat = np.gradient(average_energies, temperatures)
    specific_heat_dict[J] = specific_heat / 18  # Normalize by N=18

# Plot
plt.figure(figsize=(10, 6))
for J in J_values:
    plt.plot(temperatures, specific_heat_dict[J], label=f'J = {J}, N=18')
plt.xscale('log')
plt.xlabel('T/t')
plt.ylabel('Specific Heat (C)/N')
plt.legend()
plt.show()
