'''
Supersequence Strings
Karthik is a developer who does wonders with C and C++. He was developing a feature of searching. He wants to display all the words present in the main string that has all the characters of the given substring. But the number of lines of code and the complexity increases in his native language. He came to know about the Built-in functions available in Python which provides solutions in a single line. Unfortunately, he doesn't know Python. Help him by writing a Python program to implement this functionality.

Sample Input:
The world is running behind money
in

Sample Output:
['running', 'behind']

'''

n=list(input().split(" "))
sub=input()
res=list(filter(lambda s:all(ele in s for ele in sub),n))
print(str(res))
