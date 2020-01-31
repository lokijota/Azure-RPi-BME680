import argparse
from azure.iot.device import IoTHubDeviceClient
import time
import os, fnmatch
from datetime import datetime

# specify/parse input parameters
parser = argparse.ArgumentParser()
parser.add_argument('dataFolder', help='folder containg CSV files to upload to Azure IoT hub')
res = parser.parse_args()

# prepare for upload
print("Starting iothub client")
iothub_connstring = "HostName=..."
client =  IoTHubDeviceClient.create_from_connection_string(iothub_connstring)
client.connect()

print("Reading files from " + os.path.abspath(res.dataFolder) + ":")

#get a list of files from the folder, sorted alfabetically
listOfFiles = sorted(os.listdir(res.dataFolder))
pattern = "2*.csv" # must start with a '2' of year 2000, otherwise uploaded_ files are re-sent
count = 0

for entry in listOfFiles:
    if fnmatch.fnmatch(entry, pattern):

        # read the file's contents
        filename = os.path.join( os.path.abspath(res.dataFolder), entry)
        file = open(filename, 'r')
        contents = file.read()

        # upload to azure IoT Hub
        client.send_message(contents)

        #  close and delete file
        file.close()

        os.rename(filename, os.path.join(os.path.abspath(res.dataFolder), "uploaded_" + entry))
        count = count + 1

        print (str(count) + " - " + filename)


print("Files uploaded: " + str(count))

client.disconnect()
# meter um try-catch!