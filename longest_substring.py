#-*-coding:utf-8-*-
# Longest Substring Without Repeating Characters 最长无重复字符的子串
# Given a string, find the length of the longest substring without repeating characters.
#
# Examples:
#
# Given "abcabcbb", the answer is "abc", which the length is 3.
#
# Given "bbbbb", the answer is "b", with the length of 1.
#
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequenceand not a substring.
s = 'cpwwkew'
l = []
p = []
d = {}
for i in range(len(s)):
    for j in range(i):
        if sorted(s[j:i])==sorted(set(s[j:i])) and sorted(s[j:i+1])!=sorted(set(s[j:i+1])):
            d[s[j:i]]=len(s[j:i])
        else:
            pass
for i in d.values():
    l.append(i)
l = sorted(l)
a = l[-1]
for m,n in d.items():
    if n==a:
        p.append(m)
for i in range(len(p)):
    print 'the answer is "%s",with the length of %d' % ((p[i]),a)