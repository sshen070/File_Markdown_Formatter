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
            
            if (headerEndTracker(wordList)):
                headerMaker(wordList, writeFile)
            else:
                bulletMaker(wordList, writeFile)

            writeFile.write("\n")

            # If bullets exist --> create bullet points
            while (bulletTracker(wordList) != len(wordList)):
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


# Determines when a new Line is required (Headers)
# Upper | Upper lower --> End of header | Body text (First word capitalized --> rest lower case)  
def headerEndTracker(wordList):
    # If there are bullet points in the wordList --> do not make a header
    if (bulletTracker(wordList) != len(wordList)):
        return 0
    
    for i in range(len(wordList) - 2):
            # If first word is upper case & the second is lower --> issue with formating
            if (not wordList[i].islower() and not wordList[i + 1].islower() and wordList[i + 2].islower()):
                return i + 1
            
            
    return len(wordList)


def headerMaker(wordList, writeFile):
    nextHeader = headerEndTracker(wordList)
    
    # Create header
    writeFile.write(" ".join(wordList[0:nextHeader]))

    writeFile.write("\n")
    del wordList[0:nextHeader]
    nextHeader = headerEndTracker(wordList)




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
    
    # Create bullet point
    writeFile.write(" ".join(wordList[0:nextBullet]))

    writeFile.write("\n")
    del wordList[0:nextBullet]
