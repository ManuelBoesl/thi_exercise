import re


def version_regex(original_string, search_string):
    """
    This function searches for a substring in a given string with a regex pattern and prints the location of the match
    to the console. It is also possible to enter a regex pattern.
    :param original_string: The string which will be searched for occurrences of a substring or regex pattern
    :param search_string: The substring or the regex pattern
    """
    regex = search_string
    original = original_string
    matches = re.finditer(regex, original, re.MULTILINE)

    length = 0

    for match_num, match in enumerate(matches, start=1):
        print_match(match_num, match.start(), match.end())
        length = match_num

    print(f"{search_string} kommt in {original_string} {length} Mal vor\n")


def version_slice(original_string, search_string):
    """
    This function searches for a substring in a given string by using the "slice" operator. It is not possible to enter
    a regex pattern
    :param original_string: The string which will be searched for occurrences of a substring or regex pattern
    :param search_string: The substring or the regex pattern
    """
    changed_string = original_string

    counter = 0
    number_sliced = 0

    while (start_index := changed_string.find(search_string)) != -1:
        counter += 1

        end_index = start_index + len(search_string)
        changed_string = changed_string[end_index:len(changed_string)]

        print_match(counter, start_index + number_sliced, end_index + number_sliced)
        # Add the end index of the last match to the amount of characters sliced away, so that the
        # index will be displayed correctly
        number_sliced += end_index

    print(f"{search_string} kommt in {original_string} {counter} Mal vor\n")


def print_match(match_num, start, end):
    """
    This function prints where the found match is located in the given string
    :param match_num: The number of the match
    :param start: The start index of the match
    :param end: The end index of the match
    """
    print(f"Match {match_num} was found at {start}-{end}.")


if __name__ == '__main__':
    original_string = input("String: ")
    search_string = input("Teilstring: ")
    print("Running version regex")
    version_regex(original_string, search_string)
    print("running version slice")
    version_slice(original_string, search_string)
