from datetime import datetime, date

class HouseInfo():
    """

    Attributes:
        data: list
            a list of sensor data records

    Methods:
        get_data_by_area(field, rec_area = 0): 
            Returns the sensor data for the specified recording area and the specified field
    """
    def __init__(self, data):
        self.data = data

    def get_data_by_area(self, field, rec_area = 0):
        """Returns the sensor data for a record area and the specified field
        If the argument 'rec_area' is not passed then the value of the specified field
        for all records is returned. 
        If the argument 'rec_area' is passed then the value of the specified field 
        for records belonging to the rec_area are returned. 
        
        Parameters
        ----------
        field : str
            The field for which sensor data is required
        rec_Area : int
            The recording area for which sensor data is required
        """
        field_data = []
        for record in self.data:
            if rec_area == 0:
                field_data.append(record[field])
            elif rec_area == int(record['area']):
                field_data.append(record[field])
        return field_data

    def get_data_by_date(self, field, rec_date = date.today()):
        """Returns the sensor data for a record date and the specified field
        If the argument 'rec_date' is not passed then the value of the specified field
        for todays records are returned. 
        If the argument 'rec_date' is passed then the value of the specified field 
        for records belonging to the rec_date are returned. 
        
        Parameters
        ----------
        field : str
            The field for which sensor data is required
        rec_date : date
            The date for which sensor data is required
        """
        field_data = []
        for record in self.data:
            if rec_date.strftime('%m/%d/%y') == record['date']: 
                field_data.append(record[field])

        return field_data
