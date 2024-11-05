word = str(input())

dictionary = {}

for element in word:
    if element in dictionary :
        dictionary[element] += 1
    else:
        dictionary[element] = 1

print(dictionary)