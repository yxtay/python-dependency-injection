import datetime
import json


class DataSource:
    def read(self, **kwargs):
        temperatures_by_hour = {}
        with open(kwargs["file_name"]) as file:
            json_data = json.load(file)["hourly"]
            for row in json_data:
                hour = datetime.datetime.fromtimestamp(row["dt"]).isoformat()
                temperature = float(row["temp"])
                temperatures_by_hour[hour] = temperature

        return temperatures_by_hour
