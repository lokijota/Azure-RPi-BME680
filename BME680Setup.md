# Install libraries to interact with the BME680 sensor and call into Azure

## Install BOSH BSEC's wrapper project (and BSEC libraries, of course)

1. Run `git clone https://github.com/alexh-name/bsec_bme680_linux.git`. This is a great/simple repo that includes C code to wrap Bosh's libraries. I'll be changing some of the code of this repo to upload readings to Azure.

    - This will create a folder `bsec_bme680_linux`, with the two most important files there being `bsec_bme680.c` which is the code that reads from the sensor via the BSEC library, and `make.sh` which compiles this code to create the executable.
    - `cd` into the `bsec_bme680_linux` folder for the following steps.

2. Follow the setup instructions on here: https://github.com/alexh-name/bsec_bme680_linux. Some notes:
    - To copy Bosh's BSEC library's Zip to the Zero, if you're using an headless install, use something like `scp bsec_1-4-7-4_generic_release.zip pi@192.168.1.123:/home/pi/` (replacing the IP address of your Zero). `scp` is pre-installed on Windows 10 now, like `ssh`, and stands for "Securely Copy Files".
    - Remember to create a folder `src` inside `bsec_bme680_linux/` on the Zero
    - Also remember to `chmod +x make.sh` for it to be executable.

3. Install I2C's tools if you haven't already. You'll need them to check if you have the I2C connection correctly set up: `sudo apt-get install i2c-tools -y`
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

- If you don't see this, you may want to check you've enabled I2C in `raspi-config`, or check the physical connections from your Zero to the sensor.

5. In what I've read online, you can have either 76 or 77 in the previous step. If you have 77 like me, you'll need to edit the file `bsec_bme680.c` file and change the line `int i2c_address = BME680_I2C_ADDR_PRIMARY;` to `int i2c_address = BME680_I2C_ADDR_SECONDARY;`. Then do another compilation by calling `./make.sh` again.

6. Run the resulting executable with `./bsec_bme680`.

7. By now you should be getting readings printed out every few seconds, such as:

```
2020-01-23 21:22:45,[IAQ (0)]: 25.00,[T degC]: 16.60,[H %rH]: 55.10,[P hPa]: 965.48,[G Ohms]: 4270,[S]: 0,[eCO2 ppm]: 500.000000000000000,[bVOCe ppm]: 0.4999999403953552246093750
```

## Install Azure IoTHub Client SDK for Python

This is a Python client library to talk with Azure IoT Hub. There's also a C version available (https://github.com/Azure/azure-iot-sdk-c), but while I got it to work, I don't know enough about C anymore to know how to add the references to a new C application, so after spending some hours around CMake/Makefiles, I gave up and decided to go for Python SDK.

1. Run `pip3 install azure-iot-device` (you should have installed pip3 in the [previous setup step](DeviceSetup.md))

The SDK's documentation is here: https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-devguide-sdks (scroll down to the "Azure IoT Hub device SDK for Python" section).

And that's it. You now have a working Zero, the sensor is working, and all the requirements are installed. The next step includes the remaining steps to [get the Zero to do readings in an interesting format and then upload them to Azure](DeviceUploadData.md).


## Other links

- Bosch forum - Explanation on static IAQ, breath VOC and CO2 equivalent - https://community.bosch-sensortec.com/t5/MEMS-sensors-forum/Explanation-on-static-IAQ-breath-VOC-and-CO2-equivalent/td-p/7413

    - Static IAQ: The main difference between IAQ and static IAQ (sIAQ) relies in the scaling factor calculated based on the recent sensor history. The sIAQ output has been optimized for stationary applications (e.g. fixed indoor devices) whereas the IAQ output is ideal for mobile application (e.g. carry-on devices).
    - bVOCeq estimate: The breath VOC equivalent output (bVOCeq) estimates the total VOC concentration [ppm] in the environment. It is calculated based on the sIAQ output and derived from lab tests.
    - CO2eq estimate: Estimates a CO2-equivalent (CO2eq) concentration [ppm] in the environment. It is also calculated based on the sIAQ output and derived from VOC measurements and correlation from field studies.
    - Since bVOCeq and CO2eq are based on the sIAQ output, they are expected to perform optimally in stationnary applications where the main source of VOCs in the environment comes from human activity (e.g. in a bedroom).


- Bosch forum - BME680: IAQ accuracy definition - https://community.bosch-sensortec.com/t5/MEMS-sensors-forum/BME680-IAQ-accuracy-definition/td-p/5920

    - IAQ Accuracy=0 could either mean: BSEC was just started, and the sensor is stabilizing (this lasts normally 5min in LP mode or 20min in ULP mode),
there was a timing violation (i.e. BSEC was called too early or too late), which should be indicated by a warning/error flag by BSEC,
    - IAQ Accuracy=1 means the background history of BSEC is uncertain. This typically means the gas sensor data was too stable for BSEC to clearly define its references,
    - IAQ Accuracy=2 means BSEC found a new calibration data and is currently calibrating,
    - IAQ Accuracy=3 means BSEC calibrated successfully.

- BlueDot - Air Quality Measurement (IAQ) with the BME680 - https://www.bluedot.space/tutorials/air-quality-measurement-with-the-bme680/