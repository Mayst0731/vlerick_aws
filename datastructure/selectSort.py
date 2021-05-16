def selectSort(lst):
    for i in range(len(lst)):
        min_idx = i
        for j in range(i,len(lst)):
            if(lst[j]<lst[min_idx]):
                min_idx = j
        lst[i],lst[min_idx] = lst[min_idx],lst[i]

    return lst


print(selectSort([5,8,12,3,7]))