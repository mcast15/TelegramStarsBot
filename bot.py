from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import os.path
from modelo import Modelo

m = Modelo()


# --------------------- Comandos -----------------------------

def start(update, context):
    try:
        update.message.reply_text('¡Hola! Bienvenido(a), soy un bot que te ayudará a visualizar'
                                  ' lo impresionante que es el universo con sus estrellas'
                                  ' y constelaciones. %s %s\n\nSi quieres ver qué puedo hacer '
                                  'solamente tienes que ejecutar el comando /menu.' % (u'\U0001F60A', u'\U0001F31F'))
    except Exception as e:
        print('Error en start: ', e)


def menu(update, context):
    update.message.reply_text(main_menu_message(),
                              reply_markup=main_menu_keyboard())


# -------------------- Keyboards -------------------------

def main_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton('Las estrellas', callback_data='stars')],
        [InlineKeyboardButton('Estrellas y una constelación', callback_data='constellation')],
        [InlineKeyboardButton('Quiero ver las estrellas y constelaciones', callback_data='all')]
    ]
    return InlineKeyboardMarkup(keyboard)


def constellation_menu_keyboard():
    keyboard = [
        [
            InlineKeyboardButton('1', callback_data='Boyero'),
            InlineKeyboardButton('2', callback_data='Casiopea'),
            InlineKeyboardButton('3', callback_data='Cazo'),
            InlineKeyboardButton('4', callback_data='Cygnet')
        ],
        [
            InlineKeyboardButton('5', callback_data='Geminis'),
            InlineKeyboardButton('6', callback_data='Hydra'),
            InlineKeyboardButton('7', callback_data='Osa Mayor'),
            InlineKeyboardButton('8', callback_data='Osa Menor')
        ]
    ]
    return InlineKeyboardMarkup(keyboard)


# ----------------- Messages ----------------

def main_menu_message():
    return 'Por favor, hazme saber qué te gustaría ver %s:' % u'\U0001F914'


def constellation_menu_message():
    return '''Selecciona el botón correspondiente a la constelación que deseas ver: 
                1.  Boyero
                2.  Casiopea
                3.  Cazo
                4.  Cygnet
                5.  Geminis
                6.  Hydra
                7.  Osa Mayor
                8.  Osa Menor'''


# --------------------------------------------------------

def ver_estrellas(update, context):
    try:
        query = update.callback_query
        chat_id = query.message.chat.id
        query.edit_message_text(text="¡Listo! Te mostraré las estrellas.")
        if not os.path.isfile('generated/stars.png'):
            m.plot_stars()
        context.bot.send_photo(chat_id, open('generated/stars.png', 'rb'))
    except Exception as e:
        print('Error:', e)


def ver_todas(update, context):
    try:
        chat_id = update.callback_query.message.chat.id
        query = update.callback_query
        query.edit_message_text(text="¡Fantástico! Observa todas las estrellas y constelaciones.")
        if not os.path.isfile('generated/all.png'):
            m.plot_stars_and_constellations()
        context.bot.send_photo(chat_id, open('generated/all.png', 'rb'))
    except Exception as e:
        print('Error:', e)


def ver_constelacion(update, context):
    try:
        chat_id = update.callback_query.message.chat.id
        query = update.callback_query
        query.edit_message_text(text="¡Genial! Ahora necesito que me indiques cuál constelación"
                                     " deseas que te muestre %s:" % u'\U0001F914')
        update.callback_query.message.reply_text(text=constellation_menu_message(),
                                                 reply_markup=constellation_menu_keyboard())
    except Exception as e:
        print('Error:', e)


def cargar_constelacion(update, context):
    try:
        query = update.callback_query
        chat_id = query.message.chat.id
        constellation = query.data.upper()
        query.edit_message_text(text="¡Excelente! has seleccionado %s" % query.data)
        path = 'generated/%s.png' % constellation
        if not os.path.isfile(path):
            m.plot_stars_and_constellation(constellation)
        context.bot.send_photo(chat_id, open(path, 'rb'))
    except Exception as e:
        print('Error:', e)

