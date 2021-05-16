# None和str是不便对象，定义默认参数时，必须指向不便对象
def add_end(L=None):
    if L is None:
        L=[]
    L.append('end')
    print(L)
    return L


add_end([1, 2, 3])
add_end([4, 5, 6])
add_end()
add_end()
