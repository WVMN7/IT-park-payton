import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# TMDB API sozlamalari
TMDB_API_KEY = "SIZNING_TMDB_API_KALITINGIZ"  # Bu yerga API kalitingizni kiriting
TMDB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"

# /start komandasi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom! Men KinoBotman. Film haqida ma'lumot qidirish uchun /search [film nomi] yozing.")

# Kino qidirish funksiyasi
async def search_movie(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = ' '.join(context.args)  # Foydalanuvchi yuborgan qidiruv so‘zi
    if not query:
        await update.message.reply_text("Iltimos, film nomini yozing. Masalan: /search Inception")
        return

    # TMDB API orqali qidirish
    params = {
        "api_key": TMDB_API_KEY,
        "query": query,
        "language": "en-US"
    }
    response = requests.get(TMDB_SEARCH_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        results = data.get("results", [])

        if results:
            # Birinchi natijani chiqaramiz
            movie = results[0]
            title = movie.get("title", "Noma'lum")
            overview = movie.get("overview", "Ma'lumot yo'q")
            release_date = movie.get("release_date", "Ma'lumot yo'q")
            rating = movie.get("vote_average", "Ma'lumot yo'q")

            message = (
                f"🎬 *{title}*\n"
                f"🗓️ Chiqqan sana: {release_date}\n"
                f"⭐️ Reyting: {rating}\n\n"
                f"📖 *Qisqacha*: {overview}"
            )
            await update.message.reply_text(message, parse_mode="Markdown")
        else:
            await update.message.reply_text("Hech qanday natija topilmadi. Iltimos, boshqa nom kiriting.")
    else:
        await update.message.reply_text("Xatolik yuz berdi. Keyinroq qayta urinib ko‘ring.")

# Botni ishga tushirish
if name == 'main':
    app = ApplicationBuilder().token("BOT_TOKEN").build()  # Bu yerga o'zingizning Telegram bot tokeningizni kiriting

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("search", search_movie))

    print("Bot ishga tushdi!")
    app.run_polling()