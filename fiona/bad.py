import os
import fiona

assert "GDAL_DATA" not in os.environ

try:
    with fiona.open("data/test.shp", "r") as source:
        print(source.crs)  # We are doomed!
except:
    pass


with fiona.Env():  # Useless now!
    with fiona.open("data/test.shp", "r") as source:
        print(source.crs)
