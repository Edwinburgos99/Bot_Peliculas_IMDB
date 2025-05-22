# Bot de telegram para buscar información de peliculas y series basado en IMBD (Base de Datos de películas en Internet)

Este proyecto es un bot de Telegram desarrollado en Python que permite buscar **películas y series** mediante su nombre, mostrando el **Año, calificación IMDB, descripción traducida al español** y el **póster**. La información se obtiene usando la **OMDB API**, y la descripción se traduce utilizando **GoogleTranslator** de `deep-translator`.

[**OMDB API**](https://www.omdbapi.com/)

Una vez se encuentre en la pagina indicada, debe ir a la pestaña API Key de la pagina web y dar click, una vez se encuentre dentro de la pestaña API Key, digite un correo electronico activo y de click en el boton submit para enviar las llaves correspodientes para el uso de la API gratis la cual permite 1000 peticiones como limite.

# Creación del bot de telegram

Se ingresa en la app de Telegram y en el buscador se coloca BotFather, se ingresa en la opción que se muestre, una vez dentro se coloca el comando /newbot para la creación de un nuevo bot, luego se pedira que escoja un nombre para el bot puede ser cualquiera que te guste, por ultimo te pedira crear un nombre de usuario. Al final el chat te enviara un mensaje diciendo que el bot se creo correctamente y te indicara el token que necesitaras para las variables de entorno.

# Uso del bot

/start – Inicia la conversación con el bot

/buscarlist <palabra> – Busca una lista de películas/series con la palabra clave

/buscar <nombre exacto> – Busca detalles de una película o serie específica

# Creación del archivo secretKeys

En la carpeta del proyecto crear un archivo .env para las variables de entorno, las variables se estableceran como la llave OMDB_API_KEY y la llave TELEGRAM_BOT_TOKEN, ambas llaves ya se encuentra disponibles para cada usuario en los anteriores procesos realizados.

# Creación del archivo requirements.txt

Para empezar se crea un archivo .txt en la carpeta del proyecto, luego se procede a instalar las dependencias del archivo con el siguiente comando en la terminal del proyecto "pip install -r requirements.txt".

## 🚀 Funcionalidades

📌 Buscar información detallada de una película o serie (`/buscar`)

📌 Buscar una lista de coincidencias por palabra clave (`/buscarlist`)

📌 Ver título, año, calificación IMDB y descripción traducida

📌 Recibir la imagen del póster (si está disponible)

## 🛠️ Tecnologías utilizadas

📌 Python

📌 [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)

📌 OMDB API

📌 Deep Translator (Google Translate)

📌 dotenv

# Estructura del proyecto

.

├── Movies.py # Código principal del bot

├── secretKeys.env # Variables de entorno

├── requirements.txt # Lista de dependencias

├── Readme.md # Documentación del proyecto

├── .gitignore # Archivos y carpetas ignorados por Git

└── env/ # Entorno virtual

Desarrollado por [Edwin Burgos - "Ingeniero de sistemas"] como un proyecto de aprendizaje e integración de APIs con bots de Telegram.
