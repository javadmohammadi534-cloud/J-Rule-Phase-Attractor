import numpy as np
import time
import random
from scipy.linalg import eigvalsh_tridiagonal

# Setting the random seed to 42 for computational reproducibility as stated in the methodology
random.seed(42)
np.random.seed(42)

def run_gue_study_with_shuffle(num_t_values):
    print(f"🚀 Starting Research Network for GUE Simulation (Targets: {num_t_values} T_i values)...")
    start_time = time.time()
    
    all_t_values = []
    batch_size = 50000  # Dyson matrix dimension to ensure statistical stability
    processed_count = 0
    
    # Phase 1: Generating cross-differential gaps T_i from GUE bulk spectrum
    while len(all_t_values) < num_t_values:
        N = batch_size
        diagonal = np.random.normal(0, 1, N)
        degrees_of_freedom = 2 * np.arange(1, N)  # Beta = 2 for Gaussian Unitary Ensemble
        off_diagonal = np.sqrt(np.random.chisquare(degrees_of_freedom)) / np.sqrt(2.0)
        
        eigs = eigvalsh_tridiagonal(diagonal, off_diagonal)
        
        # Unfolding the central bulk spectrum based on Wigner's semicircle law
        R = 2.0 * np.sqrt(N / 2.0)
        start, end = int(0.40 * N), int(0.60 * N)
        bulk_eigs = eigs[start:end]
        
        unfolded_eigs = []
        for x in bulk_eigs:
            if -R < x < R:
                cdf = 0.5 + (x * np.sqrt(R**2 - x**2)) / (np.pi * R**2) + np.arcsin(x / R) / np.pi
                unfolded_eigs.append(cdf * (N / 2.0))
                
        # Extracting variables T_i using a 4-point moving window
        zeros = np.array(unfolded_eigs)
        for i in range(len(zeros) - 3):
            p4, p3, p2, p1 = zeros[i], zeros[i+1], zeros[i+2], zeros[i+3]
            t_curr = abs((p1 - p4) - (p2 - p3))
            all_t_values.append(t_curr)
            
            processed_count += 1
            if len(all_t_values) >= num_t_values:
                break
                
        if len(all_t_values) % 20000 == 0 or len(all_t_values) >= num_t_values:
            current_progress = min(len(all_t_values), num_t_values)
            print(f"   [Data Generation] Processed {current_progress} GUE variables...")

    # Trim to exact target size required for the evaluation framework
    all_t_values = all_t_values[:num_t_values]

    # Phase 2: Evaluation of frequency on the main sequence (Deterministic Order)
    bits_main = []
    hits_main = 0
    blocks_main = 0
    for i in range(1, len(all_t_values)):
        bits_main.append(1 if all_t_values[i] > all_t_values[i-1] else 0)
        if len(bits_main) >= 6:
            blocks_main += 1
            val1 = bits_main[0]*4 + bits_main[1]*2 + bits_main[2]
            val2 = bits_main[3]*4 + bits_main[4]*2 + bits_main[5]
            if val1 + val2 == 7:
                hits_main += 1
            bits_main = bits_main[6:]

    # Phase 3: Stochastic shuffling control test
    shuffled_t_values = all_t_values.copy()
    random.shuffle(shuffled_t_values)  # Randomizing the temporal order of gaps
    
    bits_shuff = []
    hits_shuff = 0
    blocks_shuff = 0
    for i in range(1, len(shuffled_t_values)):
        bits_shuff.append(1 if shuffled_t_values[i] > shuffled_t_values[i-1] else 0)
        if len(bits_shuff) >= 6:
            blocks_shuff += 1
            val1 = bits_shuff[0]*4 + bits_shuff[1]*2 + bits_shuff[2]
            val2 = bits_shuff[3]*4 + bits_shuff[4]*2 + bits_shuff[5]
            if val1 + val2 == 7:
                hits_shuff += 1
            bits_shuff = bits_shuff[6:]

    # Precise frequency calculation
    f_main = (hits_main / blocks_main) * 100 if blocks_main > 0 else 0
    f_shuff = (hits_shuff / blocks_shuff) * 100 if blocks_shuff > 0 else 0
    
    print("\n" + "="*55)
    print(f"🎯 DETERMINISTIC GUE ORDER FREQUENCY   : {f_main:.6f}%")
    print(f"🎲 STOCHASTIC SHUFFLING CONTROL BASELINE: {f_shuff:.6f}%")
    print(f"📊 Total Evaluated 6-Bit Blocks         : {blocks_main}")
    print(f"⏱️ TOTAL PROCESSING TIME                : {time.time() - start_time:.2f}s")
    print("="*55)

# Execution with 20,000 samples for verification matching the prime study scale
run_gue_study_with_shuffle(20000)

