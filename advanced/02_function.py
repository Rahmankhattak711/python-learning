def calculate_tea_price(tea_type, per_cup_price, number_of_cups):
    tea_varients_price = {
        "green": per_cup_price * number_of_cups,
        "black": per_cup_price * number_of_cups,
        "herbal": per_cup_price * number_of_cups,
        "earl_grey": per_cup_price * number_of_cups,
    }

    if tea_type in tea_varients_price:
        return f"The total price for {number_of_cups} cups of {tea_type} tea is: ${tea_varients_price[tea_type]:.2f}"
    else:
        return (
            "Invalid tea type. Please choose from green, black, herbal, or earl_grey."
        )


print(calculate_tea_price("herbal", 2, 3))
