#prompt user for weather condition
weather = input("whats the weather like today? (sunny/rainy/cold)")

if weather == "sunny":
    print("Wear  a T-shirt and sunglass")
elif weather == "rainy":
    print("Dont forget to take your umbrella and a raincoat")
elif weather == "cold":
    print("Make sure you wear a warm coat and a scarf")
else:
    print("Sorry, I don't have recommendations for that weather condition.")
