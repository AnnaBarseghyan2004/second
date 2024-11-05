n = int(input())

def dictionary (n) :
    return {f'{i}': f'{len(str(i))}' for i in range(n+1)}

result = dictionary(n)
print(result)