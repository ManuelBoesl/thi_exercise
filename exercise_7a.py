def verdichte(liste):
    #iterate over the list and add the numbers to the result list
    result = []
    for i in liste:
        if i != 0:
            result.append(i)
    #add the zeros to the result list
    for i in liste:
        if i == 0:
            result.append(i)
    return result


liste1 = [0, 0, 3, 0, 0, 1, 0, 5, 0, 0]
liste2 = verdichte(liste1)
print(liste1)
print(liste2)