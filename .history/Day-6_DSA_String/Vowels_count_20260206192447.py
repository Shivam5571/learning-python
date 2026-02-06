#======================== """ Vowels == "aeiouAEIOU" """ ==============================#

#s = input("Enter a string : ")
s = "Shubhamchutiyahai"

count = 0 

for  ch in s: 
    if ch in "aeiouAEIOU":
        count += 1
print(count)