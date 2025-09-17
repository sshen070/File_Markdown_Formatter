# Functionality: Cleans poorly formatted markdown files
def file_markdown_cleaner(read_file: str, write_file: str) -> None:

    # Opens the file with read permission & write permission for appropriate files
    with open(read_file, "r") as read_file, open(write_file,
                                                 "w") as write_file:

        # Iterates through each line in the file
        for line in read_file:
            word_list: list[str] = line.strip().split()

            # If the line is empty --> skip to next line
            if not word_list:
                continue

            # Continues until the word_list is empty
            while (word_list):

                # Deals period mislocation issues (edge case)
                period_splicer(word_list)

                # If the line starts with '#' --> must be header
                if (word_list[0].startswith("#")):

                    # If the header is valid --> create header
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
                    if (colon_tracer(word_list) != len(word_list)
                            or word_list[-1].endswith(":")):
                        colon_spacer(word_list, write_file)

                    # If bullets exist --> create bullet points
                    while (bullet_tracker(word_list) != len(word_list)):
                        bullet_maker(word_list, write_file)

                    # If the word_list is still not empty
                    if (word_list):

                        # If a word is a header --> write text until header & loop again
                        if (header_exists(word_list)):

                            write_file.write(" ".join(
                                word_list[0:header_exists(word_list)]))
                            write_file.write("\n\n")
                            del word_list[0:header_exists(word_list)]
                            continue

                        # If no headers/special cases --> write the rest of the line
                        else:
                            write_file.write(" ".join(word_list))
                            write_file.write("\n\n")
                            word_list.clear()


# Determines if a header exists in the word_list --> returns index of word containing header
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
        if (not word_list[i].islower() and not word_list[i + 1].islower()
                and word_list[i + 2].islower()):

            # If the third word is a valid header word (ex. "to") --> continue
            if (word_comparator(word_list[i + 2])):
                continue
            return i + 1

    return len(word_list)


# Checks if a word is a valid header word (ex. "to", "and", "the")
def word_comparator(lower_case_word: str) -> bool:
    valid_in_header: list[str] = [
        "a", "an", "and", "as", "at", "but", "by", "en", "for", "if", "in",
        "of", "on", "or", "the", "to", "v", "v.", "vs", "vs."
    ]

    for word in valid_in_header:
        if (lower_case_word == word):
            return True
    return False


# Creates the header in the write_file
def header_maker(word_list: list[str], write_file: str) -> None:
    next_header: int = header_end_tracker(word_list)

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


# Creates the bullet point in the write_file
def bullet_maker(word_list: list[str], write_file: str) -> None:
    nextBullet: int = bullet_tracker(word_list)

    # Create bullet point
    write_file.write(" ".join(word_list[0:nextBullet]))

    write_file.write("\n")
    del word_list[0:nextBullet]


# Determines if a colon exists in the word_list --> returns index of word after colon
def colon_tracer(word_list: list[str]) -> int:

    # If the colon is at the end of the line (edge case)
    if (word_list[-1].endswith(":")):
        return len(word_list)

    for i in range(len(word_list) - 1):

        # If ':' appears --> we have a list under a header list
        if word_list[i].endswith(":"):

            # If the next word is lower case --> new line not required
            if word_list[i + 1].islower():
                return len(word_list)
            return i + 1

    return len(word_list)


# Creates a new line at the colon in the write_file
def colon_spacer(word_list: list[str], write_file: str) -> None:
    colon_index: int = colon_tracer(word_list)

    # If the line is a bullet point --> do not create new line
    if (word_list[0].startswith("*")):
        return

    # Create new line at colon
    write_file.write(" ".join(word_list[0:colon_index]))

    if (colon_index != len(word_list) - 1):
        write_file.write("\n")

    del word_list[0:colon_index]


def period_splicer(word_list: list[str]) -> None:
    for i in range(len(word_list) - 1):

        # period_index = -1 if no period found / else index of period in word
        period_index: int = word_list[i].find(".")

        # Period exists in word
        if (period_index != -1):

            # Period is not at the end of the word
            if (not word_list[i].endswith(".")):

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
