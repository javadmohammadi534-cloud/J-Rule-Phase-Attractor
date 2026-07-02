# An Invariant Cross-Differential Phase Attractor in Prime Distributions and Riemann Zeta Zeros

This repository contains the official, verified open-source computational suite and data replication packages for the $J\text{-Rule}$ non-linear cross-differential operator analysis. This framework evaluates higher-order correlation structures, information density, and spectral rigidity across both deterministic arithmetic sequences and stochastic/quantum chaotic ensembles.

---

## 📂 Repository Structure

* **`J-rule_Prime_Number.py`**: Localized verification and asymptotic sweep network for prime distributions utilizing an optimized Miller-Rabin probabilistic framework with fixed stochastic shuffling validation.
* **`J-rule-Deterministic-sieve.py`**: The high-performance segmented sieve pipeline designed for exhaustive, memory-efficient processing of the entire sequence of $\pi(10^{10})$ natural primes, yielding the absolute structural invariant frequency of **28.958549%**.
* **`J-rule-GUE-simulator.py`**: Quantum chaotic validation network utilizing the Gaussian Unitary Ensemble (GUE) tridiagonal matrix formulation, mapping the $J\text{-Rule}$ invariant directly to Random Matrix Theory (RMT) bulk spectra.
* **`J-rule_Zero-Of-The-Riemann-Zeta-Function.py`**: Spectral rigidity analysis network evaluating the non-trivial zeros of the Riemann Zeta function.
* **`J-rule_White_Noise.py`**: Rigorous Monte Carlo simulation benchmarking continuous random noise topologies (Gaussian, Laplace, Cauchy, Uniform, etc.) at extreme scales ($20 \times 10^6$ samples, 30 independent iterations) to isolate the universal asymptotic noise ceiling (~16%).
* **`data/zeta_zeros_100k.txt`**: Extracted dataset containing 100,000 non-trivial zeros of the Riemann Zeta function for instant benchmark execution.

---

## 🛠️ Requirements

* Python 3.x
* NumPy (`pip install numpy`)
* SciPy (`pip install scipy`)

---

## 🚀 How to Execute

To reproduce the numerical results reported in the manuscript, clone the repository and execute any of the core architectural scripts:

```bash
# 1. Run the localized Prime Distribution analysis
python J-rule_Prime_Number.py

# 2. Run the exhaustive 10^10 Deterministic Sieve framework
python deterministic_sieve_jrule.py

# 3. Run the Quantum Chaotic GUE Simulation
python gue_simulator_jrule.py

# 4. Run the Riemann Zeta Zeros benchmark
python J-rule_Zero-Of-The-Riemann-Zeta-Function.py

# 5. Run the Rigorous Noise Calibration stress-test (20M Samples)
python J-rule_White_Noise.py
 Dual-Arm Methodological FrameworkThe architecture of this repository is divided into two mathematically distinct arms to rigorously isolate order from maximum entropy:The Deterministic / Quantum Chaos Arm: Evaluates natural primes, Riemann zeros, and GUE bulk spectra. In this regime, the $J\text{-Rule}$ uncovers a highly rigid, non-random correlation structure characterized by a sharp phase attractor emergence at ~28.95%.The Information-Theoretic Noise Baseline Arm: Evaluates scrambled systems (via stochastic shuffling) and pure mathematical noise distributions. Bound by maximum entropy, these uncorrelated sequences consistently freeze at an asymptotic boundary of ~16.0% (analytically derived from a 6-bit Markovian configuration spaces where $\mathbb{P} \approx \frac{1}{6}$).⚙️ Computational ReproducibilityIn accordance with open science standards, all stochastic components—such as shuffling pipelines, randomized primality base generation, and continuous chaotic noise fields—are bound to a fixed pseudorandom initialization seed (seed=42). Parallel execution across disparate hardware platforms will yield identical statistical frequencies and identical standard deviations down to the final reported decimal places.
