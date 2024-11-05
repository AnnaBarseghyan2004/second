number = int(input())

reversed_number = 0
temp = number 

while temp > 0 :
    x = temp % 10
    reversed_number = reversed_number * 10 + x 
    temp = temp // 10

print (reversed_number)
    
