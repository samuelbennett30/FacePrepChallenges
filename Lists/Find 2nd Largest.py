'''
Find the second largest number in a list
Python Program to Find the Second Largest Number in a List

Problem Description:
The program takes a list and prints the second largest number in the list.

Input Format:
Input consists of n + 1 integers. First integer corresponds to the size , The next n inputs corresponds to the elements in the list.

Sample Input:
4
23
56
39
11

Sample Output:
39
'''
rr=[]
num=int(input())
for n in range(num):
  numbers=int(input())
  arr.append(numbers)
arr.sort()
print(arr[-2])

