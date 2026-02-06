""" 👉 Palindrome Check = reverse same ho """
"""Example :  madam = madma / pop = pop """


s = input("Enter a string : ")

if s == s[::-1]:
    print("Palindrome String")
else:
    print("Not a Palindrome String")

