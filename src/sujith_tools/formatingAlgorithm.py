def file_cleaner(read_file: str, write_file: str) -> None:
    # Opens the file with read permission
    with open(read_file, "r") as read_file, open(write_file, "w") as write_file:

        # Iterates through each line in the file
        for line in read_file:
            word_list = line.strip().split()
            print(word_list)
            if not word_list:
                continue

            # If the line starts with '#' --> must be header
            if word_list[0].startswith("#"):
                
                if (header_end_tracker(word_list)):
                    header_maker(word_list, write_file)
                else:
                    bullet_maker(word_list, write_file)

                write_file.write("\n")

                # If bullets exist --> create bullet points
                while (bullet_tracker(word_list) != len(word_list)):
                    bullet_maker(word_list, write_file)            
                

            # word_list is not empty --> write remaining words to file        
            if word_list:
                write_file.write(" ".join(word_list))
                write_file.write("\n\n")



                    
            # # Continues until all words in the line are processed
            # while (len(word_list) > 0):
            #     nextLineValue = nextNewLineRequired(word_list)
            #     write_file.write("\n")
            #     del word_list[0:nextLineValue]


# Determines when a new Line is required (Headers)
# Upper | Upper lower --> End of header | Body text (First word capitalized --> rest lower case)  
def header_end_tracker(word_list: list[str]) -> int:
    # If there are bullet points in the word_list --> do not make a header
    if (bullet_tracker(word_list) != len(word_list)):
        return 0
    
    for i in range(len(word_list) - 2):
            # If first word is upper case & the second is lower --> issue with formating
            if (not word_list[i].islower() and not word_list[i + 1].islower() and word_list[i + 2].islower()):
                return i + 1
            
            
    return len(word_list)


def header_maker(word_list: list[str], write_file: str) -> None:
    next_header = header_end_tracker(word_list)
    
    # Create header
    write_file.write(" ".join(word_list[0:next_header]))

    write_file.write("\n")
    del word_list[0:next_header]
    next_header = header_end_tracker(word_list)




# Determines the next index in word_list when a  new line is required
def bullet_tracker(word_list: list[str]) -> int:
    for i in range(len(word_list) - 1):

        # If '*' appears --> we have a list under a header list
        if word_list[i].startswith("*"):
            if (i == 0):
                return bullet_tracker(word_list[1:]) + 1
            return i
                    
    return len(word_list)



def bullet_maker(word_list: list[str], write_file: str) -> None:
    nextBullet = bullet_tracker(word_list)
    
    # Create bullet point
    write_file.write(" ".join(word_list[0:nextBullet]))

    write_file.write("\n")
    del word_list[0:nextBullet]
