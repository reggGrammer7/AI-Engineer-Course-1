tea_prices_inr = {
    "masala" : 40,
    "green tea ": 50,
    "lemon tea": 200
}
# print(tea_prices_inr.items())
# Convering prices to dollars
tea_prices_usd = {tea:price/80 for tea, price in tea_prices_inr.items()}
print(tea_prices_usd)