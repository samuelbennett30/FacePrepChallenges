'''
Replace Elements with in range
3M car service always allows their customers to service their cars slot wise. Each index of the list represents the slot and the value at each index represents the car number. Based on the number of cars arriving for service they will block certain slots for their privileged customers. Your task is to change the existing ID to the given ID in the list for the given range.

Sample Input:

9 5 4 3 2 1 8 7

1 5

1

Sample Output:

[9, 1, 1, 1, 1, 1, 8, 7]

Explanation:
The list is updated with 1 from the 1st to 4th index.

'''

from itertools import repeat
n=list(map(int,input().split(" ")))
i,j=map(int,input().split(" "))
k=int(input())
n[i:j]=repeat(k,(j-i))
print(str(n))
