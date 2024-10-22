def fab(n):
    if n <= 0:
        return 'Invalid input'
    elif n == 1:
        return 0
    else:
        a, b = 0, 1
        fab_list = [0, 1]
        for i in range(n-2):
            a, b = b, a+b
            fab_list.append(b)
        return fab_list


n = int(input("Enter the number of terms: "))
print(fab(n))