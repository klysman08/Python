'''Write a program that reads a string and prints to the screen whether it is a palindrome or not'''
def is_palindrome(string):
    string = list(string)
    return all(string[i] == string[len(string)-i-1] for i in range(len(string)))

print(is_palindrome("ovo"))