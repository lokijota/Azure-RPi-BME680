# Setting up a Raspberry Pi Zero 0 from scratch

Follow these instructions to install a Zero from scratch. This is pretty standard, I'm including in part so that I don't forget it myself in case I want to repeat it.

1. Flash the [Raspian image](https://www.raspberrypi.org/downloads/raspbian/) into a MicroSD Card (the [Balena Etcher](https://www.balena.io/etcher/) is a good tool, remember to run it -on Windows - in Administrator mode)
2. Log in (pi/raspberry as the default credentiaals) and update the settings in `sudo raspi-config`, including:
    - set the hostname of the device
    - turn on Camera (in my case), SSH, SPI, I2C
    - configure the right keyboard locale if needed
    - configure the Wifi
    - configure Boot to automatically log into the command line
    - change the password
    - when you're done, reboot for the Wifi and remaining configurations to take effect

3. After the reboot you can start `sudo raspi-config` again and update the tool, in case new settings appear
4. Back in the command line, update applications by running  `sudo apt-get update` followed by `sudo apt-get upgrade -y`. This will probably take a while on the Zero.
5. Install pip3: `sudo apt-get install python3-pip -y` (to later install Python3 packages)
6. Install Vim: `sudo apt-get install vim -y` (because I prefer Vim to Vi/Nano/Emacs when editing text files)
7. Install Git: `sudo apt-get install git -y` (to get files from this and other repos)

That's it. Continue with the setup of [BME680 and Azure libraries](BME680Setup.md).
