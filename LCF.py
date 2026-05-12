# Longest Common Prefix
# Question: Given a list of strings, find the longest prefix shared by all strings. If no common prefix exists, return an empty string.
# Example 1: Input: ["flower","flow","flight"] Output: "fl"
# Example 2: Input: ["dog","racecar","car"] Output: ""

str = list(input("Enter list of strings").split())
print(str)
pre = str[0]

if not str:
    pre=""

for i in range(1, len(str)):
    while not str[i].startswith(pre):
        pre = pre[:-1]
        if not pre:
            pre=""
            

if pre == "":
    print("No Common prefix")
else:
    print("Longest Common Prefix is : ", pre)