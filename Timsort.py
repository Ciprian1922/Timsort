import time
import random

def insertion_sort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    for i in range(left + 1, right + 1):
        key_item = arr[i]
        j = i - 1
        while j >= left and arr[j] > key_item:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item

    return arr

def merge(left, right):
    if not left:
        return right

    if not right:
        return left

    if left[0] < right[0]:
        return [left[0]] + merge(left[1:], right)

    return [right[0]] + merge(left, right[1:])

def merge_sort(arr):
    if len(arr) <= 20:
        return insertion_sort(arr)

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def timsort(arr):
    t_start = time.perf_counter()

    min_run = 32
    n = len(arr)

    for i in range(0, n, min_run):
        insertion_sort(arr, i, min((i + min_run - 1), n - 1))

    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (n - 1))

            merged_array = merge(
                left=arr[start:midpoint + 1],
                right=arr[midpoint + 1:end + 1]
            )
            arr[start:start + len(merged_array)] = merged_array

        size *= 2

    t_end = time.perf_counter()

    return arr, t_end - t_start

def generate_almost_sorted_array(n, num_swaps):
    arr = list(range(n))
    for i in range(num_swaps):
        a, b = random.randint(0, n-1), random.randint(0, n-1)
        arr[a], arr[b] = arr[b], arr[a]
    return arr

def generate_reverse_almost_sorted_array(n, num_swaps):
    arr = list(range(n))
    for i in range(num_swaps):
        a, b = random.randint(0, n-1), random.randint(0, n-1)
        arr[a], arr[b] = arr[b], arr[a]
    return arr[::-1]
def generate_duplicates(n, num_swaps, num_duplicates):
    arr = list(range(n))
    for i in range(num_swaps):
        a, b = random.randint(0, n-1), random.randint(0, n-1)
        arr[a], arr[b] = arr[b], arr[a]
    for i in range(num_duplicates):
        idx = random.randint(0, n-1)
        arr[idx] = random.randint(0, n-1)
    return arr


list_len = 100
#RANDOM ARRAY
# arr = list(range(list_len))
# random.shuffle(arr)

#ALMOST SORTED
# num_swaps = 50
# arr = generate_almost_sorted_array(list_len, num_swaps)
# sorted_arr, exec_time = timsort(arr)

#REVERSE ALMOST SORTED
# num_swaps = 50
# arr = generate_reverse_almost_sorted_array(list_len, num_swaps)
# sorted_arr, exec_time = timsort(arr)


#ARRAY WITH DUPLICATES 10, 20, 30, 75
num_swaps = 30  #depending on the list_len value, we can adjust from here how many swaps we want our duplicates to have
num_duplicates = 30 #we can also change the value of the duplicates
arr = generate_duplicates(list_len, num_swaps, num_duplicates)
sorted_arr, exec_time = timsort(arr)

print(sorted_arr)
precision_size = 100
while precision_size:
    print(f"{exec_time:.10f}")
    precision_size = precision_size - 1
    #random.shuffle(arr)
    #arr = generate_almost_sorted_array(list_len, num_swaps)
    #arr = generate_reverse_almost_sorted_array(list_len, num_swaps)
    arr = generate_duplicates(list_len, num_swaps, num_duplicates)
    sorted_arr, exec_time = timsort(arr)
