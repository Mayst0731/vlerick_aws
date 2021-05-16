def bubble_sort(seq):
    # from the first to the last two
    for i in range(len(seq)-1):
        #from the first one to the unsorted one
        for j in range(0,len(seq)-i-1):
            if seq[j]>seq[j+1]:
                seq[j],seq[j+1] = seq[j+1],seq[j]
    return seq


print(bubble_sort([2,4,5,7,2,3,9,8]))



