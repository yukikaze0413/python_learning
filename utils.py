def find_max(arr):
    max = arr[0]
    for num in arr:
        if num > max:
            max = num
    print("The maximum number in the array is:", max)

