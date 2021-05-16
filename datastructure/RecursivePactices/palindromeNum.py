def isPalindrome(x) :
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    else:
        reverseX = 0
        temp = x
        i = 0
        while temp > 10:
            rem = temp % 10  # 记录最后一位数
            temp //= 10  # 记录除去最后一位数的剩余数
            i += 1  # 记录除了多少次
            reverseX = reverseX * 10 + rem

        if temp == 10:
            reverseX = reverseX * 100 + temp//10

        else:
            reverseX = reverseX*10 + temp

        if reverseX == x:
            return True
        return False

print(isPalindrome(9999))