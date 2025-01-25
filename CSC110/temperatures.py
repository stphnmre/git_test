def celsius_to_fahrenheit(celcius):
    farenheit=celcius*1.8+32
    return round(farenheit,2)

def fahrenheit_to_celsius(farenheit):
    celcius=(farenheit-32)*5/9
    return round(celcius,2)

def main():
    print (celsius_to_fahrenheit(15))
    print (celsius_to_fahrenheit(25))
    print (celsius_to_fahrenheit(38))
    print (fahrenheit_to_celsius(100))
    print (fahrenheit_to_celsius(115))
    print (fahrenheit_to_celsius(75))

main()
