print ("Enter a word")

word = str(input())

if int(len(word)) <= 7 :
   new_letter = 'z'
   new_word = new_letter + word[1 :]
   print(new_word)
else :
   first_letter = word[0]
   count = 0
   for i in range(len(word)):
      if word[i] == first_letter :
        count += 1
   print (count)