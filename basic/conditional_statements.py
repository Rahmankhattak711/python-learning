age = 20

if age >= 18:
  print("You are under 18")
else:
  print("You are over 18")

marks = 75

if marks >= 90:
  print("You got an A+")
elif marks >= 80:
  print("You got an A")
elif marks >= 70:
  print("You got an B")
elif marks >= 60:
  print("You got an C")
elif marks >= 50:
  print("You got an D")
else:
  print("You got an F")

is_weekend = False
is_holiday = True

if is_weekend or is_holiday:
  print("No work today")

logged_in = False

if not logged_in:
  print("Please log in")

name = ""

if name:
  print("Name is " + name)
else:
  print("Name is empty")
