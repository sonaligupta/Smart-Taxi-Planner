from datetime import datetime

import pandas as pd
import os


indir ='/Users/Mac/PycharmProjects/DMProject/chicago-taxi-rides-2016'

for root, dirs, filenames in os.walk(indir):
    for f in filenames:
        print(f)
        data = pd.read_csv(os.path.join(root,f))


        #NaN entries in the ‘columns’ column with the empty string
        data.trip_start_timestamp =data.trip_start_timestamp.fillna('')
        data.trip_end_timestamp =data.trip_end_timestamp.fillna('')
        data.pickup_latitude=data.pickup_latitude.fillna('')
        data.pickup_longitude=data.pickup_longitude.fillna('')
        data.dropoff_longitude=data.dropoff_longitude.fillna('')
        data.dropoff_latitude=data.dropoff_latitude.fillna('')
        data.taxi_id = data.taxi_id.fillna('')
        data.tips=data.tips.fillna('')
        data.trip_miles= data.trip_miles.fillna('')
        data.fare=data.fare.fillna('')
        data.company=data.company.fillna('')

        #Drop all columns with any NA values:
        data.dropna(axis=1, how='any')

        #Normalize data types:
        #Convert data type of timestamps into datetime format
        dtypes ={'trip_start_timestamp': 'str',
                 'trip_end_timestamp':'str'}
        parse_dates =['trip_start_timestamp','trip_end_timestamp' ]
        data = pd.read_csv(os.path.join(root,f),
                           dtype=dtypes,
                           parse_dates=parse_dates,
                           date_parser = pd.core.tools.datetimes.to_datetime)
        data.info()

        #export cleaned data into new csv files for further processing
        num, ext = os.path.basename(f).split(".", 1)
        data.to_csv(os.path.join(os.path.dirname(f), "%s.csv" % (num,)))



















