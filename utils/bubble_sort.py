import time
from typing import Callable

def bubble_sort(arr: list[int], update_plot: Callable):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-1-i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            update_plot(arr)
            time.sleep(0.5)

def bubble_sort_code():
    return """
def bubble_sort(arr: list[int]) -> list[int]:
    n = len(arr)
    for i in range(n):
        for j in range(0, n-1-i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] 
    return arr
"""