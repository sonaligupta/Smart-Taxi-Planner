from collections import namedtuple

import pandas as pd
import os

indir = '/Users/Mac/PycharmProjects/DMProject/Cleaned-files'

for root, dirs, filenames in os.walk(indir):
    for f in filenames:
        print(f)
        data = pd.read_csv(os.path.join(root,f))

        trip_start_time   =    data.trip_start_timestamp
        trip_end_timestamp =   data.trip_end_timestamp
        data_pickup_latitude = data.pickup_latitude
        data_pickup_longitude = data.pickup_longitude

        #store coordinates of location as a point
        Point = namedtuple('Point','x y')
        pickup_point = Point(data_pickup_latitude,data_pickup_longitude)
        print(pickup_point)

        dropoff_longitude=data.dropoff_longitude
        dropoff_latitude=data.dropoff_latitude

        Point = namedtuple('Point', 'x y')
        dropoff_point=Point(data.dropoff_latitude,data.dropoff_longitude)

        taxi_id = data.taxi_id
        tips=data.tips
        trip_miles=data.trip_miles
        fare=data.fare
        company=data.company






