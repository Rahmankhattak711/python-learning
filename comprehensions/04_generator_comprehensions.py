hotel_daily_sales = [
    20,
    30,
    40,
    50,
    60,
    70,
    80,
    90,
    100,
    110,
    120,
    130,
    140,
    150,
    160,
    170,
    180,
    190,
    200,
]

total_sales = sum(sale for sale in hotel_daily_sales if sale > 50)

print(total_sales)
