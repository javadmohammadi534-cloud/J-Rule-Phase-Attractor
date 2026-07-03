# An Invariant Cross-Differential Phase Attractor in Prime Distributions and Riemann Zeta Zeros

This repository contains the official, verified open-source computational suite and data replication packages for the **J-Rule** non-linear second-order cross-differential operator analysis. This framework evaluates localized geometric configurations and spectral rigidity across deterministic arithmetic sequences, direct random matrix simulations, and stochastic noise baselines.

📂 Repository Structure
* **J-rule_Prime_Number.py**: Localized verification and asymptotic sweep network for prime distributions utilizing a probabilistic framework with fixed stochastic shuffling validation.
* **J-rule_Deterministic_Sieve.py**: The high-performance segmented sieve pipeline designed for the exact linear enumeration of the entire sequence of all 455,052,511 primes below $10^{10}$, yielding the absolute structural invariant frequency of 28.958549%.
* **J-rule_GUE_Simulator.py**: Quantum chaotic validation network utilizing the Gaussian Unitary Ensemble (GUE) Dyson's tridiagonal matrix formulation, mapping the J-Rule invariant directly to Random Matrix Theory (RMT) bulk spectra.
* **J-rule_Zero_Of_The_Riemann_Zeta_Function.py**: Spectral rigidity analysis network evaluating the non-trivial zeros of the Riemann Zeta function utilizing the Andrew Odlyzko reference datasets.
* **J-rule_White_Noise.py**: Rigorous Monte Carlo simulation benchmarking continuous random noise topologies (Gaussian, Laplace, Cauchy, Uniform, etc.) spanning 600,000,000 total samples (30 independent trials with 20,000,000 samples per run) to isolate the entropic floor baseline.
* **data/zeta_zeros_100k.txt**: Extracted dataset containing non-trivial zeros of the Riemann Zeta function for instant benchmark execution.

🛠️ Requirements
* Python 3.x
* NumPy (`pip install numpy`)
* SciPy (`pip install scipy`)

🚀 How to Execute
To reproduce the numerical results reported in the manuscript, clone the repository and execute any of the core architectural scripts:

```bash
# 1. Run the localized Prime Distribution analysis
python J-rule_Prime_Number.py

# 2. Run the exhaustive 10^10 Deterministic Sieve framework
python J-rule_Deterministic_Sieve.py

# 3. Run the Quantum Chaotic GUE Simulation
python J-rule_GUE_Simulator.py

# 4. Run the Riemann Zeta Zeros benchmark
python J-rule_Zero_Of_The_Riemann_Zeta_Function.py

# 5. Run the Rigorous Noise Calibration stress-test
python J-rule_White_Noise.py
⚔️ Dual-Arm Methodological FrameworkThe architecture of this repository is divided into two mathematically distinct arms to rigorously isolate deterministic order from maximum entropy:The Deterministic / Quantum Chaos Arm: Evaluates natural primes, Riemann zeros, and GUE bulk spectra. In this regime, the J-Rule uncovers a highly rigid, non-random correlation structure characterized by sharp phase attractor emergences locking at $\approx 28.9\%$ for primes, $\approx 31.41\%$ for GUE matrix simulations, and $\approx 32.2\%$ for Riemann Zeta zeros.The Information-Theoretic Noise Baseline Arm: Evaluates scrambled systems (via stochastic shuffling control tests) and pure continuous noise fields. Bound by entropy, these randomized sequences systematically destroy the geometric structure, causing the system to collapse to the entropy floor strictly within the [14.0% - 17.0%] channel (approximating the ~16% baseline).⚙️ Computational ReproducibilityIn accordance with open science standards, all stochastic components—such as shuffling pipelines and continuous chaotic noise fields—are bound to a fixed pseudorandom initialization seed (seed=42). Parallel execution across disparate hardware platforms will yield identical statistical frequencies and identical standard deviations down to the final reported decimal places.
