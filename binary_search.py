
import numpy as np 

def binary_search(array, target):
    high = len(array) - 1 
    low = 0
    while low <=high:
        mid = low + (high-low)//2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        elif array[mid] > target:
            high = mid - 1
    return None

if __name__ == "__main__":
    # we set the random array between 0 and 50 and 50 size (being consistent with choices)
    np.random.seed(42)
    bucket = np.arange(1,51)
    arr = np.random.choice(bucket, size=50, replace=False)
    arr.sort()
    target = 40
    print(f"Array = {arr}")
    result = binary_search(arr,target)
    if result is not None:
        print (f"The target {target} is in index {result}")
    else:
        print(f"Targe number [{target}] is not found ")
    

