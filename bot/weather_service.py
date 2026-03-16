# bot/weather_service.py
import requests
import os

def get_weather(city_name):
    """Consulta el clima actual de una ciudad usando OpenWeatherMap."""
    api_key = os.getenv("WEATHER_API_KEY")
    url = f"http://api.openweather.com/data/2.5/weather?q={city_name}&appid={api_key}&units=metric&lang=es"
    
    try:
        response = requests.get(url )
        response.raise_for_status()
        data = response.json()
        
        # Extraemos la información relevante
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        humidity = data['main']['humidity']
        
        return f"En {city_name} hace {temp}°C con {desc}. Humedad: {humidity}%."
    except Exception:
        return "Lo siento, no he podido encontrar esa ciudad. Revisa el nombre e inténtalo de nuevo."
