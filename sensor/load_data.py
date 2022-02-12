import os
import glob
import csv

def load_sensor_data():
    """Opens Sensor Data CSV files in the datasets folder and returns the sensor data as a list

    Parameters:

    Returns:
        list: a list of sensor data items from the sensor data stored in the datasets folder

    Raises: 
    """
    sensor_data = []
    sensor_files = glob.glob(os.path.join(os.getcwd(), "datasets", "*.csv"))
    for sensor_file in sensor_files:
        with open(sensor_file) as data_file:
            data_reader = csv.DictReader(data_file, delimiter=',')
            for row in data_reader:
                sensor_data.append(row)
    return sensor_data


