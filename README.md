# telegram-weather-bot
A telegram bot which tells you the weather using a raspberry pi 

## Links
[https://github.com/python-telegram-bot](https://github.com/python-telegram-bot)

[https://github.com/THP-JOE/Python_SI1145](https://github.com/THP-JOE/Python_SI1145)

[https://github.com/adafruit/Adafruit_Python_BME280/blob/master/Adafruit_BME280.py](https://github.com/adafruit/Adafruit_Python_BME280/blob/master/Adafruit_BME280.py)

## Installation
1. Download the repo.
2. Please follow the [installation](https://github.com/python-telegram-bot/python-telegram-bot) guide of the telegram-api first.
3. Make sure that i2c and gpio is enabled on your device.
4. Insert your Telegram TOKEN inside the bot.py. 
5. Connect your sensors and check them with:

```i2cdetect -y 1```

6. Install the following python library:

```pip3 install Adafruit-GPIO```




