/*
Program to copy all the elements of one array into another array
Input:
arr1 = [1, 2, 3, 4, 5];  
arr2 = [None] * len(arr1);  
Output:
Elements of original array: 1 2 3 4 5
Elements of new array: 1 2 3 4 5
Algorithm:
step1:define and initialize the arr1
step2:define arr2
step3:iterate over arr1 and assign those values to arr2
step4:print arr2
*/
let arr1=[1,2,3,4,5]
let arr2=[]
for(let i=0;i<arr1.length;i++){
    arr2[i]=arr1[i]
    // arr2.length++ don;t need as we're assigning arr1 to arr2
}
console.log(`Through iterating:  ${arr2}`)
/* 
Algorithm2:
step1:define and initialize the arr1
step2:define arr2
step3:destructure that arr1 in arr2
step4:print it
*/
let arr3=[1,2,3,4,5]
let arr4=[...arr3]
console.log(`Through destructuring:  ${arr4}`)