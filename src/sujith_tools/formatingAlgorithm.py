def fileCleaner(fileName):
    # Opens the file with read permission
    readFile = open(fileName, "r")
    writeFile = open("cleanedFile.txt", "w")

    # Iterates through each line in the file
    for line in readFile:
        wordList = line.strip().split()
        print(wordList)
        if not wordList:
            continue

        # If the line starts with '#' --> must be header
        if wordList[0].startswith("#"):
            # Determines the next index a new line is required
            nextLineValue = bulletTracker(wordList) 

            writeFile.write(" ".join(wordList[0:nextLineValue]))
            writeFile.write("\n\n")

            # Removes words that have been written to the file
            wordList = wordList[nextLineValue:]

            print("After header delete:", wordList)
            print(bulletTracker(wordList))

            if (bulletTracker(wordList) != len(wordList)):  # If true --> make bullet points
                bulletMaker(wordList, writeFile)

            # Wordlist is not empty --> write remaining words to file        
            if wordList:
                writeFile.write(" ".join(wordList))
                writeFile.write("\n\n")

                
        # # Continues until all words in the line are processed
        # while (len(wordList) > 0):
        #     nextLineValue = nextNewLineRequired(wordList)
        #     writeFile.write("\n")
        #     del wordList[0:nextLineValue]

                
    readFile.close()
    writeFile.close()


def upperLower(wordList):
    for i in range(len(wordList) - 1):

        # # If first word is upper case & the second is lower --> issue with formating
        if (not wordList[i].islower() and wordList[i + 1].islower()):
            return i
        
    return len(wordList)



# Determines the next index in wordList when a  new line is required
def bulletTracker(wordList):
    for i in range(len(wordList) - 1):

        # If '*' appears --> we have a list under a header list
        if wordList[i].startswith("*"):
            if (i == 0):
                return bulletTracker(wordList[1:]) + 1
            return i
                    
    return len(wordList)



    

def bulletMaker(wordList, writeFile):
    nextBullet = bulletTracker(wordList)
    # if (nextBullet == 0):
    #     nextBullet = 1    
    
    while (nextBullet > 0):

        # Create bullet point
        print(wordList[0:nextBullet])
        writeFile.write(" ".join(wordList[0:nextBullet]))

        writeFile.write("\n")
        print("Before delete:", wordList)
        del wordList[0:nextBullet]
        print("After delete:", wordList)

        nextBullet = bulletTracker(wordList)


    # Remove words that have been written
