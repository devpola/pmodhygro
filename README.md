# pmodhygro
pmodhygro is python library to read PmodHYGRO that is relative humidity sensor with integrated temperature sensor on a Raspberry Pi

-> Reference page of PmodHygro sensor : https://digilent.com/reference/pmod/pmodhygro/start?redirect=1

## Installing
### Install with pip
Use pip to install from PyPI.

Python 2:
````sh
sudo pip install pmodhygro
````
Python 3:
````sh
sudo pip3 install pmodhygro
````

### Compile and install from the repository
Download library for ZIP file from GitHub, unzipping the archive, and execute:

Python 2:
````sh
cd pmodhygro
sudo python setup.py install
````

Python 3:
````sh
cd pmodhygro
sudo python3 setup.py install
````
You may also git clone the repository:

git clone https://github.com/devpola/pmodhygro.git


## Usage
````python
from pmodhygro import PmodHygro

# Create i2c bus
sensor = PmodHygro()
sensor.begin_i2c()

# Read data from Pmod HYGRO 
temp = sensor.get_temperature()
temp_f = sensor.get_temperature_f()
hum = sensor.get_humidity()
````
You have to run program with 'sudo' command for avoiding permission error


## Check list before using library
### Check for I2C
Raspbian:
1. Using “Raspi-config” on Command Line
  ````sh
  sudo raspi-config
  ````
2. Enable I2C Interface

Ubuntu(20.04):
1. Open '/boot/firmware/syscfg.txt' file
2. Check if there are contents below. If not, add it.
  ````sh
  dtparam=i2c_arm=on, dtparam=spi=on
  ````


### Check the connection 
* Check port sensor is connected using command below.
  ````sh
  ls /dev/*i2c*
  ````
  1. You can get **/dev/i2c-0** or **/dev/i2c-1**
  
      * In case of Raspberry Pi B model, there are two i2c ports, 0 and 1.
  2. Remember whether the port number is 0 or 1


* Check device address is 0x40
  1. Install **i2c-tools** package for checking connected devices to i2c interface
      ````sh
      sudo apt-get install i2c-tools
      ````
  
  
  2. Check device address at the port is 0x40 using command below.
    ````sh
    sudo i2cdetect -y 0 (or 1)
    ````
    