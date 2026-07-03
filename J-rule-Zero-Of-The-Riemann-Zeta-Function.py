import time
import random

def j_rule_zeta_core(zeta_zeros):
    """
    Core J-Rule cross-differential operator for Riemann Zeta Zeros.
    Eliminates local consecutive intervals to evaluate the joint probability 
    field of non-consecutive spacings under strict statistical block independence.
    """
    # Strict 100% synchronized pipeline matching the prime-number logic
    window = []
    all_t_values = []

    # Phase 1: Generating cross-differential gaps T_i from spectral distribution
    for current in zeta_zeros:
        window.append(current)
        if len(window) > 4: 
            window.pop(0)
            
        if len(window) == 4:
            p4, p3, p2, p1 = window[0], window[1], window[2], window[3]
            t_curr = abs((p1 - p4) - (p2 - p3))
            all_t_values.append(t_curr)

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
            bits_main = bits_main[6:]  # Clearing buffer to preserve statistical independence

    return hits_main, blocks_main, all_t_values

def run_zeta_experiment(file_path):
    """
    Executes the J-Rule sweep over the Riemann Zeta non-trivial zeros 
    and validates against a stochastic shuffling control baseline.
    """
    print(f"🚀 Loading Riemann Zeta Zeros from dataset...")
    start_time = time.time()
    
    zeros = []
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    zeros.append(float(line))
                except ValueError:
                    continue 
                    
    total_zeros = len(zeros)
    print(f"📊 Successfully Loaded {total_zeros:,} zeros.")
    print(f"⚙️ Environment initialized. Running J-Rule on Original Sequence...")
    
    # Phase 1: Evaluation of the deterministic spectral sequence
    t0 = time.time()
    hits_main, groups_main, all_t_values = j_rule_zeta_core(zeros)
    orig_percent = (hits_main / groups_main) * 100 if groups_main > 0 else 0
    orig_time = time.time() - t0
    print(f"✅ Original Sequence Done in {orig_time:.2f} seconds.")
    
    # Phase 2: Stochastic Shuffling Control Framework
    print(f"🔀 Shuffling the sequence for Noise-Validation test...")
    shuffled_t_values = all_t_values.copy()
    
    # Fixed seed for computational reproducibility as stated in the methodology
    random.seed(42) 
    random.shuffle(shuffled_t_values)
    
    print(f"⚙️ Running J-Rule on Shuffled Sequence...")
    t1 = time.time()
    
    bits_shuff = []
    hits_shuff = 0
    groups_shuff = 0
    for i in range(1, len(shuffled_t_values)):
        bits_shuff.append(1 if shuffled_t_values[i] > shuffled_t_values[i-1] else 0)
        if len(bits_shuff) >= 6:
            groups_shuff += 1
            val1 = bits_shuff[0]*4 + bits_shuff[1]*2 + bits_shuff[2]
            val2 = bits_shuff[3]*4 + bits_shuff[4]*2 + bits_shuff[5]
            if val1 + val2 == 7:
                hits_shuff += 1
            bits_shuff = bits_shuff[6:]

    shuffled_percent = (hits_shuff / groups_shuff) * 100 if groups_shuff > 0 else 0
    shuffled_time = time.time() - t1
    print(f"✅ Shuffled Sequence Done in {shuffled_time:.2f} seconds.")
    
    print("\n" + "="*65)
    print(f"🎯 RIEMANN ZETA ZEROS J-RULE BENCHMARK REPORT")
    print("="*65)
    print(f"🔹 Total Zeros Analyzed      : {total_zeros:,}")
    print(f"🔹 Main 6-Bit Blocks         : {groups_main:,}")
    print(f"🔹 Shuffled 6-Bit Blocks     : {groups_shuff:,}")
    print(f"📈 ORIGINAL PERCENTAGE      : {orig_percent:.6f} %")
    print(f"📉 SHUFFLED PERCENTAGE      : {shuffled_percent:.6f} % (Expected Entropy Floor)")
    print(f"⏱️ TOTAL ELAPSED TIME       : {time.time() - start_time:.2f} seconds")
    print("="*65 + "\n")

if __name__ == '__main__':
    # DATA INGESTION NOTE: Ensure the file contains one non-trivial zero per line
    # (e.g., Andrew Odlyzko's standard reference formats).
    # Modify the FILE_PATH to point to your local text dataset.
    FILE_PATH = 'C:data/zeta_zeros_100k.txt'
    run_zeta_experiment(FILE_PATH)

