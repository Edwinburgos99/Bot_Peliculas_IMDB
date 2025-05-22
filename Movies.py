#Librerias usadas
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests 
import os
from dotenv import load_dotenv
from deep_translator import GoogleTranslator

# Carga las variables desde el archivo .env
load_dotenv("secretKeys.env")

# Se obtiene los valores correspodientes a las variables de entorno del sistema operativo mediante os.getenv()
OMDB_API_KEY = os.getenv("OMDB_API_KEY")
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Se define una función start que se ejecuta de manera asíncrona cuando el usuario inicia una conversación con el bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hola! Envíame el nombre de una película o serie para ver su calificación.")

# Se define otra función asíncrona search_list, que responde con una lista de peliculas o series en base a la palabra digitada, cuando un usuario busca una película o serie
async def search_list(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Por favor, escribe una palabra clave para buscar películas (por ejemplo: /buscarlist batman).")
        return
        
    # Se toma lo que el usuario escribió después del comando (/buscarlist) y se convierte en una cadena
    query = ' '.join(context.args)
    # Se crea la URL para hacer la consulta a la OMDB API, usando la clave OMDB_API_KEY y el parámetro s, que se usa para búsquedas generales
    url = f"http://www.omdbapi.com/?apikey={OMDB_API_KEY}&s={query}"

    # Consulta a la API: Se hace la petición HTTP a la URL de la API usando requests.get(), La respuesta se convierte en un diccionario de Python con response.json()
    response = requests.get(url)
    data = response.json()

    # condicional que busca si hay resultados con respecto a la entrada de busquedad y sino envia mensaje de notificacion
    if data.get("Response") == "True" and "Search" in data:
        movies = data["Search"]# Se extraen las películas encontradas
        results = "\n".join([f"🎬 {movie['Title']} ({movie['Year']})" for movie in movies])# Se crea una cadena con todos los títulos y años de las películas, usando un emoji 🎬 por cada una
        await update.message.reply_text(f"Resultados para '{query}':\n\n{results}")
    else:
        if data.get("Response") == "False":
            await update.message.reply_text("No encontré resultados para esa búsqueda.")
        else:
            await update.message.reply_text("Hubo un error con la búsqueda. Intenta nuevamente.")
# define una función search que permite al bot de Telegram buscar información detallada de una película o serie específica usando el título exacto
async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Por favor, escribe el nombre de la película o serie.")
        return
    # Preparar y realizar la consulta: Se genera una URL para buscar una película o serie específica, usando el parámetro t de la OMDB API (que busca por título exacto).
    query = ' '.join(context.args)
    url = f"http://www.omdbapi.com/?apikey={OMDB_API_KEY}&t={query}"
    # Llamar a la API y procesar la respuesta: Se hace la solicitud HTTP a OMDB y se convierte la respuesta en un diccionario de Python
    response = requests.get(url)
    data = response.json()
    
    if data["Response"] == "True":
        plot_es = GoogleTranslator(source='en', target='es').translate(data['Plot'])# Usa GoogleTranslator de la librería deep-translator para traducir la descripción (Plot) del inglés al español
        # Preparar y enviar el mensaje: Crea un mensaje con el título, el año, la calificación IMDB y la sinopsis traducida
        msg = (
            f"🎬 *{data['Title']}* ({data['Year']})\n"
            f"📊 IMDB: {data['imdbRating']}/10\n"
            f"📄 {plot_es}"
        )
        poster_url = data.get("Poster", None)
        await update.message.reply_text(msg, parse_mode="Markdown")# Envía ese mensaje al usuario, usando formato Markdown (para poner el título en negrita)
        # Enviar el póster: Si hay una URL válida del póster, el bot también lo envía como imagen
        if poster_url and poster_url != "N/A":
            await update.message.reply_photo(poster_url)
    else:
        await update.message.reply_text("No encontré esa película o serie.", parse_mode="Markdown")

#  inicia el bot de Telegram y le dice qué funciones ejecutar cuando los usuarios envían comandos
app = ApplicationBuilder().token(BOT_TOKEN).build()# Se construye la aplicación principal del bot usando la librería python-telegram-bot, Se pasa el token del bot (almacenado en la variable de entorno BOT_TOKEN) para conectarse con Telegram
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("buscar", search))
app.add_handler(CommandHandler("buscarlist", search_list))
# Iniciar el bot
app.run_polling()
