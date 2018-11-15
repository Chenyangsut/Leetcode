#-*-coding:utf-8-*-
# ZigZag Converesion 之字形转换字符串
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string text, int nRows);
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
l = []
n = 3
def convert(string,nRows):
    for i in range(nRows):
        l.append(string[i])
    for i in range(nRows,len(string)):
        m = i/nRows
        n = i%nRows
        l[n] += string[i]
    return nRows
convert("PAYPALISHIRING",n)
for i in range(n):
    if i%2==0:
        print ' '.join(l[i])
    else:
        print l[i]