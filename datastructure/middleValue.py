def find_mid(lst):
    # Write your code here
    if lst.get_head() is None:
        return None
    temp = lst.get_head()
    i = 1
    while temp:
            temp = temp.next_element
            i += 1
    lst_len = i + 1
    if lst_len % 2 == 0:
        mid_step = lst_len // 2 - 1
    else:
        mid_step = lst_len // 2

    fir = lst.get_head()
    while mid_step > 0:
        fir = fir.next_element
        mid_step -= 1

    return fir.data