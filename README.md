# Using the BME680 sensor in a Raspberry Pi Zero connected to Microsoft Azure

Sample of using the Bosch BME680 sensor connected to a Raspberry Pi Zero and uploading/processing data in Azure. I'm using Adafruit's breakout (https://www.adafruit.com/product/3660).

Bosch has a library (compiled C) to handle this sensor, including proprietary code to calculate the Interior Air Quality (IAQ) score adjusting for humidity/pressure, so I decided to not use either Adafruit's (https://github.com/adafruit/Adafruit_BME680) or Pimoroni's (https://github.com/pimoroni/bme680-python/) Python Libraries. What Bosch's code does exactly is not clear because the code is closed. You can also simply use either of the above libraries with the Adafruit breakout, both work.


**Note**: This project is Work in Progress as of 22/01/2020. I'm actively working on it and will be adding daily.

[Basic Device Setup](DeviceSetup.md)

[Libraries setup](BME680Setup.md)

