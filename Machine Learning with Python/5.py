import random
k = random.uniform(-5,5)
c = random.uniform(-5,5)

print (f"y = {k} * x + {c}")
rate = 0.0001

data = {
    22 : 150,
    23 : 155,
    24 : 160,
    25 : 162,
    26 : 171,
    27 : 174,
    28 : 180
}

def proceed (x):
    return x * k + c

for i in range(100000):
    x = random.choice(list(data.keys()))
    true_result = data[x]
    out = proceed(x)
    delta = true_result - out
    k += delta * rate * x
    c += delta * rate
print (f"y = {k} * x + {c}")