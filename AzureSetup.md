# Provision required Azure services

## Provision IoT Hub/Device in Azure

The following operations can all be done from the Azure Portal. I'm showing the commands using the Azure CLI which I find more convenient.

1. Create a resource group with the command: `az group create -l northeurope -g RES_GROUP_NAME`
2. Crete an IoT Hub with the command: `az iot hub create -l northeurope -g RES_GROUP_NAME --sku B1 -n IOTHUB_NAME`

    - This is a Basic 1 tier, which means that features like cloud-to-device messaging won't be available. If you want to use them, provision an S1 instead.

3. Create an IoT Device with the command `az iot hub device-identity create -g RES_GROUP_NAME -n IOTHUB_NAME --device-id NAME_YOUR_DEVICE`. This creates an IoT device configuration on the IoT Hub, which you'll use to push readings to it. By default the authentication method is Shared Access Key.

4. Copy the IoT device's Connection String, with the command: `az iot hub device-identity show-connection-string -g RES_GROUP_NAME -n IOTHUB_NAME --device-id NAME_YOUR_DEVICE`. Copy the string starting with "Hostname=..." to a text editor for later use.