# Quantum and Classical Simulation Codes

This repository contains three Python scripts for simulating quantum and classical lattice models using DMRG, Exact Diagonalization, and Classical Monte Carlo methods.

## Contents

- `dmrg.py`: DMRG simulation using the TeNPy library.
- `ed.py`: Exact diagonalization using QuSpin on an 18-site system with translational symmetry.
- `MC_global_move.py`: Classical Monte Carlo simulation with temperature as a runtime argument.

---

## 1. `dmrg.py`

Uses the [TeNPy](https://github.com/tenpy/tenpy) library to simulate Model 4

**Features:**
- Computes expectation values of **charge** and **$S_z$**.


## 2. `ed.py`

Performs **Exact Diagonalization (ED)** for Model 1 using the [QuSpin](https://github.com/weinbe58/QuSpin) library.

**Features:**
- Exploits **translational symmetry** to reduce Hilbert space size and improve performance.
- Computes the **full energy spectrum**.



## 3. `MC_global_move.py`

### Description

Simulates a 2D classical double gated potential using global Monte Carlo moves at a specified temperature.

### Features

- Accepts **temperature** as a command-line argument.
- Tracks and visualizes the **energy evolution** during the simulation.
