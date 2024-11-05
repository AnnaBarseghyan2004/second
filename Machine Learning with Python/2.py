a = str(input())

for char in a:
    if char == "{" or char == "}" or char == "(" or char ==")" or char == "[" or char == "]":
        a = a.replace(char, "")
print(a)