'''Write a program that reads two strings and prints the combined strings to the screen'''

def combine_letters():
    string1 = input('Digite a primeira string: ')
    string2 = input('Digite a segunda string: ')
    new = ''
    
    if string1 == string2:
        for i in range(len(string1)):
            new = new + string1[i] + string2[i]
    elif string1 < string2:
        for i in range(len(string2)):
            new = new + string1[i] + string2[i]
    else:
        print ('erro')
        
    print (f'Combinação:{new}')
    
combine_letters()