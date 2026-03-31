import time
import random
import heapq
from typing import List, Tuple

def generate_sales_data(count: int = 10000) -> List[Tuple[int, int]]:
    """Generates a large list of (day, amount) tuples."""
    return [(i, random.randint(100, 10000)) for i in range(count)]

def find_top_sales_days(data: List[Tuple[int, int]], top_n: int = 5) -> Tuple[List[Tuple[int, int]], float]:
    """
    Finds the top N sales days efficiently.
    
    Optimized from O(N * N log N) with artificial delays to O(N log K) using a heap,
    where K is top_n. For small K relative to N, this is exceptionally fast.
    """
    start_time = time.time()
    
    # FIXED (Performance): Use heapq.nlargest for O(N log K) complexity.
    # This avoids sorting the entire list and is much faster for finding a few top items.
    top_days = heapq.nlargest(top_n, data, key=lambda x: x[1])
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    return top_days, execution_time

if __name__ == "__main__":
    print("Generating 1,000,000 sales records...")
    data = generate_sales_data(1000000)
    
    print(f"Finding top 5 performing days...")
    top, duration = find_top_sales_days(data, 5)
    
    print("\n--- Sales Report ---")
    for rank, (day, amount) in enumerate(top, 1):
        print(f"Rank {rank}: Day {day} with ${amount:,}")
    
    print(f"\nExecution time: {duration:.6f} seconds")
    if duration < 0.1:
        print("PERFORMANCE STATUS: OPTIMIZED ✅")
    else:
        print("PERFORMANCE STATUS: NEEDS WORK ⚠️")
