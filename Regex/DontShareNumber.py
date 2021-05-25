'''
Don't share Mobile number
In a college mobile phones are restricted. No one should share their mobile number with anyone. But still, several students are sharing their mobile numbers through college chat messenger not directly but in a tricky way. Information from intelligence says that students are sharing their number in between a huge sentence by two 3 digit numbers followed by two 2 digit numbers separated by any single character. The college want's to find the culprits. Write a program to extract mobile numbers in the mentioned format. See the sample input for a better understanding.

Sample Input:
Hi I am Vishwa and I can not 979s876m99m00 number

Sample Output:
Nummber Shared

'''
import re
string = input()
string +=' '
pattern = '(\d{3}).(\d{3}).(\d{2}).(\d{2})'
match = re.search(pattern, string) 
if match:
  print("Number Shared")
else:
  print("Number Not Shared")

