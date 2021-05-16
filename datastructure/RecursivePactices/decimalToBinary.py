def decimalToBinary(testVariable):
    # Write your code here
    # Base Case
    if (testVariable == 0) or (testVariable == 1):
        return str(testVariable)

    # Recursive Case
    else:
        if testVariable % 2 == 0:
            return str(decimalToBinary(testVariable // 2)) + '0'
        else:
            return str(decimalToBinary((testVariable - 1) // 2)) + '1'

for i in range(12):
    print(" i Decimal is: ",decimalToBinary(i))