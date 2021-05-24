'''
Stock Clearance
The shop "Pro Street Biker" offers different quality helmets. There are several helmets present in the shop. The shopkeeper want's to know the number of helmet models has more than 1 quantity. So that he can sell those models which helps him in-stock clearance. All helmet models have an ID. Given a list of helmet models ID, the task is to write a python program to compute total equal digit pairs, i.e extract the number of all IDs which can be dual paired with similar IDs present in the list.
Note: You can use count() and set() to solve this problem

Sample Input:
[2, 4, 5, 2, 5, 4, 2, 4, 5, 7, 7, 8, 3]

Sample Output:
Total Pairs: 4

Explanation:
4, 2, and 5 have 3 occurrences, 7 has 2 occurrences, 1 pair each.

'''
import ast
test = ast.literal_eval(input())#input goes here
#your code here
res=0
all_ele=set(test)
for ele in all_ele:
  res+=test.count(ele)//2
print("Total Pairs: " + str(res))
