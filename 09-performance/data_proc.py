import time
import random

def generate_sales_data(count=10000):
    """Generates a large list of (day, amount) tuples."""
    return [(i, random.randint(100, 1000)) for i in range(count)]

def find_top_sales_days(data, top_n=5):
    """
    BUG (Performance): Highly inefficient algorithm to find top N elements.
    It sorts the entire list multiple times or uses a nested loop unnecessarily.
    Attendee's Goal: Optimize this to used heapq or a single sort.
    """
    start_time = time.time()
    
    # Inefficient approach: 
    # For every rank we want (1st, 2nd, 3rd...), we sort the whole list and pick the i-th element.
    # This is O(N * N log N) instead of O(N log N).
    top_days = []
    
    # Intentionally bad logic:
    temp_data = list(data)
    for i in range(top_n):
        # We sort the whole list in every iteration of the loop!
        temp_data.sort(key=lambda x: x[1], reverse=True)
        top_days.append(temp_data[i])
        # Simulate some extra lag per step
        time.sleep(0.5) 
         
    end_time = time.time()
    return top_days, end_time - start_time
