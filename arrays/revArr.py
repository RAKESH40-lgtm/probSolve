"""
Program to print the elements of an array in reverse order
Input:
arr = [1, 2, 3, 4, 5]  
Output:
Original array: 1 2 3 4 5
Array in reverse order: 5 4 3 2 1
Algorithm:
step1:create and define array.
step2:create a newStr
step3:iterate over array from length and steps by -1
step4:assign that element to newStr
step5:print the newStr
"""
arr=[1,2,3,4,5]
newStr=''
for item in range(len(arr),0,-1):
    newStr=newStr+' '+str(item)
print(newStr)