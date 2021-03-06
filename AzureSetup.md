# Provision required Azure services

## Provision an Azure SQL Database

I created a server (which is a logical concept) called `bme680` and a database called `bme680db`. In the end I'm using a Standard S2 tier, with 50 DTUs and 250Gb of storage, which should be enough for over an year (at one reading every 3 seconds the database grows reasonably fast). Follow instructions here: https://docs.microsoft.com/en-us/azure/azure-sql/database/single-database-create-quickstart?tabs=azure-portal . You'll have to scale up if you're running complex queries on the data.

![](azure-sql-database.png)

## Provision IoT Hub/Device in Azure

The following operations can all be done from the Azure Portal. I'm showing the commands using the [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/?view=azure-cli-latest) which I find more convenient.

1. Create a resource group with the command: `az group create -l northeurope -g RES_GROUP_NAME`
2. Crete an IoT Hub with the command: `az iot hub create -l northeurope -g RES_GROUP_NAME --sku B1 -n IOTHUB_NAME`

    - This is a Basic 1 tier, which means that features like cloud-to-device messaging won't be available. If you want to use them, provision an S1 instead.

3. Create an IoT Device with the command `az iot hub device-identity create -g RES_GROUP_NAME -n IOTHUB_NAME --device-id NAME_YOUR_DEVICE`. This creates an IoT device configuration on the IoT Hub, which you'll use to push readings to it. By default the authentication method is Shared Access Key.

4. Copy the IoT device's Connection String, with the command: `az iot hub device-identity show-connection-string -g RES_GROUP_NAME -n IOTHUB_NAME --device-id NAME_YOUR_DEVICE`. Copy the string starting with "Hostname=..." to a text editor for later use.

5. You'll also need to create a consummer group, which I'm using in Stream Analytics. I named mine `bme680consumers`) (you can find this in the "Built-in endpoints" option in the IoT Hub's page, or create with the CLI - https://docs.microsoft.com/en-us/cli/azure/iot/hub/consumer-group?view=azure-cli-latest ).


**TBD** - If you have other sensors wired to your IoT Hub, you'll need to specify configurations so that your processing only happens with the BME680's readings.

## Links

These links can be informative if you want to know more: https://docs.microsoft.com/en-gb/learn/modules/remotely-monitor-devices-with-azure-iot-hub/2-create-iot-hub-device-id?pivots=csharp and https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-devguide-messages-read-builtin .
