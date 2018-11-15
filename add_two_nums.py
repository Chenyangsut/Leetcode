#-*-coding:utf-8-*-
# add two numbers 两个数字相加
# You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
import re
m = raw_input('Input:')
l = m.split('+')
the1 = re.sub(r'\D','',l[0])
the2 = re.sub(r'\D','',l[1])
the1 = map(int,the1)
the2 = map(int,the2)
su = []
o = 0
for a in range(0,len(the1)):
    summer = the1[a]+the2[a] + o
    if summer<10:
        o = 0
    else:
        o = 1
        summer = summer - 10
    su.append(summer)
su = map(str,su)
st = '->'.join(su)
print 'Output:',st