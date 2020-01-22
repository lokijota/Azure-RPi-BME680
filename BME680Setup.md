# Install libraries to interact with the BME680 sensor

## Bosh BSEC libraries setup

1. Run `git clone https://github.com/alexh-name/bsec_bme680_linux.git`. This is a great repo that includes C code to call Bosh's libraries. These are close source and include code to calculate an IAQ score (Interior Air Quality) that depends on other atmospheric factors. Unfortunatelly not public how this calculation is done. I'll be changing some of the code of this repo to upload readings to Azure.
2. Follow the setup instructions on (https://github.com/alexh-name/bsec_bme680_linux). Remember to `chmod +x make.sh` for it to be executable.

**Add here**: Download of BSEC and copy into RPI / PIMIDORI / Adafruit

Also -- for another page, not here:
- secondary I2C in my case
- change the checkpointing interval
- every 3 seconds
- change 5ºC to 4ºC ??

## Install Azure IoTHub Client SDK

https://pypi.org/project/azure-iot-device/ and https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-devguide-sdks
