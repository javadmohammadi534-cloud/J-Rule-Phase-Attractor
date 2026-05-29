import time
import random

# Setting the random seed to 42 for computational reproducibility as stated in the methodology
random.seed(42)

def is_prime_fast(n):
    if n < 2: return False
    primes_under_500 = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 
        73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 
        157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 
        239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 
        331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 
        421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499
    ]
    if n in primes_under_500: return True
    if any(n % p == 0 for p in primes_under_500): return False
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for _ in range(15):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1: continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1: break
        else: return False
    return True

def run_optimized_prime_study_with_shuffle(power_of_ten, num_primes):
    print(f"🚀 Starting Research Network at 10^{power_of_ten} (Primes: {num_primes})...")
    start_time = time.time()
    
    current = 10**power_of_ten
    window = [] 
    all_t_values = [] # Store all T_i values for shuffling test
    processed_count = 0

    # Phase 1: Generating cross-differential gaps T_i from natural prime distribution
    while processed_count < num_primes:
        current = current + 1 if current % 2 == 0 else current + 2
        while not is_prime_fast(current):
            current += 2
        
        window.append(current)
        if len(window) > 4: window.pop(0) 
        
        if len(window) == 4:
            p4, p3, p2, p1 = window[0], window[1], window[2], window[3]
            t_curr = abs((p1 - p4) - (p2 - p3))
            all_t_values.append(t_curr)
            processed_count += 1
            
            if processed_count % 20000 == 0:
                print(f"   [Data Generation] Processed {processed_count} primes...")

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
    random.shuffle(shuffled_t_values) # Randomizing the temporal order of gaps
    
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
    print(f"🎯 DETERMINISTIC PRIME ORDER FREQUENCY : {f_main:.6f}%")
    print(f"🎲 STOCHASTIC SHUFFLING CONTROL BASILINE: {f_shuff:.6f}%")
    print(f"📊 Total Evaluated 6-Bit Blocks        : {blocks_main}")
    print(f"⏱️ TOTAL PROCESSING TIME               : {time.time() - start_time:.2f}s")
    print("="*55)

# Execution with 20,000 samples for verification
run_optimized_prime_study_with_shuffle(30, 20000)