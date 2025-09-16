# Functionality: Cleans poorly formatted markdown files
def file_cleaner(read_file: str, write_file: str) -> None:
    # Opens the file with read permission
    with open(read_file, "r") as read_file, open(write_file, "w") as write_file:

        # Iterates through each line in the file
        for line in read_file:
            word_list = line.strip().split()

            if not word_list:
                continue

            while (word_list):

                print(word_list)
                period_splicer(line, word_list)

                # If the line starts with '#' --> must be header
                if (word_list[0].startswith("#")):

                    if (header_end_tracker(word_list)):
                        header_maker(word_list, write_file)
                    else:
                        bullet_maker(word_list, write_file)

                    write_file.write("\n")

                    # If bullets exist --> create bullet points
                    while (bullet_tracker(word_list) != len(word_list)):
                        bullet_maker(word_list, write_file)
                
                # Line begins with body text
                elif (not word_list[0].startswith("#")):
                    
                    # If a colon exists --> create new line
                    if (colon_tracer(word_list) != len(word_list) or word_list[-1].endswith(":")):
                        colon_spacer(word_list, write_file)
                    
                    # If bullets exist --> create bullet points
                    while (bullet_tracker(word_list) != len(word_list)):
                        bullet_maker(word_list, write_file)

                    # If the word_list is still not empty
                    if (word_list):

                        # If a word is a header --> track location & loop again
                        if (header_exists(word_list)):
                            
                            write_file.write(" ".join(word_list[0:header_exists(word_list)]))
                            write_file.write("\n\n")
                            del word_list[0:header_exists(word_list)]
                            continue
                    
                elif (word_list):
                    write_file.write(" ".join(word_list))
                    write_file.write("\n\n")
                    del word_list[:]
                    # write_file.clear()



def header_exists(word_list: list[str]) -> int:
    for i, word in enumerate(word_list):
        if (word.startswith("#")):
            return i
    return len(word_list)



# Determines when a new Line is required (Headers)
# Upper | Upper lower --> End of header | Body text (First word capitalized --> rest lower case)  
def header_end_tracker(word_list: list[str]) -> int:
    # If there are bullet points in the word_list --> do not make a header
    if (bullet_tracker(word_list) != len(word_list)):
        return 0
    

    for i in range(len(word_list) - 2):
            # If first word is upper case & the second is lower --> issue with formating
            if (not word_list[i].islower() and not word_list[i + 1].islower() and word_list[i + 2].islower()):
                if (word_comparator(word_list, word_list[i + 2])):
                    continue
                return i + 1
            
    return len(word_list)



def word_comparator(word_list: list[str], lower_case_word: str) -> bool:
    valid_in_header = [ "a", "an", "and", "as", "at", "but", "by", "en", "for", "if", "in", "of", "on", "or", "the", "to", "v", "v.", "vs", "vs."]

    for word in valid_in_header:
        if (lower_case_word == word):
            return True
    return False



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
    line_info(word_list)



def colon_tracer(word_list: list[str]) -> int:

    if (word_list[-1].endswith(":")):
        return len(word_list)
    
    for i in range(len(word_list) - 1):
        # If ':' appears --> we have a list under a header list
        if word_list[i].endswith(":"):
            if word_list[i + 1].islower():
                return len(word_list)
            return i + 1
        
    return len(word_list)



def colon_spacer(word_list: list[str], write_file: str) -> None:
    colon_index = colon_tracer(word_list)
    line_info(word_list)
    # If the line is a bullet point --> do not create new line
    if (word_list[0].startswith("*")):
        return
    
    # Create new line at colon
    write_file.write(" ".join(word_list[0:colon_index]))

    if (colon_index != len(word_list) - 1):
        write_file.write("\n")
    
    del word_list[0:colon_index]

    

def period_splicer(line: str, word_list: list[str]) -> None:

    for i in range(len(word_list) - 1):

        # period_index = -1 if no period found / else index of period in word
        period_index = word_list[i].find(".")

        # Period exists in word
        if period_index != -1:
            
            # Period is not at the end of the word
            if  (not word_list[i].endswith(".")):

                # Split the word at the period --> word before period stays at index i / word after period goes to index i + 1
                word_list.insert(i + 1, word_list[i][period_index + 1:])
                word_list[i] = word_list[i][:period_index + 1]
                return



def line_info(word_list: list[str]) -> None:
    print("\n\n")
    print("Line Info: \n")
    print("Word List: ", word_list)

    for i in range(len(word_list)):
        print(i, word_list[i])

    print("\n")