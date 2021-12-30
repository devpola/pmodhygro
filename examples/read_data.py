from pmodhygro import PmodHygro

# Create i2c bus
sensor = PmodHygro()
sensor.begin_i2c()

# Read data from Pmod HYGRO 
temp = sensor.get_temperature()
temp_f = sensor.get_temperature_f()
hum = sensor.get_humidity()

# Print data
print("temp : ", temp)
print("temp_f : ", temp_f)
print("hum : ", hum)