n = 5
def flippingBits(n):
    newerNum = []
    newNum = str(bin(n)[2:].zfill(32))
    for digit in newNum:
        if digit == "0":
            digit = "1"
            newerNum.append(digit)
        else:
            digit = "0"
            newerNum.append(digit)
    fixedNum = ""
    for item in newerNum:
        if newerNum.index == 0:
            fixedNum = item
        else:
            fixedNum = fixedNum + item
    finalNum = int(fixedNum, 2)
    print(finalNum)
    return finalNum
flippingBits(n)