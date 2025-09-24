import tkinter as tk
from tkinter import ttk
import requests

API_KEY = "b866c315840b05d9c142862425e8c066"
URL = "http://api.openweathermap.org/data/2.5/weather"

root = tk.Tk()
root.title("Weather App")
root.geometry("450x500")
root.configure(bg="#2E4053")

style = ttk.Style()
style.configure("TButton", font=("Arial", 612, "bold"), padding=8)
style.configure("TEntry", font=("Arial", 124))
style.configure("TLabel", background="#2E4053", foreground="white", font=("Arial", 12))

def get_weather():
    city = city_entry.get()
    if city:
        try:
            url = f"{URL}?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                data = response.json()
                city_name = data["name"]
                country = data["sys"]["country"]
                temp = data["main"]["temp"]
                humidity = data["main"]["humidity"]
                description = data["weather"][0]["description"].title()
                icon = "☀️"
                if "cloud" in description.lower():
                    icon = "☁️"
                elif "rain" in description.lower():
                    icon = "🌧️"
                elif "snow" in description.lower():
                    icon = "❄️"
                result = (
                    f"{icon} {description}\n\n"
                    f"🌍 City: {city_name}, {country}\n"
                    f"🌡️ Temperature: {temp} °C\n"
                    f"💧 Humidity: {humidity}%"
                )
            else:
                result = "⚠️ City not found!"
        except requests.exceptions.RequestException:
            result = "❌ Network error. Please try again."
    else:
        result = "⚠️ Please enter a city name."
    weather_label.config(text=result)

header = tk.Label(root, text="🌤️ Weather App 🌍", font=("Arial", 20, "bold"),
                  bg="#2E4053", fg="white")
header.pack(pady=20)

frame = tk.Frame(root, bg="#2E4053")
frame.pack(pady=10)

city_entry = ttk.Entry(frame, width=25)
city_entry.grid(row=0, column=0, padx=5)

get_button = ttk.Button(frame, text="Get Weather", command=get_weather)
get_button.grid(row=0, column=1, padx=5)

weather_label = tk.Label(root, text="", font=("Arial", 14), bg="#34495E", fg="white",
                         justify="left", width=40, height=10, anchor="nw", bd=2, relief="groove")
weather_label.pack(pady=30)

root.mainloop()
