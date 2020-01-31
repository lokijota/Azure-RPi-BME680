# Get sensor readings in CSV format and upload to Azure

## Change C code that does the sensor readings to write CSV files

The original code from https://github.com/alexh-name/bsec_bme680_linux prints out sensor the readings to stdout (screen). Replace the file from that repo with my version [here](https://github.com/lokijota/Azure-RPi-BME680/blob/master/bsec_bme680.c). The changes I made were:

- modified the `output_ready()` function to generate files named YYYYNNDD-HHMMSS.csv in a `data` subfolder. Remeber to create this folder;
- at the top a `temp_offset` constant is defined with value `5.0f`. This value is being added to the temperature measurements (which are in Celcius), to compensate for the temperature of the Raspberry/Power supply/etc. I changed this value to `4.0f` as I believe I have better isolation -- do edit to your own situation;
- also at the head of the file there's an `int` variable valled `i2c_address` declared, with default value `BME680_I2C_ADDR_PRIMARY` (corresponding to I2C address 76). In my case I have address 77, so needed to change this to `BME680_I2C_ADDR_SECONDARY`;
- changed call `bsec_iot_loop` near the end to checkpoint the internal state of the sensor every 4 hours (i.e., changed the last parameter from `10000` to `4800`).

After this, compile the file again by calling `./make.sh` as before. Remember to create a `data` folder as a subfolder from where you'll be running the compiled `bsec_bme680`, or you'll a friendly `Segmentation fault` when you run it.

Now type `./bsec_bme680 &` to run the application in the background. If you change into the data folder, you'll start seeing the csv files being generated every 3 seconds.

## Upload the CSV files to Azure

I decided to separate the capture of the sensor readings from the uploading to Azure for a couple of reasons:
- If there's any networking issue, you won't run the risk of losing readings. Additionally, while the time to push a reading to the cloud is non-deterministic, writing to a file is much more so, so you can keep a predictable reading every 3 seconds;
- It's much simpler to install/use the IoT Hub Client SDK for Python than it is to figure out how the CMake-based compilation process of the IoT Hub Client SDK for C works. Hence, I'll be using Python for the upload.

The steps to follow are:

1. Create a file on the Pi called `scoop_up_data.py` with the contents you find [here](https://github.com/lokijota/Azure-RPi-BME680/blob/master/scoop_up_data.py). This code uses the  version 1.4.4 of the Azure IotHub Device Client SDK (which you installed [previously](BME680Setup.md)).
2. Edit the file to change the value of the `iothub_connstring` variable. This is a string looking like `"HostName=NAME_OF_YOUR_IOTHUB.azure-devices.net;DeviceId=NAME_OF_YOUR_DEVICE_IN_THE_IOTHUB;SharedAccessKey=LOTS_OF_ALFANUM_CHARACTERS"` which you can get from the Azure portal.
3. To do test run, call `python3 scoop_up_data.py ./data/`. This will upload all your already captured CSV files to the Azure IoTHub, in cronological order, and print out something like:

```
pi@rpi0:~/bsec_bme680_linux $ python3 scoop_up_data.py ./data/
Starting iothub client
Reading files from /home/pi/bsec_bme680_linux/data:
1 - /home/pi/bsec_bme680_linux/data/20200131-233324.csv
2 - /home/pi/bsec_bme680_linux/data/20200131-233327.csv
...
378 - /home/pi/bsec_bme680_linux/data/20200131-235215.csv
Files uploaded: 378

```

4. The files in the `data` folder are renamed, with an `uploaded_` prefix added. E.g., `20200131-235215.csv` becomes `uploaded_20200131-235215.csv`. You'll need to clear up these files later.
5. Now that this process has been tested, you need to run the previous command on a schedule with a cron job. To do this, run `crontab -e`, pick a text editor if Linux asks you to (nano may be the simplest one), and add the following at the end of the file:

`* * * * * /usr/bin/python3 /home/pi/bsec_bme680_linux/scoop_up_data.py /home/pi/bsec_bme680_linux/data/`

When you save and exit, the specified command will be executed every minute, and upload the readings (typically 20 at a time, considering they are recorded every 3 seconds).

## TBD

**TBD** clear up the uploaded files.

**TBD** - how to set up your Azure IotHub -- create it and an IoT Device. Add a new instructions step. Maybe link to this: https://docs.microsoft.com/en-gb/learn/modules/remotely-monitor-devices-with-azure-iot-hub/2-create-iot-hub-device-id?pivots=csharp

**TBD** avoid race condition as per here: https://www.cyberciti.biz/faq/how-to-run-cron-job-every-minute-on-linuxunix/
