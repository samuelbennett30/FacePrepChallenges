'''
Mark Duplicate Element in a string
Robert is working with strings. He was stuck in implementing a particular part. He wants to mark the duplicate occurrence of elements with a progressive occurrence number. Help him to implement the functionality by writing a python program.

Input Format:
Input is a string

Output Format:
The output consists of a list of words and their progressive occurrence.

Sample Input:
the program outcome is great everyone likes our program the program outcome is great everyone likes our program.

Sample Output:
['the1', 'program1', 'outcome1', 'is1', 'great1', 'everyone1', 'likes1', 'our1', 'program2', 'the2', 'program3', 'outcome2', 'is2', 'great2', 'everyone2', 'likes2', 'our2', 'program4']

'''
import ast
test=list(input().split(" "))
res=[val+str(test[:idx].count(val)+1) if test.count(val)>1 else val for idx,val in enumerate(test)]
print(str(res))
