'''
Extract numbers
You are provided with an URL. You are required to extract the digits present in the URL. Use Python - RegEx to solve this problem.

Sample Input:
https://www.google.com/search?q=google&oq=google&aqs=chrome..69i57j69i60l4j69i65l2j69i60.4365j0j4&sourceid=chrome&ie=UTF-8

Sample Output:
['69', '57', '69', '60', '4', '69', '65', '2', '69', '60', '4365', '0', '4', '8']﻿

'''

import re
string=input()
result=re.findall('\d+',string)
print(result)

