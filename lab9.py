# Jacob Wright
# Trevor Waite


# define a funtion that will sort the word.  word will be passed through it as parameter.
def sortLetters(word):
    word = word.lower()
    # make the word into a list so that it can be changed
    listWord = list(word)
    # sort the letters in the word
    listWord.sort()
    # join letters back together
    return ''.join(listWord)

def createDictionary(fileName, dictionary):
    # open the file
    fileHandle = open(fileName, 'r')
    # read a line
    for line in fileHandle:
        line = line.strip()
        word = line.lower()
        # determine if word starts with v
        if word[0] == 'v':
            # process line into word
            sortedWord = sortLetters(word)
            # key is sorted letters, value is the word
            # add to dictionary
            dictionary[sortedWord] = word
    fileHandle.close()

def findAnagrams(fileName, dictionary):
    # open quizwords.txt
    fileHandle = open(fileName, 'r')
    for line in fileHandle:
        line = line.strip()
        line = line.strip(',')
        quizWord = line.lower()
        print(quizWord, dictionary[sortLetters(quizWord)])
    fileHandle.close()

    
def main():
    aDict = {}
    filename = 'wordList.txt'
    quizListName = 'quizwords.txt'
    createDictionary(filename, aDict)
    findAnagrams(quizListName, aDict)
    
main()