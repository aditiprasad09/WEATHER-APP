import tkinter as tk
from PIL import Image, ImageTk
import requests
import time


def getWeather(event):
    city = textField.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=06c921750b9a82d8f5d1294e1586276f"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))

    final_info = condition + "\n" + str(temp) + "°C"
    final_data = "\n" + "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(max_temp) + "°C" + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(humidity) + "\n" + "Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
    label1.config(text=final_info)
    label2.config(text=final_data)

# Create main window


canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")

# Load background image
bg_image = Image.open("weatherimage.jpg")  # Make sure to replace "background.jpg" with the path to your image file
bg_image = bg_image.resize((600, 500), Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a canvas widget to display the background image
background_label = tk.Label(canvas, image=bg_photo)
background_label.place(relwidth=1, relheight=1)

# Set fonts
f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

# Add Entry widget for user input
textField = tk.Entry(canvas, justify='center', width=20, font=t)
textField.pack(pady=20)
textField.focus()
textField.bind('<Return>', getWeather)

# Add labels for displaying weather information
label1 = tk.Label(canvas, font=t, bg='lightblue')
label1.pack()
label2 = tk.Label(canvas, font=f, bg='lightblue')
label2.pack()

# Start the main loop
canvas.mainloop()
