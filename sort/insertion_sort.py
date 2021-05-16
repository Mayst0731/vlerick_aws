def insertion_sort(seq):
    for i in range(1,len(seq)):
        value = seq[i]

        # find a suitable slot
        pos = i
        while pos>0 and value<seq[pos-1]:
            seq[pos] = seq[pos-1]
            pos -= 1
        seq[pos] = value
    return seq

print(insertion_sort([2,4,5,7,2,3,9,8]))

