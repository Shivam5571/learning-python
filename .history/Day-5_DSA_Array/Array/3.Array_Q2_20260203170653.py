# -------------------------------------Find max element
arr = [10,0,5,46,50]

a = arr[0]
for i in arr:
    if i > a:
        max = i 
print("Max element is:",max)


#------------------------------------- Find min element
arr = [1,2,3,4,5]

min = arr[0]
for i in arr:
    if i < min:
        min = i 
print("Min element is:",min)