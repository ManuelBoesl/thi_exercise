import re


def version_regex(original_string, search_string):

    regex = search_string

    original = original_string

    matches = re.finditer(regex, original, re.MULTILINE)

    length = 0

    for matchNum, match in enumerate(matches, start=1):
        
        print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
        length = matchNum

    print(f"Found {length} matches")


def version_slice(original_string, search_string):
    pass
    

if __name__ == '__main__':
    original_string = input("Original: ")
    search_string = input("Search: ")

    version_regex(original_string, search_string)
    version_slice(original_string, search_string)
