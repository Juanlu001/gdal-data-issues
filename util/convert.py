import fiona

with fiona.Env():
    with fiona.open("data/test.json", "r") as source:
        with fiona.open(
            "data/test.shp",
            "w",
            driver="ESRI Shapefile",
            schema=source.schema,
            crs=source.crs,
        ) as sink:
            for feature in source:
                sink.write(feature)
