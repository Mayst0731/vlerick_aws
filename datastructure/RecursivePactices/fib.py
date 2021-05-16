# # def fib(n):
# #     a = 0
# #     b = 1
# #
# #     for i in range(n):
# #         a, b = b, a+b
# #
# #     return a
#
# def fib_rec(n):
#     # Base Case
#     if n ==0 or n ==1:
#         return n
#     else:
#         return fib_rec(n-1) + fib_rec(n-2)
#
#
# print(fib_rec(10))

def sum_rec(n):
    if n == 1:
        return 1
    else:
        return n + sum_rec(n-1)


print(sum_rec(11))