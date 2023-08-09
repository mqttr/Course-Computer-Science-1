temperature = float(input("What is the temperature in Farenheit?  "))
humidity = float(input("What is the humidity percentage?  "))
wind = float(input("What is the wind speed in mph?  "))

temperatureOut = ""
humidityOut = ""
windOut = ""

if temperature < 32:
    temperatureOut = "very cold"
elif 32 <= temperature <= 49:
    temperatureOut = "cold"
elif 50 <= temperature <= 64:
    temperatureOut = "cool"
elif 65 <= temperature <= 79:
    temperatureOut = "moderate"
elif 80 <= temperature <= 94:
    temperatureOut = "hot"
elif temperature > 90:
    temperatureOut = "very hot"
else:
    temperatureOut = "ERROR"

if humidity < 45:
    humidityOut = "comfortable"
elif 45 <= humidity <= 65:
    humidityOut = "muggy"
elif humidity > 65:
    humidityOut = "oppressive"
else:
    humidityOut = "ERROR"

if wind < 1:
    windOut = "calm"
elif 1 <= wind <= 7:
    windOut = "light breeze"
elif 8 <= wind <= 18:
    windOut = "moderate breeze"
elif 19 <= wind <= 31:
    windOut = "strong breeze"
elif 32 <= wind <= 46:
    windOut = "moderate gale"
elif 47 <= wind <= 63:
    windOut = "strong gale"
elif 64 <= wind <= 73:
    windOut = "storm"
elif wind > 74:
    windOut = "hurricane"
else:
    windOut = "ERROR"

print(f"Today's tempreature of {temperature:.2f} is {temperatureOut}, with a {humidityOut} humidity of {humidity:.2f}%, and a {windOut}-force wind at {wind} mph.")