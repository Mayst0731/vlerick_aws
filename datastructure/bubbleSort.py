

def bubbleSort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(n-i-1):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1], lst[j]
    return lst


arr = [90,64, 34, 25, 22, 12, 11]

print(bubbleSort(arr))