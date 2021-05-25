'''
Remove the Duplicate
The program takes a lists and removes the duplicate items from the list.

Problem Solution:
Take the number of elements in the list and store it in a variable. Accept the values into the list using a for loop and insert them into the list. Use a for loop to traverse through the elements of the list. Use an if statement to check if the element is already there in the list and if it is not there, append it to another list. Print the non-duplicate items of the list. Exit.

Sample Input:
5
10
10
20
20
20

Sample Output:
Non-duplicate items:
[10, 20]

'''
arr=[]
num=int(input())
for x in range(0,num):
  numbers=int(input())
  arr.append(numbers)
b=[]
unique=[]
for x in arr:
  if x not in b:
    unique.append(x)
    b.append(x)
print("Non-duplicate items:")
print(unique)
