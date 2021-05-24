'''
Factorial
Write a program to determine whether 'n' is a factorial number or not. Factorial of a number is the product of all positive numbers from 1 to 'n'.

Input format:
The input containing an integer 'n' which denotes the given number.

Output format:
If the given number is factorial, print "Yes". Otherwise, print "No". Refer the sample output for formatting.

Sample Input:
6

Sample Output:
Yes
'''
n=int(input())
i=1
fact=1
while(i!=0):
  fact=fact*i
  if(n==fact):
    flag=1
    break
  if(n<fact):
    flag=0
    break
  i=i+1
if(flag==1):
  print("Yes")
else:
  print("No")
