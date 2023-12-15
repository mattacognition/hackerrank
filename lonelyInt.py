a = [1, 2, 3, 4, 3, 2, 1, 2]
b = a

def lonelyinteger(a):

    noMatch = []
    match = []

    for number in b:
        numberCount = 0
        if number in a:
            for digit in a:
                if digit == number:
                    numberCount = numberCount + 1
            if numberCount == 1:
                noMatch.append(number)
        else:
            match.append(number)
    
    for item in noMatch:
        print(item)
    return(noMatch)

lonelyinteger(a)