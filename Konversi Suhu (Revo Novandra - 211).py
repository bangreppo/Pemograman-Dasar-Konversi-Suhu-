# Input suhu
celsius = float(input("Masukkan suhu dalam Celsius: "))
fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))
kelvin = float(input("Masukkan suhu dalam Kelvin: "))

# Konversi suhu
celcius_fahrenheit = (celsius * 9/5) + 32
farenheit_celsius = (fahrenheit - 32) * 5/9
celcius_kelvin = celsius + 273.15
kelvin_celcius = kelvin - 273.15

print()

# Output hasil konversi
print("Konversi suhu",celsius ,"celcius ke farenheit adalah",celcius_fahrenheit,"°F")
print("Konversi suhu",fahrenheit ,"farenheit ke celcius adalah",farenheit_celsius,"°C")
print("Konversi suhu",kelvin ,"celcius ke kelvin adalah",celcius_kelvin,"°K")
print("Konversi suhu",celsius ,"kelvin ke celcius adalah",kelvin_celcius,"°C")

