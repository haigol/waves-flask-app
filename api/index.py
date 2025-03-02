from flask import Flask, jsonify, request
from flask_cors import CORS
import xarray as xr
import numpy as np

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": ["http://localhost:3000", "https://map-waves-assignment-haigols-projects.vercel.app", "https://map-waves-assignment.vercel.app", "https://map-waves-assignment-git-main-haigols-projects.vercel.app"]}})

@app.route('/', methods=['GET'])
def home():
    return "Flask running on port 8080"


@app.route('/hmaxByCoords', methods=['POST'])
def getHMaxAtCoords():
    data = request.get_json()

    lat = data['lat']
    lon = data['lon']
    
    try:
        ds = xr.open_dataset("./waves_2019-01-01.nc", engine="netcdf4")
        ds_hmax_array = ds["hmax"].sel(longitude=lon,latitude=lat, method="nearest")
        ds_hmax_max_value = (ds_hmax_array.values.max())
    
        return str(ds_hmax_max_value) # either string value or nan if no value found (handle on client side)
    except Exception as e:
        print("Error occured", e)

