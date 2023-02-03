"""
Program to copy all the elements of one array into another array
Input:
arr1 = [1, 2, 3, 4, 5];  
arr2 = [None] * len(arr1);  
Output:
Elements of original array: 1 2 3 4 5
Elements of new array: 1 2 3 4 5
step1:define and initialize the arr1
step2:define arr2
step3:iterate over arr1 and append those values to arr2
step4:print arr2
"""
my_arr=[1,2,3,4,5]
my_arr2=[]
for item in my_arr:
    # my_arr2=item #it will assign but not update its main length
    my_arr2.append(item)

# print(len(my_arr2))
print(f'through iteration: {my_arr2}')
"""
Algorithm2:
step1:define and initialize the arr1
step2:define arr2 and copy the arr1
step3:print arr2
"""
arr1=[1,2,3,4,5]
arr2=arr1.copy()
print(f'through array method : {arr2}')
# arr2=arr1#it affects the data in both arr
# arr2[2]=8
# print(arr1)
