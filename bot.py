pip install python-telegram-bot
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Botni ishlatish uchun Token
TOKEN = 'Sizning_Tokeningiz'

# Start komandasi
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Salom! Kino botiga xush kelibsiz. Kino izlash uchun /search <kino nomi> deb yozing.")

# Kino qidirish komandasi
def search_movie(update: Update, context: CallbackContext) -> None:
    if context.args:
        movie_name = " ".join(context.args)
        # Kino haqida ma'lumot olish uchun API qo'llanilishi mumkin, masalan OMDB API
        # Misol uchun: https://www.omdbapi.com/
        # API orqali kino ma'lumotlarini olish va foydalanuvchiga yuborish
        response = f"Qidirgan kinongiz: {movie_name}"
        update.message.reply_text(response)
    else:
        update.message.reply_text("Iltimos, kino nomini kiriting. Masalan: /search Matrix")

def main():
    # Updater va Dispatcher yaratish
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    
    # Komandalar uchun handlerlar qo'shish
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("search", search_movie))
    
    # Botni ishga tushirish
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()