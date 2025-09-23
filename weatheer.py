
import tkinter as tk
import requests

API_KEY = "d71732a26007b8246ad3aa2d92326eac"
URL = "http://api.openweathermap.org/data/2.5/weather"

root = tk.Tk()
root.title("Weather App")
root.geometry("400x400")

# Function to fetch weather
def get_weather():
    city = city_entry.get()
    if city:
        url = f"{URL}?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            city_name = data["name"]
            country = data["sys"]["country"]
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            description = data["weather"][0]["description"].title()

            result = (
                f"City: {city_name}, {country}\n"
                f"Temperature: {temp} °C\n"
                f"Humidity: {humidity}%\n"
                f"Condition: {description}"
            )
        else:
            result = "City not found!"
    else:
        result = "Please enter a city name."

    weather_label.config(text=result)


tk.Label(root, text="Enter City Name:", font=("Arial", 12)).pack(pady=10)

city_entry = tk.Entry(root, font=("Arial", 14))
city_entry.pack(pady=5)

get_button = tk.Button(root, text="Get Weather", command=get_weather, font=("Arial", 12))
get_button.pack(pady=10)

weather_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
weather_label.pack(pady=20)


root.mainloop()