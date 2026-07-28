import random

x = 10.897
int(x)

y = 10
float(y)

print(type(x))
print(type(y))

reverse_x = 100 ** 2
print(reverse_x)

x_power = 2 ** 1000
print(x_power)

x = random.randint(1, 100)
print(x)

colors = ["red", "green", "blue"]
print(random.choice(colors))
print(random.shuffle(colors))

setone = {1,2,3,4}
settwo = {3,4,5,6}
setone & settwo
setone | settwo
print(setone.union(settwo))
print(setone.intersection(settwo))
