import requests
import json

def obtener_datos_climaticos(ciudad="Madrid"):
    """Function to obtain weather data for a city using the OpenWeatherMap API."""
    api_key = '7a9762d5480bb8886629550cb1fa2f7f'  # Replace the key with your real API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

def imprimir_clima(data):
    """Function to print the weather details in a formatted manner."""
    nombre_ciudad = data['name']
    temp_actual = data['main']['temp']
    descripcion = data['weather'][0]['description']
    country = data['sys']['country']

    print(f"Country: {country}")
    print(f"City: {nombre_ciudad}")
    print(f"Current Temperature: {temp_actual}°C")
    print(f"Weather Condition: {descripcion}")


def main():
    ciudad = input("Enter the city name to get its weather information (default is Madrid): ")
    if not ciudad:  # If no city name is entered, use Madrid as default
        ciudad = "Madrid"
    datos_climaticos = obtener_datos_climaticos(ciudad)
    if datos_climaticos.get("cod") != 200:
        print("Error retrieving the weather data.")
    else:
        imprimir_clima(datos_climaticos)

if __name__ == "__main__":
    main()