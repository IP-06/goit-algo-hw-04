import timeit
import random

def insertion_sort(arr):
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

def merge_sort(arr):
    if len(arr) <= 1:
        return arr.copy()
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def measure_time(func, data, repeats=3):
    timer = timeit.Timer(lambda: func(data))
    return min(timer.repeat(repeat=repeats, number=1))

def run_tests():
    sizes = [10, 100, 1000]
    print(f"{'Розмір':<10} | {'Insertion':<12} | {'Merge':<12} | {'Timsort'}")
    print("-" * 55)

    for size in sizes:
        data = [random.randint(0, size) for _ in range(size)]
        
        t_insertion = measure_time(insertion_sort, data) if size <= 2000 else "N/A"
        t_merge = measure_time(merge_sort, data)
        t_timsort = measure_time(sorted, data)

        res_ins = f"{t_insertion:.5f}" if isinstance(t_insertion, float) else t_insertion
        print(f"{size:<10} | {res_ins:<12} | {t_merge:<12.5f} | {t_timsort:.5f}")

if __name__ == "__main__":
    run_tests()