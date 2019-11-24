from SI1145 import SI1145
import bme280
si1145 = SI1145()

print(bme280.readTemperature())
print(bme280.readPressure())
print(bme280.readHumidity())

print(si1145.readUV())
print(si1145.readVisible())
print(si1145.readIR())
