# Setting up a Pi0 after old kingston microSD piffed

## Base setup

1. Flash the Raspian image intro the MicroSD Card (the BalenaEtcher is a good tool, but run it in Administrator mode)
2. Log in (pi/raspberry) and update the settings in `sudo raspi-config`, including:
    - set the hostname of the device
    - turn on Camera, SSH, SPI, I2C
    - configure the right keyboard
    - configure the WIFI
    - configure Boot to automatically log into the command line
    - change the password
    - when you're done, reboot for the wifi to take effect

3. After reboot you can start `sudo raspi-config` again and update the tool, in case new settings appear
4. Update the system by running  `sudo apt-get update` followed by `sudo apt-get upgrade -y`
5. Install pip3: `sudo apt-get install python3-pip -y`
6. Install Vim: `sudo apt-get install vim -y`
7. Install Git: `sudo apt-get install git -y`

## BSCE setup

1. Run `git clone https://github.com/alexh-name/bsec_bme680_linux.git`

