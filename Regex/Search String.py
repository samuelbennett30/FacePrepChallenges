'''
Search a String
Asgard is in danger. Thor and Loki are looking for clues to save their world. Luckily they got a part of the clue. You are provided with 2 strings. The first string is the actual clue and the second string is the part of a clue that they have. Help Thor and Loki by searching the second string occurrence in the first string irrespective of cases using Regex in Python.

Sample Input:
I love Asgard
asgard

Sample Output:
String Found

'''

import re
string=input()
pattern= re.compile(input(),re.IGNORECASE)
match=re.search(pattern,string)
if match:
  print("String Found")
else:
  print("String Not Found")
