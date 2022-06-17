""" Create a program that takes a string and replaces all occurrences of repeated letters (consecutively) with a single occurrence of the same uppercase. """

def replace_repeated_letters(string):
    """ Replace all occurrences of repeated letters (consecutively) with a single occurrence of the same uppercase. """
    string = list(string)
    for i in range(len(string)):
        if i == 0:
            continue
        elif string[i] == string[i-1]:
            string[i] = string[i].upper()
        else:
            continue
    return ''.join(string)

test = replace_repeated_letters('Arranhão')

print(test)