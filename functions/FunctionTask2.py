# create function which will take 1 sinle argument username
# check userName is palindrome or not
# # use string slicing...


def isPalindrome(name):
    if(name == name[::-1]):
        print("palindrome...")
    else:
        print("not palindrome..")    

isPalindrome("raj")        