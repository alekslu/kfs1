# leetcode ylesanne https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
# 1614. Maximum Nesting Depth of the Parentheses

# s = "(1)+((2))+(((3)))"
s = "(1+(2*3)+((8)/4))+1"
def maxDepth(s):
    current_depth = 0
    very_deep = 0

    for char in s:
        if char == "(":
            current_depth += 1
            very_deep = max(very_deep, current_depth)
        elif char == ")":
            current_depth -= 1

    return very_deep

sugavus = maxDepth(s)
print("Koige sugavam arv on: " + str(sugavus))