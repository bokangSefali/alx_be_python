currentWeather = input("What's the weather like today? (sunny/rainy/cold):").lower()

if currentWeather == "sunny" :
    print("Wear a t-shirt and sunglasses.")
elif currentWeather == "rainy":
    print("Dont forget your umbrella and a raincoat.")
elif currentWeather == "cold":
    print("Make sure to wear a warm coat and scarf.")
else:
    print("Sorry, I dont have recommendations for this weather.")


