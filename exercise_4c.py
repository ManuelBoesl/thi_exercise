

def change_order(name):
    """
    This function searches for an occurrence of a space character. If it is found, it slices the string and places
    the last part of the string in the front, separated by a comma and returns it.
    :param name: the given name
    :return: the changed string if space is found, else the original string
    """
    start = name.rfind(" ")
    changed_string = name
    if start != -1:
        first_string = name[start + 1:len(name)]
        second_string = name[:name.find(" ")]
        changed_string = first_string + ", " + second_string

    return changed_string


if __name__ == '__main__':
    name = input("Name: ")
    print(change_order(name))
