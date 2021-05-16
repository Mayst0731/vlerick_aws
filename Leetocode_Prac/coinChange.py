def coinChange(coins, amount: int) -> int:
    def helper(coins, amount, i):
        if amount == 0:
            return
        if amount < 0:
            countlist[i] = -1
            return

        else:
            for coin in coins:
                countlist[i] += 1
                helper(coins, amount - coin, i)
                return

    countlist = [float('inf')] * len(coins)

    for i in range(len(coins)):
        helper(coins, amount, i)

    minC = amount
    for i in range(len(countlist)):
        if countlist[i] < minC:
            minC = countlist[i]

    return minC


print(coinChange([1,2,5],11))