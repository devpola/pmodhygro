import smbus2
import time


class PmodHygro:
    """class that define procedures of Pmod HYGRO (relative humidity sensor with an integrated temperature sensor)"""

    
    # address variables
    I2C_ADDR = 0x40         # unique 7-bit address of Pmod HYGRO device on the I2C bus 
    TMP_REG = 0x00          # temperature register address
    HUM_REG = 0x01          # relative humidity register address
    CONFIG_REG = 0x02       # configuration register address


    def __init__(self):
        """initialize variables of sensor data"""
        self.temperature = 0.0
        self.humidity = 0.0
        self.i2cbus = None
    

    def begin_i2c(self):
        """create i2c bus & update configuration register"""
        self.i2cbus = smbus2.SMBus(1) # create a new I2C bus
        time.sleep(0.015)       # Wait 15ms
        self.i2cbus.write_word_data(PmodHygro.I2C_ADDR, PmodHygro.CONFIG_REG, 0x00)  # use non-sequential acquisition mode, all other config bits are default


    def get_temperature(self):
        """get data from temperature register & convert raw data to temperature(celcius)"""
        self.i2cbus.write_byte(PmodHygro.I2C_ADDR, PmodHygro.TMP_REG)    # write temperature register pointer to talk
        time.sleep(0.007)   # wait conversion time for temperature(at least 6.35ms at 14bit resolution)

        # read 2 byte from temperature register(2 byte)
        temp_raw_front = self.i2cbus.read_byte(PmodHygro.I2C_ADDR)
        temp_raw_rear = self.i2cbus.read_byte(PmodHygro.I2C_ADDR)
        temp_raw_front = temp_raw_front << 8
        temp_raw = temp_raw_front | temp_raw_rear

        # convert raw data of sensors(provided in reference manual)
        temp_raw /= 0x10000
        self.temperature = temp_raw * 165.0 - 40.0

        return self.temperature


    def get_humidity(self):
        """get data from humidity register & convert raw data to relative humidity(%)"""
        self.i2cbus.write_byte(PmodHygro.I2C_ADDR, PmodHygro.HUM_REG)    # write humidity register pointer to talk
        time.sleep(0.007)   # wait conversion time for humidity(at least 6.5ms at 14bit resolution)

        # read 2 byte from humidity register(2 byte)
        humidity_raw_front = self.i2cbus.read_byte(PmodHygro.I2C_ADDR)
        humidity_raw_rear = self.i2cbus.read_byte(PmodHygro.I2C_ADDR)
        humidity_raw_front = humidity_raw_front << 8
        humidity_raw = humidity_raw_front | humidity_raw_rear

        # convert raw data of sensors(provided in reference manual)
        humidity_raw /= 0x10000
        self.humidity = humidity_raw * 100.0

        return self.humidity


    def get_temperature_f(self):
        """return fahrenheit temperature (°F)"""
        if self.temperature:
            return self.temperature * 1.8 + 32;
        else:
            return get_temperature() * 1.8 + 32;
        
