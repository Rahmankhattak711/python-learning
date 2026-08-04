def hotel_menu():
    yield "Breakfast"
    yield "Lunch"
    yield "Dinner"
    yield "Dessert"


print_menu = hotel_menu()

# print(next(print_menu))
# print(next(print_menu))
# print(next(print_menu))
# print(next(print_menu))

for item in print_menu:
    print(item)
