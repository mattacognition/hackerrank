s = "12:00:00PM"
def timeConversion(s):
    time = s.split(":")
    numArray = []
    newSentence = ""
    
    if "AM" in s:
        for word in time:
            if time.index(word) == 0:
                firstDigit = int(word)
                if firstDigit != 12 and firstDigit > 9:
                    number = str(firstDigit)
                if firstDigit == 12:
                    number = "00"
                if firstDigit < 10:
                    number = "0" + str(firstDigit)
                numArray.append(number)   
            else: 
                number = word
                numArray.append(number)

        for num in numArray:
            if numArray.index(num) == len(numArray) - 1:
                wordAgain = str(num.strip("AM"))
            else:
                wordAgain = str(num) + ":"
            newSentence = newSentence + wordAgain
        print(newSentence)

    if "PM" in s:
        for word in time:
            if time.index(word) == 0:
                firstDigit = int(word)
                if firstDigit != 12:
                    number = str(firstDigit + 12)
                else:
                    number = str(firstDigit)
            else:
                number = word
            numArray.append(number)
            
        for num in numArray:
            if numArray.index(num) == len(numArray) - 1:
                wordAgain = str(num.strip("PM"))
            else:
                wordAgain = str(num) + ":"
            newSentence = newSentence + wordAgain
        print(newSentence)    
        
    return newSentence

timeConversion(s)