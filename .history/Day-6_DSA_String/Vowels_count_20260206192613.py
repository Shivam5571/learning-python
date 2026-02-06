#======================== """ Vowels == "aeiouAEIOU" """ ==============================#

#s = input("Enter a string : ")
s = "Shubhamchutiyahai"

count = 0 

for i in s: 
    if i in "aeiouAEIOU":
        count += 1
print(count)