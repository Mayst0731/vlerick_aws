
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def sumNumbers(root) -> int:

    res = []

    def helper(root, cur_sum, res):

        if not root.left and not root.right:
            cur_sum += root.val
            res.append(cur_sum)

        cur_sum += cur_sum + root.val

        if root.left:
            helper(root.left, cur_sum * 10, res)
        if root.right:
            helper(root.right, cur_sum * 10, res)

    cur_sum = 0
    helper(root, cur_sum, res)

    sum = 0
    for num in res:
        sum += num
    return sum

def main():
    root = TreeNode(5)
    root.left = TreeNode(9)
    root.right = TreeNode(0)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(1)
    print("Total Sum of Path Numbers: " + str(sumNumbers(root)))


main()




