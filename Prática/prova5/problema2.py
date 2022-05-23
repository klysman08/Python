'''Write a program that reads two strings and prints the combined strings to the screen'''

def combine_letters():
    string1 = input('Digite a primeira string: ')
    string2 = input('Digite a segunda string: ')
    
    if string1 > string2:
        for i in range(len(string1)):
            print(string1[i] + string2[i])
    else:
        for i in range(len(string2)):
            print(string1[i] + string2[i])

combine_letters()