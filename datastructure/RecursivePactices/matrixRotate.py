def rotate(matrix):
    """
    Do not return anything, modify matrix in-place instead.

    """
    rotate_number = len(matrix) // 2
    layer = 0

    while layer <= rotate_number:
        top_left = matrix[layer][layer]
        top_right = matrix[layer][-(layer + 1)]
        bottom_left = matrix[-(layer + 1)][layer]
        bottom_right = matrix[-(layer + 1)][-(layer + 1)]



        matrix[layer][layer] = bottom_left
        matrix[-(layer + 1)][layer] = bottom_right
        matrix[-(layer + 1)][-(layer + 1)] = top_right
        matrix[layer][-(layer + 1)] = top_left

        layer += 1
    return matrix

matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
print('answer is [[7,4,1],[8,5,2],[9,6,3]]')
print(matrix)
print(rotate(matrix))