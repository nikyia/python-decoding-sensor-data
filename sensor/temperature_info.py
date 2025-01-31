# Import libraries
from house_info import HouseInfo
from datetime import datetime
from datetime import date

# Create TemeratureData Class

class TemperatureData(HouseInfo):
    # Create private method convert data to convert temperature data
    def _convert_data(self,data):
        recs = []
        # Loop over data and convert it to integers
        for rec in data:
            recs.append(int(rec, base=10))       
        return recs

    # Create new get data by area method
    def get_data_by_area(self, rec_area=0):
        recs = super().get_data_by_area("temperature",rec_area)
        return self._convert_data(recs)

    # Create new get data by date method
    def get_data_by_date(self, rec_date=date.today()):
        recs = super().get_data_by_date("temperature",rec_date)

        return self._convert_data(recs)