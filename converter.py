import json
import pandas
import requests


class GeoJsonConverter(object):
    def __init__(self):
        pass

    def get_source():
        pass

    def from_json(self, filename=None):
        if filename=None:
            filename=self.filename
        else:
            filename = ''
        if filename:
            with open(filename, 'r') as json_obj:
                json_data = json.load(json_obj)
            return json_data

    def from_csv(self, filename):
        if filename=None:
            filename=self.filename
        else:
            filename = ''
        if filename:
            df = pd.read_csv(filename)
            data = df.to_dict('r')
            return data


    def to_geojson(self, data):
        geojson = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [d["longitude"], d["latitude"]],
                },
                "properties": d,
            } for d in data]
        }
        return geojson


    def export_geojson(self):
        with open('output.geojson', 'w') as geo:
            json.dump(geojson, geo)
    

