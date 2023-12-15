strings = ['ab', 'ab', 'abc', 'bc', 'cd']
queries = ['ab', 'abc', 'bc', 'ac']
def matchingStrings(strings, queries):
    
    matching = []
    matcher = []

    for query in queries:
        numberCount = 0
        if query in strings:
            for string in strings:
                if string == query:
                    numberCount = numberCount + 1
            matching.append(query)
        else:
            matcher.append(query)
    
    for item in matcher:
        print(item)

    return(matching)

matchingStrings(strings=strings, queries=queries)