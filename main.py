
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import bot
from token_1 import TOKEN



def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Crea un comando llamado start
    # que es manejado por la función start
    dispatcher.add_handler(CommandHandler('start', bot.start))
    dispatcher.add_handler(CommandHandler('menu', bot.menu))

    dispatcher.add_handler(CallbackQueryHandler(bot.ver_todas,
                                                pattern='all'))
    dispatcher.add_handler(CallbackQueryHandler(bot.ver_constelacion, pattern='constellation'))
    dispatcher.add_handler(CallbackQueryHandler(bot.ver_estrellas, pattern='stars'))
    dispatcher.add_handler(CallbackQueryHandler(bot.cargar_constelacion))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
