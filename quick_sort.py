def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr.pop(0)
    less = [a for a in arr if a <= pivot]
    bigger = [a for a in arr if a > pivot]
    return quick_sort(less) + [pivot] + quick_sort(bigger)


print(quick_sort([4, 6, 6, 1, 9, 5]))