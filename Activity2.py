def match_words(words):
    ctr = 0
    list1 = []
    for word in words:
        #Checking the first and las character of a list
        if len(word) > 1 and word[0]==word[-1]:
            ctr = ctr + 1
            #.append adds the value to a list
            list1.append(word)
    print("list of words with first and last characters same", list1)
    return ctr
count = match_words(["abc", "cat", "aba", "121"])
print("Number of words having first and last character same:", count)