import time
import random
import math

# Setting the random seed to 42 for computational reproducibility
random.seed(42)

def run_deterministic_sieve_study(limit):
    print(f"🚀 Starting Deterministic Sieve Network up to {limit:,}...")
    start_time = time.time()
    
    # Step 1: Standard Sieve to find base primes up to sqrt(limit)
    sqrt_limit = int(math.isqrt(limit))
    base_sieve = [True] * (sqrt_limit + 1)
    base_sieve[0] = base_sieve[1] = False
    for p in range(2, int(math.isqrt(sqrt_limit)) + 1):
        if base_sieve[p]:
            for i in range(p*p, sqrt_limit + 1, p):
                base_sieve[i] = False
    base_primes = [p for p, is_p in enumerate(base_sieve) if is_p]
    
    # Step 2: Segmented Sieve pipeline to extract sequential primes without memory overflow
    segment_size = max(5000000, sqrt_limit)
    low = 2
    high = segment_size
    
    window = []
    all_t_values = []
    total_primes_found = 0
    
    while low <= limit:
        if high > limit:
            high = limit
            
        segment = [True] * (high - low + 1)
        
        for p in base_primes:
            # Find the first multiple of p in the current segment
            start = max(p*p, ((low + p - 1) // p) * p)
            for j in range(start, high + 1, p):
                segment[j - low] = False
                
        # Process sequential primes from this segment directly into J-Rule window
        for i in range(low, high + 1):
            if segment[i - low]:
                total_primes_found += 1
                window.append(i)
                
                if len(window) > 4:
                    window.pop(0)
                    
                if len(window) == 4:
                    p4, p3, p2, p1 = window[0], window[1], window[2], window[3]
                    t_curr = abs((p1 - p4) - (p2 - p3))
                    all_t_values.append(t_curr)
                    
        low += segment_size
        high += segment_size

    print(f"   [Data Generation] Total Primes Extracted: {total_primes_found:,}")
    
    if len(all_t_values) < 6:
        print("❌ Not enough primes generated to form a 6-bit block.")
        return

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

    # Precise frequency calculation
    f_main = (hits_main / blocks_main) * 100 if blocks_main > 0 else 0
    f_shuff = (hits_shuff / blocks_shuff) * 100 if blocks_shuff > 0 else 0
    
    print("\n" + "="*55)
    print(f"🎯 DETERMINISTIC SIEVE ORDER FREQUENCY : {f_main:.6f}%")
    print(f"🎲 STOCHASTIC SHUFFLING CONTROL BASELINE: {f_shuff:.6f}%")
    print(f"📊 Total Evaluated 6-Bit Blocks        : {blocks_main}")
    print(f"⏱️ TOTAL PROCESSING TIME               : {time.time() - start_time:.2f}s")
    print("="*55)

# اجرای تست قطعی برای تمام اعداد اول زیر ۱۰ به توان ۸ برای راستی‌آزمایی اولیه سرعت
# شما می‌توانید این عدد را برای محدوده نهایی خود بزرگتر کنید.
run_deterministic_sieve_study(10**10)