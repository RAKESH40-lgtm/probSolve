"""
Program to print the elements of an array
Input:
arr = [1, 2, 3, 4, 5]  
Output:
Elements of given array: 1 2 3 4 5
Algorithm:
step1:define and initialize the arr
step2:create an empty string
step3:iterate over an arr
step4:assign each element to the string
step5:print that new string.
"""
arr=[1,2,3,4,5]
newStr=""
for item in arr:
    newStr=newStr+' '+str(item)
print(newStr)