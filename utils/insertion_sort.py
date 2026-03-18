import time
from typing import Callable

def insertion_sort(arr: list[int], update_plot: Callable):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        update_plot(arr)
        time.sleep(0.5)

def insertion_sort_code():
    return """
def insertion_sort(arr: list[int]) -> list[int]:
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key 
    return arr  
"""