import numpy as np
import time
import random
import argparse
import os

# Parse command-line argument for temperature
parser = argparse.ArgumentParser(description='MC simulation')
parser.add_argument('temperature', type=float)
args = parser.parse_args()

# Lattice parameters
LX, LY = 12,12
N = LX * LY

# Load interaction data
data = np.load("interaction_V_.npz")
aA = data['aA']
aA1 = data['aA1']
aA2 = data['aA2']

# Define energy functions
def energy(config):
    return np.sum(aA * config[aA1] * config[aA2])

def energy_change(config, i1, i2):
    e1 = np.sum(aA[i1] * config[aA1[i1]] * config[aA2[i1]])
    e2 = np.sum(aA[i2] * config[aA1[i2]] * config[aA2[i2]])
    config[i1], config[i2] = config[i2], config[i1]
    e3 = np.sum(aA[i1] * config[aA1[i1]] * config[aA2[i1]])
    e4 = np.sum(aA[i2] * config[aA1[i2]] * config[aA2[i2]])
    return 2 * (e3 + e4 - e1 - e2)

# Temperature setup
temp = args.temperature
Temp = temp
beta = 1 / Temp

# Output file suffix
suffix = f"T{temp:.3f}"

# Checkpoint file
ckpt_file = f"checkpoint_{suffix}.npz"

# Load from checkpoint if exists
if os.path.exists(ckpt_file):
    ckpt = np.load(ckpt_file)
    config = ckpt['config']
    ee = ckpt['ee']
    counter = int(ckpt['counter'])
    sum_energy = ckpt['sum_energy']
    sum_energy_sq = ckpt['sum_energy_sq']
    sum_config = ckpt['sum_config']
    print(f"Resuming from checkpoint at step {counter} for T={Temp:.4f}")
else:
    config = np.zeros(N, dtype=int)
    config[:N // 2] = 1
    np.random.shuffle(config)
    ee = energy(config) / 2
    counter = 1
    sum_energy = 0.0
    sum_energy_sq = 0.0
    sum_config = np.zeros(N, dtype=float)

# Parameters
max_steps = 1_000_000_000
thermalization_steps = 1_000_000
save_interval = 100 * N
checkpoint_interval = 1_000_000  # steps
last_config = np.copy(config)

start_time = time.perf_counter()

while counter <= max_steps:
    while True:
        i1, i2 = random.sample(range(N), 2)
        if config[i1] != config[i2]:
            break

    trial_config = config.copy()
    delta_E = energy_change(trial_config, i1, i2)

    if random.random() < np.exp(-delta_E * beta / 2):
        config = trial_config
        ee += delta_E / 2

    if counter > thermalization_steps:
        sum_energy += ee
        sum_energy_sq += ee ** 2
        sum_config += config

    if counter % save_interval == 0:
        last_config = np.copy(config)
        print(f"Step {counter}, Energy {ee}")

    # Periodically save checkpoint
    if counter % checkpoint_interval == 0:
        np.savez(ckpt_file,
                 config=config,
                 ee=ee,
                 counter=counter,
                 sum_energy=sum_energy,
                 sum_energy_sq=sum_energy_sq,
                 sum_config=sum_config)

    counter += 1

# Final results
effective_steps = counter - thermalization_steps
if effective_steps > 0:
    avg_energy = sum_energy / effective_steps
    avg_config = sum_config / effective_steps
    specific_heat = (sum_energy_sq / effective_steps - avg_energy ** 2) * beta ** 2
else:
    avg_energy = 0
    avg_config = config
    specific_heat = 0

# Save final outputs
np.savetxt(f'final_config_{suffix}.txt', last_config, fmt='%d', delimiter=',')
np.savetxt(f'final_step_{suffix}.txt', np.array([counter]), fmt='%d')
np.savetxt(f'temperature_{suffix}.txt', np.array([1 / beta]), delimiter=',')
np.savetxt(f'specific_heat_{suffix}.txt', np.array([specific_heat]), delimiter=',')
np.savetxt(f'avg_config_{suffix}.txt', avg_config, delimiter=',')

# Remove checkpoint if done
if os.path.exists(ckpt_file):
    os.remove(ckpt_file)
