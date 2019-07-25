# BME680 MicroPython Driver

## Introduction

MicroPython driver for BME680 environmental sensor. This is a port of Adafruit's CircuitPython driver, modified to work with MicroPython. Only I2C functionality has been ported. It has been tested with a Lolin D1 mini (ESP8266) and a Lolin D32 (ESP32).

## Usage Example

```python
import time
from machine import I2C, Pin
import ubme680

# Create I2C object and pass to library object
i2c = I2C(-1, scl=Pin(22), sda=Pin(21), freq=100000)
bme680 = ubme680.uBME680_I2C(i2c, debug=False)

# change this to match the location's pressure (hPa) at sea level
bme680.sea_level_pressure = 1013.25

while True:
    print("\nTemperature: %0.1f C" % bme680.temperature)
    print("Gas: %d ohm" % bme680.gas)
    print("Humidity: %0.1f %%" % bme680.humidity)
    print("Pressure: %0.3f hPa" % bme680.pressure)
    print("Altitude = %0.2f meters" % bme680.altitude)

    time.sleep(2)
```
