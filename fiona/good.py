import os
import fiona

assert "GDAL_DATA" not in os.environ

with fiona.Env():
    with fiona.open("data/test.shp", "r") as source:
        print(source.crs)

with fiona.open("data/test.shp", "r") as source:  # Cached
    print(source.crs)
