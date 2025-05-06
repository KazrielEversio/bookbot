def getBookText(path):
    with open(path) as f:
        bookText = f.read()
    return (bookText)

from stats import wordCount

def main():
    x = getBookText("./books/frankenstein.txt")
    wordCount(x)

main()