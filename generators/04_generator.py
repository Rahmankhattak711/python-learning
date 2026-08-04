def local_food():
  yield "Biriyani"
  yield "Pani Puri"
  yield "Rice"

def imported_food():
  yield "Noodles"
  yield "Pasta"
  yield "Pizza"

def all_food():
  yield from local_food()
  yield from imported_food()

def all_food():
  try:
    while True:
      order = yield "What would you like to order?"
  except:
    print("Thanks for ordering!")

print(next(all_food()))
all_food().close()
