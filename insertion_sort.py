def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key


Array = [40, 20, 10, 30, 50, 60, 90, 70, 80]
print("Array Before Sorting =",Array)
insertion_sort(Array)
print("Array After Sorting =",Array)
print("--------------------------------------------")
Array2 = [9,14,5,3,10,12,11,13,6,8,2,1,4,7]
print("Array Before Sorting =",Array2)
insertion_sort(Array2)
print("Array After Sorting =",Array2)
