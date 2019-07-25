import time
from machine import I2C, Pin
import ubme680

# Create library object using our Bus I2C port
i2c = I2C(-1, scl=Pin(22), sda=Pin(21), freq=100000)
bme680 = ubme680.uBME680_I2C(i2c, debug=False)

# change this to match the location's pressure (hPa) at sea level
bme680.sea_level_pressure = 1013.25

print('')

print('| Temperature |  Humidity   |  Pressure   | Gas Resistance | Altitude |')
print('| (C)         |  (%RH)      |  (hPa)      | (Ohms)         | (m)      |')
print('|-------------|-------------|-------------|----------------|----------|')
while True:
    output = '| {0:>11.2f} | {1:>11.2f} | {2:>11.2f} | {3:>14.d} | {4:>8.2f} |'.format(
                bme680.temperature,
                bme680.humidity,
                bme680.pressure,
                bme680.gas,
                bme680.altitude)
    print(' '*71, end='\r') # clear previous printout
    print(output, end='\r')
    
    time.sleep(1)
