def string_markdown_cleaner(unformatted_line: str) -> str:
    word_list: list[str] = unformatted_line.strip().split()
    formatted_line: str = ""

    period_splicer(word_list)

    while word_list:
        # If the line starts with '#' --> must be header
        if word_list[0].startswith("#"):

            if header_end_tracker(word_list):
                formatted_line += header_maker(word_list)
            else:
                formatted_line += bullet_maker(word_list)

            formatted_line += "\n"

            while bullet_tracker(word_list) != len(word_list):
                formatted_line += bullet_maker(word_list)

        # Line begins with body text
        elif not word_list[0].startswith("#"):

            if colon_tracer(word_list) != len(
                    word_list) or word_list[-1].endswith(":"):
                formatted_line += colon_spacer(word_list)

            while bullet_tracker(word_list) != len(word_list):
                formatted_line += bullet_maker(word_list)

            if word_list:
                if header_exists(word_list) != len(word_list):
                    idx = header_exists(word_list)
                    formatted_line += " ".join(word_list[:idx]) + "\n\n"
                    del word_list[:idx]
                else:
                    formatted_line += " ".join(word_list) + "\n\n"
                    word_list.clear()

    return formatted_line


def header_exists(word_list: list[str]) -> int:
    for i, word in enumerate(word_list):
        if word.startswith("#"):
            return i
    return len(word_list)


def header_end_tracker(word_list: list[str]) -> int:
    if bullet_tracker(word_list) != len(word_list):
        return 0

    for i in range(len(word_list) - 2):
        if (not word_list[i].islower() and not word_list[i + 1].islower()
                and word_list[i + 2].islower()):
            if word_comparator(word_list[i + 2]):
                continue
            return i + 1
    return len(word_list)


def word_comparator(lower_case_word: str) -> bool:
    valid_in_header = [
        "a", "an", "and", "as", "at", "but", "by", "en", "for", "if", "in",
        "of", "on", "or", "the", "to", "v", "v.", "vs", "vs."
    ]
    return lower_case_word in valid_in_header


def header_maker(word_list: list[str]) -> str:
    next_header = header_end_tracker(word_list)
    header = " ".join(word_list[0:next_header]) + "\n"
    del word_list[0:next_header]
    return header


def bullet_tracker(word_list: list[str]) -> int:
    for i in range(len(word_list) - 1):
        if word_list[i].startswith("*"):
            if i == 0:
                return bullet_tracker(word_list[1:]) + 1
            return i
    return len(word_list)


def bullet_maker(word_list: list[str]) -> str:
    next_bullet = bullet_tracker(word_list)
    bullet = " ".join(word_list[0:next_bullet]) + "\n"
    del word_list[0:next_bullet]
    return bullet


def colon_tracer(word_list: list[str]) -> int:
    if word_list[-1].endswith(":"):
        return len(word_list)
    for i in range(len(word_list) - 1):
        if word_list[i].endswith(":"):
            if word_list[i + 1].islower():
                return len(word_list)
            return i + 1
    return len(word_list)


def colon_spacer(word_list: list[str]) -> str:
    colon_index = colon_tracer(word_list)

    if word_list[0].startswith("*"):
        return ""

    line = " ".join(word_list[0:colon_index])
    if colon_index != len(word_list) - 1:
        line += "\n"
    del word_list[0:colon_index]
    return line


def period_splicer(word_list: list[str]) -> None:
    for i in range(len(word_list) - 1):
        period_index = word_list[i].find(".")
        if period_index != -1 and not word_list[i].endswith("."):
            word_list.insert(i + 1, word_list[i][period_index + 1:])
            word_list[i] = word_list[i][:period_index + 1]
            return
