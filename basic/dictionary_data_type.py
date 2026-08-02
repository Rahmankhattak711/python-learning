studInfo = {
  "name" : "Rahman Ullah",
  "age" : 20,
  "course" : "Computer Science",
  "city" : "Karachi",
  "country" : "Pakistan"
}

studInfo.pop("city")
studInfo.get("name")

for x,y in studInfo.items():
  print(x,y)


if "name" or "Rahman Ullah":
  print("Yes This is Rahman Ullah")
else:
  print("This is Not Rahman Ullah")
