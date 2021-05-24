'''
Covert the Number
You are provided with a 10 digit phone number. You are requested to convert this 10 digit number to US format using RegEx in python.
Sample Input:
321-963-0612
Sample Output:
(321) 963-0612
'''
import re  
def convert_phone_number(phone): 
  num = re.sub(r'(?<!\S)(\d{3})-', r'(\1) ', phone)  
  return num 
num = input()
print(convert_phone_number(num))
