ice_cream_shop = {
    "vanilla": 140,
    "chocolate": 300,
    "strawberry": 100,
    "raspberry": 50,
    "blueberry": 300,
}

convert_to_dollars = {name: price / 277 for name, price in ice_cream_shop.items()}

print(convert_to_dollars)
