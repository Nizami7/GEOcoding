import requests
from geopandas.tools import geocode, reverse_geocode
from shapely.geometry import Point

class TestNominatim():
    def test_lat_lng_into_location_name(self):
        points = [Point(-71.0594869, 42.3584697), Point(-77.0365305, 38.8977332)]
        df = reverse_geocode(points, provider="nominatim", user_agent='my_request')
        assert df.address[
                   0] == '18-32, Tremont Street, Downtown Crossing, Downtown Boston, Boston, Suffolk County, Massachusetts, 02108, United States'
        assert df.address[
                   1] == 'White House, 1600, Pennsylvania Avenue Northwest, Washington, District of Columbia, 20500, United States'

    def test_location_name_into_lag_lng(self):
        loc = 'Baku'
        assert_point = Point(49.8328009, 40.3755885)
        location = geocode(loc, provider="nominatim", user_agent='my_request')
        point = location.geometry.iloc[0]

        assert assert_point == point

