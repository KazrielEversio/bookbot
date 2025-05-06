def wordCount(bookText):
    num_words = len(bookText.split())
    print("Found", num_words, "total words")
    return(bookText)

def letters(bookText):
    letters = bookText.lower()
    lettersDict = {}
    for char in letters:
        if char.isalpha():
            lettersDict[char] = lettersDict.get(char, 0) + 1
    items = list(lettersDict.items())
    items.sort(key=lambda x: x[1], reverse=True)
    sortedLetters = dict(items)

    for char, count in sortedLetters.items():
        print(f"{char}: {count}")