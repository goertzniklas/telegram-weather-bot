from telegram.ext import Updater
from telegram.ext import CommandHandler, CallbackQueryHandler, MessageHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import BME280
from SI1145 import SI1145
si1145 = SI1145()

updater = Updater(token='859692484:AAHJiQ3FnI-G6NHHoz2KUPIIzUyJxVRk1qg', use_context=True)
dispatcher = updater.dispatcher

# bot listeners
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Hallo {} ðŸ‘‹'.format(update.message.from_user.first_name))
    context.bot.send_message(chat_id=update.effective_chat.id, text=selection_message(), reply_markup=selection_keyboard())

def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=overview_message())

def summary(update, context):
    getTemperature(update, context)
    getHumidity(update, context)
    getPressure(update, context)
    getUltraviolet(update, context)
    getIlluminance(update, context)
    getInfrared(update, context)


# bot messages
def selection_message():
    return 'Was mÃ¶chtest du Ã¼ber das aktuelle Wetter wissen? ðŸŒ¤'

def overview_message():
    return 'Telegram-Weather-Bot ðŸŒ¤â›ˆâ˜€ \n Ich kann dich mit den folgenden Kommandos unterstÃ¼tzen: \n\n â–ª /start \n Eine Gesamtansicht bekommst du mit: \n â–ª /summary \n A summary of your current weather. \n\n For a description of the Bot visit:\n https://google.com/'


# buttons
def getTemperature(update, context):
    temperature = BME280.readTemperature()    
    context.bot.send_message(chat_id=update.effective_chat.id, text='Die aktuelle Temepratur liegt %f Â°C' %temperature )   

def getHumidity(update, context):
    humidity = BME280.readHumidity()
    context.bot.send_message(chat_id=update.effective_chat.id, text='Die Luftfeuchte liegt bei %f Prozent' %humidity )

def getPressure(update, context):
    pressure = BME280.readPressure()
    context.bot.send_message(chat_id=update.effective_chat.id, text='Der Luftdruck liegt bei %f hPa' %pressure )

def getUltraviolet(update, context):
    ultraviolet = si1145.readUV()
    context.bot.send_message(chat_id=update.effective_chat.id, text='Die WellenlÃ¤nge der elektromagnetischen Strahlung liegt bei %f nm' %ultraviolet )

def getIlluminance(update, context):
    illuminance = si1145.readVisible()
    context.bot.send_message(chat_id=update.effective_chat.id, text='Die LichtstÃ¤rke betrÃ¤gt %f lx' %illuminance )

def getInfrared(update, context):
    infrared = si1145.readIR()
    context.bot.send_message(chat_id=update.effective_chat.id, text='Die UV-Strahlung liegt bei %f nm' %infrared)


# keyboard
def selection_keyboard():
    keyboard = [
        [InlineKeyboardButton('Temperatur', callback_data='temperature')],
        [InlineKeyboardButton('Luftfeuchtigkeit', callback_data='humidity')],
        [InlineKeyboardButton('Luftdruck', callback_data='pressure')],
        [InlineKeyboardButton('UV-Strahlung', callback_data='ultraviolet')],
        [InlineKeyboardButton('BeleuchtungsstÃ¤rke', callback_data='illuminance')],
        [InlineKeyboardButton('IR-Strahlung', callback_data='infrared')]
    ]
    return InlineKeyboardMarkup(keyboard)


# updater
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('summary', summary))

updater.dispatcher.add_handler(CallbackQueryHandler(getTemperature, pattern='temperature'))
updater.dispatcher.add_handler(CallbackQueryHandler(getHumidity, pattern='humidity'))
updater.dispatcher.add_handler(CallbackQueryHandler(getPressure, pattern='pressure'))
updater.dispatcher.add_handler(CallbackQueryHandler(getUltraviolet, pattern='ultraviolet'))
updater.dispatcher.add_handler(CallbackQueryHandler(getIlluminance, pattern='illuminance'))
updater.dispatcher.add_handler(CallbackQueryHandler(getInfrared, pattern='infrared'))

updater.start_polling()