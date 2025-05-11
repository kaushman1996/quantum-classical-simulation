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

