import csv
import datetime
import time

def log_data(irradiance, temperature, power_output):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('solar_data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, irradiance, temperature, power_output])

while True:
    irradiance = int(input("Enter the irradiance: "))
    temperature = int(input("Enter the temperature: "))
    power_output = int(input("Enter the power output: "))
    log_data(irradiance, temperature, power_output)
    time.sleep(2)