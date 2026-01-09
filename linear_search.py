

"""
A simple implementation of linear search algorithm in Python.
Time complexity: O(n)
Space complexity: O(1)
"""

import numpy as np

def linear_search(array, target):
    for idx, value in enumerate(array):
        if value == target:
            return idx
    return None

if __name__ == "__main__":
    # we set the random array between 0 and 50 and 50 size (being consistent with choices)
    np.random.seed(42)
    bucket = np.arange(0,51)
    arr = np.random.choice(bucket, size=50, replace=False)

    for idx, value in enumerate(arr):
        print(f"Index: {idx}, Value: {value}")
    target = 38 #the only one excluded from the bucket
    response = linear_search(arr, target)
    print("="*30)
    if response is None:
        print("Value not found in the array")
    else:
        print(f"Value found un index {response}")
