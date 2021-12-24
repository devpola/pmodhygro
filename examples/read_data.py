from pmodhygro import HygroI2C

# Create i2c bus
pmod = HygroI2C()
pmod.begin_i2c()

# Read data from Pmod HYGRO 
temp = pmod.get_temperature()
temp_f = pmod.get_temperature_f()
hum = pmod.get_humidity()

# Print data
print("temp : ", temp)
print("temp_f : ", temp_f)
print("hum : ", hum)