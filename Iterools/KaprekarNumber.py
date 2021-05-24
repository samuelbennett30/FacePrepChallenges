'''
Kaprekar Number
Consider an n-digit number k. Square it and add the right n digits to the left n or n-1 digits. If the resultant sum is k, then k is called a Kaprekar number. For example, 9 is a Kaprekar number since 92 = 81 & 8+1=9. and 297 is a Kaprekar number since 297^2 = 88209 & 88+209 = 297

Input Format:
Input consists of a single integer.

Output Format:
Refer sample output for details.

Sample Input :
9

Sample Output :
Kaprekar Number
'''
#python
a=int(input())
n=a
c=0
while(n!=0):
  c=c+1
  sq=a*a
  po=pow(10,c)
  f=sq%po
  s=sq//po
  n=n//10
if(f+s==a):
  print("Kaprekar Number")
else:
  print("Not a Kaprekar Number")
