# Import libraries
import os
import glob
import csv

# Create functions to Parse the Data

def load_sensor_data():
    sensor_data = []
    
    # Sensor Data File Management
    sensor_files = glob.glob(os.path.join(os.getcwd(), 'datasets', '*.csv'))
    
    # Read Data Files
    for sensor_file in sensor_files:
        with open(sensor_file) as data_file:
            data_reader = csv.DictReader(data_file, delimiter=',')
            # Load Data Records
            for row in data_reader:
                sensor_data.append(row)

    return sensor_data
