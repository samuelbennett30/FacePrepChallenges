'''
Array Mean
Write a program to find the mean of the elements in the array.

Input Format:
Input consists of n+1 integers where n corresponds to the number of elements in the array. The first integer corresponds to n and the next n integers correspond to the elements in the array. Assume that the maximum number of elements in the array is 20.

Output Format:
Output consists of a double value which corresponds to the mean of the array. It is printed upto 2 digits of precision. Refer sample input and output for formatting specifications. [All text in bold corresponds to input and the rest corresponds to output.]

Sample Input:
5
2
4
1
3
1

Sample Output:
2.20

'''

arr=[]
num=int(input())
for n in range(num):
  numbers= int(input())
  arr.append(numbers)
print(sum(arr)/len(arr))
