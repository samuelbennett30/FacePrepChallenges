'''
Remove Tuples of length K
You are given a list of tuples, remove all the tuples with length K and print the list.

Sample Input:
[(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]
2

Sample Output : [(4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]

Explanation :
(4, 5) of length = 2 is removed.

'''

import ast
test=ast.literal_eval(input())
k=int(input())
res=list(filter(lambda x: len(x)!=k,test))
print(str(res))
