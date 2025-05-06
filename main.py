import sys
def getBookText(path):
    with open(path) as f:
        bookText = f.read()
    return (bookText)

from stats import wordCount
from stats import letters

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        x = getBookText(sys.argv[1])
        wordCount(x)
        letters(x)

main()