"""
    Name: weather_gui_3.py
    Author: Adam Frisch
    Created: 4/21/2022
    Purpose: OOP Tkinter GUI to get and display OpenWeatherMap data based on user input.

"""
import weather_utils
from tkinter import *
from tkinter.ttk import *
import requests

class OWMGUI:

    def __init__(self):
        self.root = Tk()
        self.root.title("Adam's Weather App")
        self.root.geometry("300x325")
        self.root.iconbitmap("weather.ico")
        # Call methods to create frames and widgets
        self.create_frames()
        self.create_widgets()
        # Start program main loop
        mainloop()

#--------------------------GET WEATHER--------------------------#
    def get_weather(self, *args):
        try:
            # Get the location
            location = self.location_entry.get()

            # Build the openweathermap request parameters
            # These are added on to the URL to make the complete request
            query_string = {
                "units": "imperial",    # Units of measure ex: Fahrenheit
                "q": location,          # Location for weather
                "appid": weather_utils.API_KEY
            }

            # Get the API JSON data as a Python JSON object
            response = requests.get(
                weather_utils.URL,
                params=query_string
            )

            # Load JSON response into a weather dictionary
            weather_data = response.json()

            # Get current fahrenehit temperature
            self.temperature = weather_data.get("main").get("temp")

            # Get detailed weather status
            self.description = weather_data.get(
                "weather")[0].get("description").title()

            # Get humidity
            self.humidity = weather_data.get("main").get("humidity")

            # Get wind speed
            self.speed = weather_data.get("wind").get("speed")

            # Get cloud cover percentage
            self.cloud = weather_data.get("clouds").get("all")


            # Call display weather method
            self.display_weather()
        except:
            # raise
            print("[-] Sorry, there was a problem connecting.")

#--------------------------DISPLAY WEATHER--------------------------#
    def display_weather(self):
        # Set the weather information in the value labels
        self.lbl_temperature_value.configure(text=f'{self.temperature:.1f} °F \U0001F321')
        self.lbl_description_value.configure(text=self.description)
        self.lbl_humidity_value.configure(text=f'{self.humidity:.1f}%')
        self.lbl_speed_value.configure(text=f'{self.speed:.2f} mph \U0001F4A8')
        self.lbl_cloud_value.configure(text=f'{self.cloud}% \U00002601')
        
        

        # Set focus to the entry box for the next location
        self.location_entry.focus_set()
        # Select text in the entry box for next entry
        self.location_entry.select_range(0, END)

#-------------------------CREATE FRAMES-------------------------#
    def create_frames(self):
        self.title_frame = Frame(self.root, relief=FLAT)
        self.entry_frame = LabelFrame(
            self.root, text="Location", relief=GROOVE)
        self.weather_frame = LabelFrame(
            self.root, text="Weather", relief=GROOVE)

        self.title_frame.pack(fill=X)
        self.entry_frame.pack(fill=X)
        self.weather_frame.pack(fill=X)

        self.title_frame.pack_propagate(False)
        self.entry_frame.pack_propagate(False)
        self.weather_frame.pack_propagate(False)

#-------------------------CREATE WIDGETS-------------------------#
    def create_widgets(self):
        # Create entry widget and set focus
        self.location_entry = Entry(self.entry_frame, width=25)
        self.location_entry.focus_set()

        # Create button to get weather from location
        self.btn_weather = Button(
            self.entry_frame,
            text="Show Weather",
            command=self.get_weather
        )

        # Create description labels
        self.lbl_app_title = Label(self.title_frame, text="Adam's Weather App",
                                       font=("Courier", 16, "bold"))
        self.lbl_location = Label(self.entry_frame, text="Enter Location:")
        self.lbl_temperature = Label(self.weather_frame, text="Temperature:")
        self.lbl_description = Label(self.weather_frame, text="Description:")
        self.lbl_humidity = Label(self.weather_frame, text="Humidity:")
        self.lbl_speed = Label(self.weather_frame, text="Wind Speed:")
        self.lbl_cloud = Label(self.weather_frame, text="Cloud Coverage:")
        
        

        # Create value display labels
        self.lbl_temperature_value = Label(
            self.weather_frame, width=20, anchor=W, relief=GROOVE)
        self.lbl_description_value = Label(
            self.weather_frame, width=20, anchor=W, relief=GROOVE)
        self.lbl_humidity_value = Label(
            self.weather_frame, width=20, anchor=W, relief=GROOVE)
        self.lbl_speed_value = Label(
            self.weather_frame, width=20, anchor=W, relief=GROOVE)
        self.lbl_cloud_value = Label(
            self.weather_frame, width=20, anchor=W, relief=GROOVE)
        
        

        # Grid the widgets
        self.lbl_app_title.grid(row=0, column=0)

        self.lbl_location.grid(row=0, column=0, sticky=E)
        self.location_entry.grid(row=0, column=1, sticky=W)
        self.btn_weather.grid(row=1, column=1, sticky=W)

        self.lbl_temperature.grid(row=3, column=0, sticky=E)
        self.lbl_temperature_value.grid(row=3, column=1, sticky=W)

        self.lbl_description.grid(row=4, column=0, sticky=E)
        self.lbl_description_value.grid(row=4, column=1, sticky=W)

        self.lbl_humidity.grid(row=5, column=0, sticky=E)
        self.lbl_humidity_value.grid(row=5, column=1, sticky=W)

        self.lbl_speed.grid(row=6, column=0, sticky=E)
        self.lbl_speed_value.grid(row=6, column=1, sticky=W)

        self.lbl_cloud.grid(row=7, column=0, sticky=E)
        self.lbl_cloud_value.grid(row=7, column=1, sticky=W)

        # Set padding for all widgets in window
        self.title_frame.pack_configure(padx=10, pady=(10, 0))
        self.entry_frame.pack_configure(padx=10, pady=(10, 0))
        self.weather_frame.pack(padx=10, pady=10)
        for widget in self.entry_frame.winfo_children():
            widget.grid_configure(padx=3, pady=3)
        for widget in self.weather_frame.winfo_children():
            widget.grid_configure(padx=3, pady=3)
        # Set focus to the entry box for the next location
        self.location_entry.focus_set()

        # The enter key will activate the calculate method
        self.root.bind('<Return>', self.get_weather)
        
        
owm_gui = OWMGUI()
    
        
        
