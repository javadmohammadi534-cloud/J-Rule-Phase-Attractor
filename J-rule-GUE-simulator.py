import numpy as np
import time
import random
from scipy.linalg import eigvalsh_tridiagonal

# Setting the random seed to 42 for computational reproducibility
random.seed(42)
np.random.seed(42)

def run_gue_study_with_shuffle(num_t_values):
    print(f"Executing Verified GUE Simulation Network (Target: {num_t_values:,} variables)...")
    start_time = time.time()
    
    all_t_values = []
    # N=5000 is mathematically optimal for thermodynamic limit stability without O(N^2) scaling collapse
    batch_size = 5000  
    
    # Phase 1: Generating cross-differential gaps T_i from standard GUE bulk spectrum
    while len(all_t_values) < num_t_values:
        N = batch_size
        diagonal = np.random.normal(0, 1, N)
        # Standard degrees of freedom scaling for GUE (beta=2) Dumitriu-Edelman tridiagonal matrix
        degrees_of_freedom = 2 * np.arange(N - 1, 0, -1)
        off_diagonal = np.sqrt(np.random.chisquare(degrees_of_freedom)) / np.sqrt(2.0)
        
        # Computing eigenvalues
        eigs = eigvalsh_tridiagonal(diagonal, off_diagonal)
        
        # Exact Wigner Semicircle boundary for specified variance
        R = np.sqrt(4.0 * N)
        
        # Strict extraction of the central bulk spectrum (40% to 60%) to avoid edge effects
        start_idx, end_idx = int(0.40 * N), int(0.60 * N)
        bulk_eigs = eigs[start_idx:end_idx]
        
        unfolded_eigs = []
        for x in bulk_eigs:
            if -R < x < R:
                # Wigner Semicircle Cumulative Distribution Function (CDF)
                cdf = 0.5 + (x * np.sqrt(R**2 - x**2)) / (np.pi * R**2) + np.arcsin(x / R) / np.pi
                # Multiplying strictly by N to normalize mean local spacing to <s> = 1
                unfolded_eigs.append(cdf * N)
                
        # Extracting variables T_i using the 4-point moving window
        zeros = np.array(unfolded_eigs)
        
        previous_length = len(all_t_values)
        for i in range(len(zeros) - 3):
            p4, p3, p2, p1 = zeros[i], zeros[i+1], zeros[i+2], zeros[i+3]
            t_curr = abs((p1 - p4) - (p2 - p3))
            all_t_values.append(t_curr)
            
            if len(all_t_values) >= num_t_values:
                break
                
        current_length = len(all_t_values)
        # Printing progress effectively
        if (current_length // 10000) > (previous_length // 10000) or current_length >= num_t_values:
            print(f"   [Data Generation] Processed {current_length:,} / {num_t_values:,} GUE variables...")

    # Strict truncation to exact target
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
    random.shuffle(shuffled_t_values)
    
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

    f_main = (hits_main / blocks_main) * 100 if blocks_main > 0 else 0
    f_shuff = (hits_shuff / blocks_shuff) * 100 if blocks_shuff > 0 else 0
    
    print("\n" + "="*55)
    print(f"🎯 DETERMINISTIC GUE ORDER FREQUENCY   : {f_main:.6f}%")
    print(f"🎲 STOCHASTIC SHUFFLING CONTROL BASELINE: {f_shuff:.6f}%")
    print(f"📊 Total Evaluated 6-Bit Blocks         : {blocks_main:,}")
    print(f"⏱️ TOTAL PROCESSING TIME                : {time.time() - start_time:.2f}s")
    print("="*55)

# Executing strict generation of 100,000 statistical variables
run_gue_study_with_shuffle(100000)

