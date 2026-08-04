def infinite_hotel_menu_food():
    count = 1
    while True:
        yield f"Food {count}"
        count += 1


refill = infinite_hotel_menu_food()

for i in range(5):
    print(next(refill))
