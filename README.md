# Using the BME680 sensor in a Raspberry Pi Zero connected to Microsoft Azure

This is a sample of using the Bosch BME680 sensor connected to a Raspberry Pi Zero and uploading/processing data in Azure. I'm using Adafruit's breakout (https://www.adafruit.com/product/3660) and using it to gather information including temperature, humidity and air quality.

*Note: This project is Work in Progress as of 23/01/2020. I'm actively working on it and will be adding daily.*

**To-add: Add photo of it with the connections**

## Note on reading data from sensor

Bosch has a library (compiled C) to handle their BME680 sensor, including proprietary code to calculate the Interior Air Quality (IAQ) score adjusting for humidity/pressure. This led me to decide to not use either Adafruit's (https://github.com/adafruit/Adafruit_BME680) or Pimoroni's (https://github.com/pimoroni/bme680-python/) Python Libraries. What Bosch's code does exactly is not clear because the code is closed. You can also simply use either of the above libraries with the Adafruit breakout, both work.

## Base setup instructions (if you're starting from scratch)

Start by following these instructions to set up the Zero: [Basic Device Setup](DeviceSetup.md) . If you already have one running, just remember to enable I2C. After this, you'll need to install some aditional libraries in the device, related either to the BME680 sensor or to Azure. To do this, follow the steps here: [Libraries setup](BME680Setup.md) . When you finish these two, you'll have a C application installed that prints out the sensor's readings, and all the required dependencies for what follows.

## Get sensor readings and push them to Azure

After the setup is done, you'll need to make make changes to make sure that:
- the readings are captured in a format simple to process in Azure (I picked CSV, JSON would be another good option)
- have code to send the readings to Azure IoT Hub

## Process the incoming data in Azure

And finally, what I'm doing in Azure, of course :)
