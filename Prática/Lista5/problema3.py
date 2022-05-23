'''Write a program that reads a string and prints to the screen whether it is a palindrome or not'''
def is_palindrome(string):
    string = list(string)
    for i in range(len(string)):
        if string[i] == string[len(string)-i-1]:
            continue
        else:
            return False
    return True

print(is_palindrome("ovo"))