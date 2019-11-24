from telegram.ext import Updater
from telegram.ext import CommandHandler, CallbackQueryHandler, MessageHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
updater = Updater(token='TOKEN', use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
  context.bot.send_message(chat_id=update.effective_chat.id, text='Hello {} 👋'.format(update.message.from_user.first_name))
  context.bot.send_message(chat_id=update.effective_chat.id, text=selection_message(),
                            reply_markup=selection_keyboard())

def help(update, context):
  context.bot.send_message(chat_id=update.effective_chat.id, text=overview_message())


def handle_message(update, context):
    text = update.message.text
    if text == 'hello':
        context.bot.send_message(chat_id=update.effective_chat.id, text='Hallo {} 👋'.format(update.message.from_user.first_name))

def selection(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=selection_message(),
                        reply_markup=first_menu())

class Plant(object):
    temperature = round(26.76543, 2)
    summer = ""
    summer_icon = ""
    winter = ""
    winter_icon = ""
    if temperature >= 25:
        summer = "Oh and please don't forget to put your suncream on 😎🏝"
        summer_icon = "☀"
    elif temperature < 20:
        winter = "Jacket, scarf and thick socks not that you catch a cold 🙏"
        winter_icon = "🌨"


def temperature_button(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='The current temperature is {p.temperature}°C {p.summer_icon}{p.winter_icon}'.format(p=Plant()))
    context.bot.send_message(chat_id=update.effective_chat.id, text='{p.summer}{p.winter}'.format(p=Plant()))

def humidity_button(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Die Luftfeuchte liegt bei 84%')

def pressure_button(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Der Luftdruck liegt bei 1000 hPa')

def infrared_button(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Die Wellenlänge der elektromagnetischen Strahlung liegt bei 800nm')

def illuminance_button(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Die Lichtstärke beträgt 19.000 lx')

def ultraviolet_button(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Die UV-Strahlung liegt bei 215 nm')

def selection_keyboard():
  keyboard = [[InlineKeyboardButton('Temperatur', callback_data='temperature')],
              [InlineKeyboardButton('Luftfeuchtigkeit', callback_data='humidity')],
              [InlineKeyboardButton('Luftdruck', callback_data='pressure')],
              [InlineKeyboardButton('IR-Strahlung', callback_data='infrared')],
              [InlineKeyboardButton('Beleuchtungsstärke', callback_data='illuminance')],
              [InlineKeyboardButton('UV-Strahlung', callback_data='ultraviolet')]]

  return InlineKeyboardMarkup(keyboard)

def selection_message():
  return 'What do you want to know about todays weather? 🌤'

def overview_message():
    return 'Telegram-Weather-Bot 🌤⛈☀\nI can assist you with the following commands:\n\n▪ /start\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tAn overview of all callable values\n▪ /weather\t\t\t\t\t\t\t\tA summary of your current weather.\n\nFor a description of the Bot visit:\nhttps://google.com'

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(MessageHandler(filters=Filters.text, callback=handle_message))
updater.dispatcher.add_handler(CallbackQueryHandler(temperature_button, pattern='temperature'))
updater.dispatcher.add_handler(CallbackQueryHandler(humidity_button, pattern='humidity'))
updater.dispatcher.add_handler(CallbackQueryHandler(pressure_button, pattern='pressure'))
updater.dispatcher.add_handler(CallbackQueryHandler(infrared_button, pattern='infrared'))
updater.dispatcher.add_handler(CallbackQueryHandler(illuminance_button, pattern='illuminance'))
updater.dispatcher.add_handler(CallbackQueryHandler(ultraviolet_button, pattern='ultraviolet'))

updater.start_polling()
