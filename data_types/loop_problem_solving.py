# Count the number of even numbers from 1 to 10
numbers = 10
n = 0
for number in range(1 , numbers + 1):
  if number % 2 == 0:
    n += 1

# print(n)

# Print the first non-repeated character
name = "rahmanullah"
for i in name:
  print(i)
  if name.count(i) == 1:
    print(i)
    break

# 1 <= number <= 30
while True:
  number = int(input("Enter a number: "))
  if 1 <= number <= 30:
    print("Thanks")
    break
  else:
    print("Please enter a number between 1 and 30")
