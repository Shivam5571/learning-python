#-----------------------------------Reverse an array--------------------------------#
#Reverse list ka matlab hota hai:
#List ke elements ka order ulta kar dena (last → first, first → last).
#[1, 2, 3, 4] → [4, 3, 2, 1]
arr = [1,2,3,4,5]
#Approach 1: Using built-in reverse() method
print("Original array:",arr)
arr.reverse()
print("Reverse:",arr)