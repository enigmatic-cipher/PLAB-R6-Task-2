"""
Given n as input. Print following pattern using For loop.
Input-> n = 5
Output-> #10#8#6#4#2
"""

n = 5
num = n
st = ""
pt = "#"
for i in range(0,num):
  st = pt + str(num*2)
  num = num-1
  print(st, end = "")