# def removeElement(A, elem):
#     # write your code here
#     if A == [] and elem == 0:
#         return 0
#     else:
#         n = []
#         for i in range(len(A)):
#             if A[i] != elem:
#                 n.append(A[i])
#         return len(n)
#
#
# l = [0, 4, 4, 0, 0, 2, 4, 4]
# a = 4
# r = removeElement(l, a)
# print(r)
#
# l2 = [0, 4, 4, 5, 5, 0, 0, 2, 4, 4]
# a2 = 5
# r2 = removeElement(l2, a2)
# print(r2)