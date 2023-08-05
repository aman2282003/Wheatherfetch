import requests

city_input = input("Enter Your City Name: ")

api_key = "33107e5d1eb15e50a2f9f94c1addb2d4"


def get_weather(api_key, city_input):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_input}&appid={api_key}"

    url_response = requests.get(url).json()

    temperature = url_response["main"]["temp"]

    temp_old = (temperature)-273.15  # coverts to C
    temp = format(temp_old, ".2f")

    print("The temperature in", city_input, "is", str(temp)+"°C")


get_weather(api_key, city_input)


# made with ❤️ by Aman
# Name = Amandeep singh
# Batch = Cap04
# cap_id = cap04_027
