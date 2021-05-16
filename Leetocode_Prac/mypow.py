def myPow(x,n):

    def helper(x,cur,n):

        if n == 1:
            return cur*cur


        if n%2 == 1:
            res = x*helper(x,cur,n-1)

        else:

            res = helper(x,cur*cur,n//2)
        return res
    return helper(x,x,n)

print(myPow(2,5))

