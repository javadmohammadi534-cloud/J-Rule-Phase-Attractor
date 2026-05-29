# An Invariant Cross-Differential Phase Attractor in Prime Distributions and Riemann Zeta Zeros

This repository contains the official, verified Python implementations and data replication packages for the $J\text{-Rule}$ non-linear cross-differential operator analysis.

## Repository Structure
- `J-rule_Prime_Number.py`: Asymptotic sweep network for prime distributions with Miller-Rabin test and fixed stochastic shuffling validation (`seed=42`).
- `J-rule_Zero-Of-The-Riemann-Zeta-Function.py`: Spectral rigidity analysis network for non-trivial Riemann Zeta function zeros.
- `J-rule_White_Noise.py`: Rigorous Monte Carlo simulation benchmarking continuous random white noise topologies.
- `data/zeta_zeros_100k.txt`: Extracted dataset containing 100,000 non-trivial zeros of the Riemann Zeta function for instant benchmark execution.

## Requirements
- Python 3.x
- NumPy (`pip install numpy`)

## How to Execute
To reproduce the numerical results reported in the manuscript, clone the repository and run any of the core scripts:

```bash
# Run the Prime Distribution analysis
python J-rule_Prime_Number.py

# Run the Riemann Zeta Zeros benchmark
python J-rule_Zero-Of-The-Riemann-Zeta-Function.py

# Run the Rigorous Noise Calibration stress-test
python J-rule_White_Noise.py

Computational Reproducibility
In accordance with open science standards, all stochastic components (such as shuffling pipelines and continuous noise fields) are bound to a fixed pseudorandom initialization seed (seed=42). Execution across different platforms will yield identical statistical results up to the final reported decimal places.
