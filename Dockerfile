FROM python:3.7-slim

RUN python -m pip install munch --prefer-binary
RUN python -m pip install "rasterio==1.0.13" --only-binary :all:
RUN python -m pip install "fiona==1.8.4" --only-binary :all:

WORKDIR /src
COPY . /src/

# Rasterio
RUN python rasterio/good.py
RUN python rasterio/bad.py || true

# Fiona
RUN python util/convert.py
RUN ls data/

RUN python fiona/good.py
RUN python fiona/bad.py || true
