/* 
Program to print the elements of an array in reverse order
Input:
arr = [1, 2, 3, 4, 5]  
Output:
Original array: 1 2 3 4 5
Array in reverse order: 5 4 3 2 1
Algorithm:
step1:create and define array.
step2:create a newStr
step3:iterate over array from length-1
step4:assign that element to newStr
step5:print the newStr
*/
let arr=[1,2,3,4,5]
let newStr=''
for(let i=arr.length-1;i>=0;i--){
    newStr=newStr+' '+arr[i]
}
console.log(newStr)
/* 
Algorithm2:
step1: print it by reverse it by reverse()

*/
console.log(arr.reverse().join(' '))