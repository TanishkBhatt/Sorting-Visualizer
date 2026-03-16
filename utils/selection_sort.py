import time
from typing import Callable

def selection_sort(arr: list[int], update_plot: Callable):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        if arr[min_idx] < arr[i]:
            arr[min_idx], arr[i] = arr[i], arr[min_idx]
            update_plot(arr)
            time.sleep(0.5)