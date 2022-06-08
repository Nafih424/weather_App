import tkinter as tk
import requests
import time

def get_weather(canvas):
    city = textfield.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=9c207fd8e8b4fa7b4c7d2cf7efbd7c6a"
    json_data = requests.get(api).json()
    condition = json_data["weather"][0]["main"]
    temp = int(json_data["main"]["temp"] - 273.15)
    temp_min = int(json_data["main"]["temp_min"] - 273.15)
    temp_max = int(json_data["main"]["temp_max"] - 273.15)

    final_info = condition + "\n" + str(temp) + "C" 

    final_data = "\n" + "Max Temp :" +str(temp_max) + "\n" + "Min temp :" +str(temp_min)

    label1.config(text=final_info)
    label2.config(text=final_data)


canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")


f = ("poppins" , 15 , "bold")

t = ("poppins" , 35 , "bold")

textfield = tk.Entry(canvas,font=f)
textfield.pack(pady=20)
textfield.bind('<Return>',get_weather   )

label1 =tk.Label(canvas, font= t)
label1.pack()

label2 =tk.Label(canvas, font= f)
label2.pack()

canvas.mainloop()