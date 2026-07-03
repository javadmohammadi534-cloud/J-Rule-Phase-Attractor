import time
import numpy as np

# Setting the random seed to 42 for computational reproducibility as stated in the methodology
np.random.seed(42)

def j_rule_core_analyzer(signal):
    """
    Refined and robust J-Rule operator implementation.
    Evaluates linear deterministic structural order within numerical sequences 
    by minimizing finite-size effects and maintaining statistical block independence.
    """
    bits = []
    t_prev = 0
    hits = 0
    total_evaluated_blocks = 0  # Solid counter for the statistical frequency denominator
    
    window = []
    processed = 0
    
    for current in signal:
        window.append(current)
        if len(window) > 4: 
            window.pop(0)
            
        if len(window) == 4:
            p4, p3, p2, p1 = window[0], window[1], window[2], window[3]
            t_curr = abs((p1 - p4) - (p2 - p3))
            
            if processed > 0:
                bits.append(1 if t_curr > t_prev else 0)
            t_prev = t_curr
            processed += 1

            # 6-bit block evaluation (Non-overlapping windowing)
            if len(bits) >= 6:
                total_evaluated_blocks += 1
                val1 = bits[0]*4 + bits[1]*2 + bits[2]
                val2 = bits[3]*4 + bits[4]*2 + bits[5]
                if val1 + val2 == 7:
                    hits += 1
                bits = bits[6:]  # Clearing buffer to ensure statistical independence
            
    return (hits / total_evaluated_blocks) * 100 if total_evaluated_blocks > 0 else 0

def generate_and_analyze(noise_name, num_samples):
    """Generates stochastic white noise based on defined mathematical distributions."""
    if noise_name == 'Gaussian':
        signal = np.random.normal(0, 1, num_samples)
    elif noise_name == 'Uniform':
        signal = np.random.uniform(-1, 1, num_samples)
    elif noise_name == 'Laplace':
        signal = np.random.laplace(0, 1, num_samples)
    elif noise_name == 'Exponential-centered':
        signal = np.random.exponential(1, num_samples) - 1.0
    elif noise_name == 'Gamma-centered':
        signal = np.random.standard_gamma(2, num_samples) - 2.0
    elif noise_name == 'Logistic':
        signal = np.random.logistic(0, 1, num_samples)
    elif noise_name == 'Student-t (df=3)':
        signal = np.random.standard_t(3, num_samples)
    elif noise_name == 'Student-t (df=5)':
        signal = np.random.standard_t(5, num_samples)
    elif noise_name == 'Cauchy':
        signal = np.random.standard_cauchy(num_samples)
    else:
        signal = np.random.normal(0, 1, num_samples)
        
    return j_rule_core_analyzer(signal)

if __name__ == '__main__':
    # --- Stress-test configuration for baseline calibration ---
    NUM_RUNS = 30          # Independent iterations per noise topology
    NUM_SAMPLES = 20000000   # 20M samples per iteration
    
    noise_types = [
        'Gaussian', 'Uniform', 'Laplace', 'Exponential-centered', 
        'Gamma-centered', 'Logistic', 'Student-t (df=3)', 
        'Student-t (df=5)', 'Cauchy'
    ]
    
    print(f"🚀 Starting Rigorous Baseline Calibration (Linear Execution)...")
    print(f"📊 Config: {NUM_RUNS} runs per distribution, {NUM_SAMPLES:,} samples per run.\n")
    
    start_time = time.time()
    
    print("="*65)
    print(f"{'Noise Distribution':<25} | {'Mean (%)':<10} | {'Std Dev':<10}")
    print("-" * 65)
    
    # Linear sequential processing to ensure deterministic reproducibility
    for noise in noise_types:
        results = []
        for _ in range(NUM_RUNS):
            res = generate_and_analyze(noise, NUM_SAMPLES)
            results.append(res)
        
        mean_val = np.mean(results)
        std_val = np.std(results)
        
        print(f"🔹 {noise:<23} | {mean_val:>8.2f} % | {std_val:>7.2f}")
        
    print("="*65)
    print(f"⏱️ TOTAL TIME: {time.time() - start_time:.2f} seconds")
