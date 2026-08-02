def ageCategorization (age):
  if age >= 60:
    return "senior"
  elif age >= 20 and age <= 59:
    return "Adult"
  elif age >= 13 and age <= 19:
    return "teenAger"
  elif age < 13:
    return "child"

# print(ageCategorization(18))

def getMovieTicketPricing(movie_name):
  if movie_name == "superman":
    return "Price is 200$"
  elif movie_name == "baby_driver":
    return "Price is 500$"
  elif movie_name == "black_man":
    return "Price is 100$"
  else:
    return "No ticket is available right now"

# print(getMovieTicketPricing("baby_driver"))

def passwordStrengthChecker(password):
  if len(password) < 6:
    print("Weak password")
  elif len(password) >= 6 and len(password) <= 10 and str(password).isalnum() == False:
    print("Moderate password")
  elif len(password) > 10 and str(password).isalnum() == False:
    print("Strong password")
  else:
    print("Invalid password")

# passwordStrengthChecker("rahm")

def getGrade(marks):
  if marks >= 90:
    return "A+"
  elif marks >= 80 and marks < 90:
    return "A"
  elif marks >= 70 and marks < 80:
    return "B"
  elif marks >= 60 and marks < 70:
    return "C"
  elif marks >= 50 and marks < 60:
    return "D"
  else:
    return "F"

# print(getGrade(75))
