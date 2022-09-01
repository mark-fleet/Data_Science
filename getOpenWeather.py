# DSC 510
# Week 10
# Programming Assignment Week 10, Final
# Author Mark Fleet
# 08/13/22
# importing the required libraries
import requests
from datetime import datetime
from datetime import date

# function to gather information from the user to process weather through a city and state
# function makes two API calls, one to get lat/lon via direct geocoding and a second to call weather info
# based on that lat/lon data


def get_weather1():
    now = datetime.now()
    current_time = now.strftime("%H:%M %p")
    today = date.today()
    city_name = input("What is the name of the city? ")
    state_cd = input("What is the state code? ")
    choice = input("Please enter 'F' to view in Fahrenheit and enter 'C' to view in Celsius: ")
    for choice1 in choice:
        if choice == ('F' or 'f'):
            choice1 = 'imperial'
        elif choice == ('C' or 'c'):
            choice1 = 'metric'
    api_key = '52342d9e12b49e43714ce7f5f7333a96'
    response = requests.get(f'https://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_cd},us&appid={api_key}')
    data = response.json()
    try:
        data
    except data.exceptions.ConnectionError:
        print("Oops, something went wrong")
    lat = data[0]['lat']
    lon = data[0]['lon']
    get_weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units={choice1}')
    for get_weather.status_code in get_weather:
        if get_weather.status_code != 200:
            break
        print("Oops, something went wrong.  Try again.")
        continue
    weather_data = get_weather.json()
    temperature = weather_data['main']['temp']
    weather_desc = weather_data['weather'][0]['main']
    pressure = weather_data['main']['pressure']
    humidity = weather_data['main']['humidity']
    wind = weather_data['wind']['speed']
    high_temp = weather_data['main']['temp_max']
    low_temp = weather_data['main']['temp_min']
    print("     **************************************************")
    print("     *", "As of Today's date:", today, "at ", current_time, "  ", "*")
    print("     *", "Weather for: ", city_name, "     ", state_cd, "             ", ' ', "*")
    print("     *", "Currently the temperature is: ", "       ", f'{temperature}{choice}', '', "*")
    print("     *", "Today's high is:", "                   ", f'{high_temp}{choice}', '  ', "*")
    print("     *", "Today's low is:", "                   ", f'{low_temp}{choice}', '   ', "*")
    print("     *", "The Sky conditions are: ", "       ", f'{weather_desc}', '      ', "*")
    print("     *", "The pressure is: ", "                ", f'{pressure}hPa', '   ', "*")
    print("     *", "The humidity is: ", "                   ", f'{humidity}%', '    ', "*")
    print("     *", "The speed of wind is: ", "           ", f'{wind}m/s', '   ', "*")
    print("     **************************************************")

# function to gather information from the user to process weather through a zip code
# function makes two API calls, one to get lat/lon via direct geocoding and a second to call weather info
# based on that lat/lon data.  We also get the city name from the first call which his then passed to the output


def get_weather2():
    now = datetime.now()
    current_time = now.strftime("%H:%M %p")
    today = date.today()
    zip_code = input("Please enter a valid zip code to continue: ")
    choice = input("Please enter 'F' to view in Fahrenheit and enter 'C' to view in Celsius: ")
    for choice1 in choice:
        if choice == ('F' or 'f'):
            choice1 = 'imperial'
        elif choice == ('C' or 'c'):
            choice1 = 'metric'
    api_key = '52342d9e12b49e43714ce7f5f7333a96'
    response = requests.get(f'http://api.openweathermap.org/geo/1.0/zip?zip={zip_code},US&appid={api_key}')
    data = response.json()
    try:
        data
    except data.exceptions.ConnectionError:
        print("Oops, something went wrong")
    lat = data['lat']
    lon = data['lon']
    city_name = data['name']
    get_weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units={choice1}')
    for get_weather.status_code in get_weather:
        if get_weather.status_code != 200:
            break
        print("Oops, something went wrong.  Try again.")
        continue
    weather_data = get_weather.json()
    temperature = weather_data['main']['temp']
    weather_desc = weather_data['weather'][0]['main']
    pressure = weather_data['main']['pressure']
    humidity = weather_data['main']['humidity']
    wind = weather_data['wind']['speed']
    high_temp = weather_data['main']['temp_max']
    low_temp = weather_data['main']['temp_min']
    print("     **************************************************")
    print("     *", "As of Today's date:", today, "at ", current_time, "  ", "*")
    print("     *", "Weather for: ", city_name, "  ", zip_code, "             ", ' ', "*")
    print("     *", "Currently the temperature is: ", "       ", f'{temperature}{choice}', '', "*")
    print("     *", "Today's high is:", "                   ", f'{high_temp}{choice}', '  ', "*")
    print("     *", "Today's low is:", "                    ", f'{low_temp}{choice}', '   ', "*")
    print("     *", "The Sky conditions are: ", "        ", f'{weather_desc}', '      ', "*")
    print("     *", "The pressure is: ", "                ", f'{pressure}hPa', '   ', "*")
    print("     *", "The humidity is: ", "                   ", f'{humidity}%', '    ', "*")
    print("     *", "The speed of wind is: ", "          ", f'{wind}m/s', '   ', "*")
    print("     **************************************************")


# main program with loop for user to enter as many inputs they want until exiting loop

def main():
    while True:
        choice = input("Welcome to the WeatherApp! \n To look up the weather forecast by city and state enter '1'. To "
                       "look up the weather forecast by zip code enter'2'.  To End simply enter 'E': ")
        if choice == ('E' or 'e'):
            break
        if choice not in ('1', '2', 'E', 'e'):
            print("This is not a valid choice.  Please re-enter using a valid selection.")
            continue
        if choice == '1':
            get_weather1()
        if choice == '2':
            get_weather2()
    print("Thank you for using the WeatherApp!  Have a great day!")


if __name__ == '__main__':
    main()
