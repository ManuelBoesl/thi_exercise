import re


def version_regex(original_string, search_string):

    regex = search_string

    original = original_string

    matches = re.finditer(regex, original, re.MULTILINE)

    length = 0

    for match_num, match in enumerate(matches, start=1):
        print_match(match_num, match.start(), match.end())
        length = match_num

    print(f"{search_string} kommt in {original_string} {length} Mal vor\n")


def version_slice(original_string, search_string):
    changed_string = original_string
   
    counter = 0
    number_sliced = 0

    while (start_index := changed_string.find(search_string)) != -1:
        counter += 1
        end_index = start_index + len(search_string)
        changed_string = changed_string[end_index:len(changed_string)]
        print_match(counter, start_index + number_sliced, end_index + number_sliced)
        number_sliced += len(search_string)

    print(f"{search_string} kommt in {original_string} {counter} Mal vor\n")    


def print_match(match_num, start, end):
    print (f"Match {match_num} was found at {start}-{end}.")


    

if __name__ == '__main__':
    original_string = input("String: ")
    search_string = input("Teilstring: ")
    print("Running version regex")
    version_regex(original_string, search_string)
    print("running version slice")
    version_slice(original_string, search_string)
