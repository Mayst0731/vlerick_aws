def select_sort(seq):
    for i in range(len(seq)):
        min_index = i
        for j in range(i+1,len(seq)):
            if seq[j] < seq[min_index]:
                min_index = j

        if min_index != i:
            seq[i],seq[min_index] = seq[min_index],seq[i]
    return seq

print(select_sort([2,4,5,7,2,3,9,8]))
