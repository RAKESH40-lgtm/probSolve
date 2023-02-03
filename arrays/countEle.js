/* 
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
*/
let arr=[1,2,3,4,5]
let count=0
for(let i=0;i<arr.length;i++){
    count=count+1
}
console.log(count)
/*
ALgo2:
step:print by .lenght property
*/
console.log(arr.length)
