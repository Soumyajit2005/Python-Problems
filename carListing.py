def car_listing(car_prices):
    result = ""
    for keys in car_prices:
        result += "{} costs {} dollars".format(keys, car_prices[keys]) + "\n"
    return result


print(car_listing({"Kia Soul": 19000, "Lamborghini Diablo": 55000,
      "Ford Fiesta": 13000, "Toyota Prius": 24000}))
