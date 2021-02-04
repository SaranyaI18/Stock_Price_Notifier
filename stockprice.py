from yahoo_fin import stock_info

brand = input("Enter company code: ")

price = stock_info.get_live_price(brand)

print(price)

