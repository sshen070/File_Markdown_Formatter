def fileCleaner(fileName):
    # Opens the file with read permission
    readFile = open(fileName, "r")
    writeFile = open("cleanedFile.txt", "w")

    # Iterates through each line in the file
    for line in readFile:
        wordList = line.split()
        if not wordList:
            continue

        # If the line starts with '#' --> must be header
        if wordList[0].startswith("#"):
            # Determines the next index a new line is required
            nextLineValue = newLineHeader(wordList)
            for word in wordList[0:nextLineValue]:
                writeFile.write(word)
                if (word != wordList[nextLineValue - 1]):
                    writeFile.write(" ")
            writeFile.write("\n\n")

            for word in wordList[nextLineValue:]:
                writeFile.write(word)
                if (word != wordList[-1]):
                    writeFile.write(" ")
            writeFile.write("\n\n")
                


        # # Continues until all words in the line are processed
        # while (len(wordList) > 0):
        #     nextLineValue = nextNewLineRequired(wordList)
        #     writeFile.write("\n")
        #     del wordList[0:nextLineValue]

                
    readFile.close()
    writeFile.close()


# Determines the next index in wordList when a  new line is required
def newLineHeader(wordList):
    for word in range(len(wordList) - 1):
        # If '*' appears --> we have a list under a header list

        if wordList[word].startswith("*"):
            return word


        # # If first word is upper case & the second is lower --> issue with formating
        if (not wordList[word].islower() and wordList[word + 1].islower()):
            return word
        
    return len(wordList)
    