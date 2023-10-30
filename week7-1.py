burger_prices = [int(input()) for _ in range(3)]
drink_prices = [int(input()) for _ in range(2)]

set_prices = [burger + drink - 50 for burger in burger_prices for drink in drink_prices]

print(min(set_prices))
