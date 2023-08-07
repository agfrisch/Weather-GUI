"""

    Name: weather_utils.py
    Author: Adam Frisch
    Created: 3/30/2022
    Purpose: Store OpenWeatherMap API key and URL for
    easy import into other OperWeatherMap programs

"""
import datetime

# OpenWeatherMap API Key
API_KEY = "1b8188ead5bad49cc80f38a47fb1fc27"

# URL to access current weather OpenWeatherMap API
URL = "https://api.openweathermap.org/data/2.5/weather"

WEATHER_BANNER ="""
 __          __        _   _                
 \ \        / /       | | | |               
  \ \  /\  / /__  __ _| |_| |__   ___ _ __  
   \ \/  \/ / _ \/ _` | __| '_ \ / _ \ '__| 
    \  /\  /  __/ (_| | |_| | | |  __/ |    
     \/  \/ \___|\__,_|\__|_| |_|\___|_|                                                                                            
"""

#------------------CONVERT TIME-----------------------#

def convert_time(time):

    time = datetime.datetime.fromtimestamp(time)

    time = f"{time:%I:%M:%S %p}"

    time = time.lstrip("0")

    return time


    
