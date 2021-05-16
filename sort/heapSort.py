def sift_down(array,start,end):

    while True:
        left_child = 2*start+1

        if left_child > end:
            break

        if left_child+1<= end and array[left_child+1]>array[left_child]:
            left_child += 1

        if array[left_child]>array[start]:
            array[left_child], array[start] = array[start],array[left_child]

            start = left_child

        else:
            break

def heap_sort(array):
    # initialize max_heap
    first = len(array)//2 - 1 # the last node which has at least one child

    # from the bottom to the top
    for i in range(first,-1,-1):
        # initialize a max_heap
        sift_down(array,i,len(array)-1)

    for head_end in range(len(array)-1,0,-1):
        array[head_end],array[0] = array[0],array[head_end]
        sift_down(array,0,head_end-1)

    return array


print(heap_sort([16,7,3,20,17,8]))







