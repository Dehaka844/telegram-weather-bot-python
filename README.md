# Telegram Weather Bot (Python)

Este es un bot de Telegram interactivo que proporciona información meteorológica en tiempo real. Utiliza la librería `python-telegram-bot` para la comunicación con Telegram y la API de `OpenWeatherMap` para obtener los datos climáticos.

## Características
- Respuesta automática a comandos (`/start`, `/help`).
- Consulta de clima por nombre de ciudad.
- Manejo seguro de credenciales mediante variables de entorno.
- Estructura modular y asíncrona.

## Tecnologías Utilizadas
- **Python 3.11+**
- **python-telegram-bot:** Framework asíncrono para bots de Telegram.
- **Requests:** Para el consumo de la API REST de OpenWeatherMap.
- **python-dotenv:** Gestión de configuración y seguridad.

## Configuración
1. Obtén un token de bot a través de [@BotFather](https://t.me/botfather ).
2. Obtén una API Key gratuita en [OpenWeatherMap](https://openweathermap.org/api ).
3. Copia el archivo `.env.example` a `.env` y rellena tus claves:
   ```env
   TELEGRAM_TOKEN=tu_token
   WEATHER_API_KEY=tu_api_key
   ```
4. Instala las dependencias: `pip install -r requirements.txt`.
5. Ejecuta el bot: `python main.py`.
