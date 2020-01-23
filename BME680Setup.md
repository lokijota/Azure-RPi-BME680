# Install libraries to interact with the BME680 sensor

## Bosh BSEC libraries setup

1. Run `git clone https://github.com/alexh-name/bsec_bme680_linux.git`. This is a great repo that includes C code to call Bosh's libraries. These are close source and include code to calculate an IAQ score (Interior Air Quality) that depends on other atmospheric factors. Unfortunatelly not public how this calculation is done. I'll be changing some of the code of this repo to upload readings to Azure.
2. Follow the setup instructions on (https://github.com/alexh-name/bsec_bme680_linux).
- To copy Bosh's BSEC library to the Pi, if you're using an headless install, use something like `scp bsec_1-4-7-4_generic_release.zip pi@192.168.1.123:/home/pi/` (replacing the IP address of your Zero)
- Remember to create a path folder `src` inside `bsec_bme680_linux/`
- Also remember to `chmod +x make.sh` for it to be executable.

3. Install I2C's tools if you haven't already. You'll need them to check if you have the I2C connection correctly set up: `sudo apt-get install i2c-tools`
4. Run `sudo i2cdetect -y 1`. You should see something like this:

```
pi@rpi0:~/bsec_bme680_linux $ sudo i2cdetect -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
70: -- -- -- -- -- -- -- 77
```

- If you don't see this, you may want to check you've enabled I2C in `raspi-config`, or check the connections from your Zero and the sensor.

5. In what I've read online, you can have either 76 or 77 in the previous step. If you have 77 like me, you'll need to edit the file `bsec_bme680.c` file and change the line `int i2c_address = BME680_I2C_ADDR_PRIMARY;` to `int i2c_address = BME680_I2C_ADDR_SECONDARY;`. Then do another compilation by calling `./make.sh` again.

6. Run the resulting executable with `./bsec_bme680`.


banana

**Add here**: PIMIDORI / Adafruit

Also:
**Add here**: Download of BSEC and copy into RPI / PIMIDORI / Adafruit

Also -- for another page, not here:
- secondary I2C in my case
- change the checkpointing interval
- every 3 seconds
- change 5ºC to 4ºC ??

## Install Azure IoTHub Client SDK

https://pypi.org/project/azure-iot-device/ and https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-devguide-sdks
