#12
for j in range(3):
    print("enter the n :")
    n = int(input())

    sum_cube= 0
    for i in range(n+1):
        sum_cube += i**3
    print('the sum of', n, 'is', sum_cube)