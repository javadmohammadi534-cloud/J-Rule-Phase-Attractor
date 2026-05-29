import time
import random

def j_rule_zeta_core(zeta_zeros):
    """
    Core J-Rule cross-differential operator for Riemann Zeta Zeros.
    Eliminates local consecutive intervals to evaluate the joint probability 
    field of non-consecutive spacings under strict statistical block independence.
    """
    bits = []
    t_prev = 0
    hits = 0
    total_evaluated_blocks = 0  # Rigid counter for the statistical denominator
    
    window = []
    processed = 0
    
    for current in zeta_zeros:
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

            # Non-overlapping 6-bit block evaluation for information-theoretic mapping
            if len(bits) >= 6:
                total_evaluated_blocks += 1  # Denominator increments only upon full block completion
                val1 = bits[0]*4 + bits[1]*2 + bits[2]
                val2 = bits[3]*4 + bits[4]*2 + bits[5]
                
                if val1 + val2 == 7:
                    hits += 1
                bits = bits[6:]  # Clearing buffer to preserve statistical independence

    final_percentage = (hits / total_evaluated_blocks) * 100 if total_evaluated_blocks > 0 else 0
    return final_percentage, total_evaluated_blocks

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
    orig_percent, groups_main = j_rule_zeta_core(zeros)
    orig_time = time.time() - t0
    print(f"✅ Original Sequence Done in {orig_time:.2f} seconds.")
    
    # Phase 2: Stochastic Shuffling Control Framework
    print(f"🔀 Shuffling the sequence for Noise-Validation test...")
    shuffled_zeros = list(zeros)
    
    # Fixed seed for computational reproducibility as stated in the methodology
    random.seed(42) 
    random.shuffle(shuffled_zeros)
    
    print(f"⚙️ Running J-Rule on Shuffled Sequence...")
    t1 = time.time()
    shuffled_percent, groups_shuff = j_rule_zeta_core(shuffled_zeros)
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
    FILE_PATH = 'C:/Users/user/Documents/zero)100k.txt'
    run_zeta_experiment(FILE_PATH)
