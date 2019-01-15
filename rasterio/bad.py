import os
import rasterio
from rasterio.crs import CRS

assert "GDAL_DATA" not in os.environ

azeq_point = CRS(
    {
        "units": "m",
        "proj": "aeqd",
        "ellps": "WGS84",
        "datum": "WGS84",
        "lat_0": -17.0,
        "lon_0": -44.0,
    }
)

assert azeq_point == azeq_point
wgs84 = CRS.from_epsg(4326)

try:
    assert not azeq_point == wgs84  # We are doomed!
except:
    pass

with rasterio.Env():  # Useless now!
    assert azeq_point == azeq_point
    wgs84 = CRS.from_epsg(4326)
    assert not azeq_point == wgs84
