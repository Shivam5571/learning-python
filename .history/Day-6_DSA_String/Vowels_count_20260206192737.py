#======================== """ Vowels == "aeiouAEIOU" """ ==============================#

#s = input("Enter a string : ")
s = "0098765432123456789876543`"

count = 0 

for i in s: 
    if i in "aeiouAEIOU":
        count += 1
print(count)