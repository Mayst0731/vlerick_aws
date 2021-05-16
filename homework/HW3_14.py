
print("How many numbers:")
n = int(input())

sum = 0
for j in range(n):
    print("enter the number :")
    num = int(input())
    sum += num

ave = sum / n
print("The average of", n, "numbers is", ave)