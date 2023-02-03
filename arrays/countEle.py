"""
Program to print the number of elements present in an array
Input:
arr = [1, 2, 3, 4, 5]  
Output:
Number of elements present in given array: 5
Algorithm:
step1:define arr
step2:define count=0
step3:iterate over arr
step4:increase count by 1
"""
arr=[1,2,3,4,5]
count=0
for _ in arr:
    count+=1
print(count)
print(len(arr))#print no of element present in an array