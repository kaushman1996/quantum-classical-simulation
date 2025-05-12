# Quantum and Classical Simulation Codes

This repository contains three Python scripts for simulating quantum and classical lattice models using DMRG, Exact Diagonalization, and Classical Monte Carlo methods.

## Contents

- `dmrg.py`: DMRG simulation using the TeNPy library.
- `ed.py`: Exact diagonalization using QuSpin on an 18-site system with translational symmetry.
- `MC_global_move.py`: Classical Monte Carlo simulation with temperature as a runtime argument.

---

## 1. `dmrg.py`

Uses the [TeNPy](https://github.com/tenpy/tenpy) library to simulate **Model 2**, a 1D quantum lattice system.

**Features:**
- Computes expectation values of **charge** and **$S_z$**.
- Suitable for strongly correlated 1D systems.

**Requirements:**
```bash
pip install physics-tenpy



## 2. `ed.py`

Performs **Exact Diagonalization (ED)** for Model 1 — a chain of 18 sites with nearest-neighbor interactions, using the [QuSpin](https://github.com/weinbe58/QuSpin) library.

### Features
- Exploits **translational symmetry** to reduce Hilbert space size and improve performance.
- Computes the **full energy spectrum**.

### Usage
```bash
python ed.py

# Classical Monte Carlo Simulation with Global Moves

This script performs a **classical Monte Carlo (MC)** simulation.

## File: `MC_global_move.py`

### Description

Simulates a 2D classical doble gated potential  using global Monte Carlo moves at a specified temperature.

### Features

- Accepts **temperature** as a command-line argument.
- Tracks and visualizes the **energy evolution** during the simulation.

### Usage

Run the script from the command line with temperature as an argument:

```bash
python MC_global_move.py 0.07
