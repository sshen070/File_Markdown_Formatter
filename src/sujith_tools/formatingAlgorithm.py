def fileCleaner(fileName):
    # Opens the file with read permission
    readFile = open(fileName, "r")
    writeFile = open("cleanedFile.txt", "w")

    # Iterates through each line in the file
    for line in readFile:
        wordList = line.strip().split()

        if not wordList:
            continue

        # If the line starts with '#' --> must be header
        if wordList[0].startswith("#"):
            # Determines the next index a new line is required
            nextLineValue = newLineTracker(wordList)

            for word in wordList[0:nextLineValue]:
                writeFile.write(word)
                if (word != wordList[nextLineValue - 1]):
                    writeFile.write(" ")

            writeFile.write("\n\n")

            # Removes words that have been written to the file
            wordList = wordList[nextLineValue:]

            while (nextBulletTracker(wordList)):  # If true --> make bullet points
                print("Bullet Point Detected")
                bulletMaker(wordList, writeFile)

        
            # Writes the rest of the words in the line
            # for word in wordList:
            #     writeFile.write(word)
            #     if (word != wordList[-1]):
            #         writeFile.write(" ")

            # writeFile.write("\n\n")
            if wordList:
                writeFile.write(" ".join(wordList) + "\n\n")

                


        # # Continues until all words in the line are processed
        # while (len(wordList) > 0):
        #     nextLineValue = nextNewLineRequired(wordList)
        #     writeFile.write("\n")
        #     del wordList[0:nextLineValue]

                
    readFile.close()
    writeFile.close()


# Determines the next index in wordList when a  new line is required
def newLineTracker(wordList):
    for i in range(len(wordList) - 1):

        # If '*' appears --> we have a list under a header list
        if wordList[i].startswith("*"):
            return i + 1


        # # If first word is upper case & the second is lower --> issue with formating
        if (not wordList[i].islower() and wordList[i + 1].islower()):
            return i
        
    return len(wordList)


def nextBulletTracker(wordList):
    for word in range(len(wordList) - 1):

        # If '*' appears --> we have a list under a header list
        if wordList[word].startswith("*"):
            return True

    return False
    

def bulletMaker(wordList, writeFile):
    nextBullet = newLineTracker(wordList)

    if nextBullet == 0:  # safety check
        del wordList[0]
        return


    # Create bullet point
    for word in wordList[0:nextBullet]:
        writeFile.write(word)
        if (word != wordList[nextBullet - 1]):
            writeFile.write(" ")

    writeFile.write("\n")

    # Remove words that have been written
    del wordList[0:nextBullet]
