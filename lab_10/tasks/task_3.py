import filecmp
import pathlib
from typing import Union
from os import listdir
from os.path import isfile, join
import pandas as pd




def concat_data(path: Union[str, pathlib.Path],):
    files = [f for f in listdir(path) if isfile(join(path, f))]
    all_data = None
    for file_ in files:
        day = int(file_.split('_')[2].split('.')[0])
        data = pd.read_csv(pathlib.Path(path) / file_) 
        data = data[['created', 'min_temp', 'the_temp', 'max_temp', 'air_pressure', 'humidity', 'visibility', 'wind_direction_compass', 'wind_direction', 'wind_speed']]
        data.rename(columns={'the_temp':'temp'}, inplace=True)
        data.created = pd.to_datetime(data.created)
        data = data[data.created.dt.day == day]
        if all_data is not None:
            all_data = all_data.append(data.copy()) 
        else:
            all_data = data.copy()
    all_data.sort_values(['created'], inplace=True)
    all_data.created = all_data.created.dt.strftime('%Y-%m-%dT%H:%M')
    with open(str(path) + '.csv', 'w+') as f:
        f.write(all_data.to_csv(index=False))

if __name__ == "__main__":
    concat_data("weather_data/523920_2017_03")
    assert filecmp.cmp("expected_523920_2017_03.csv", "weather_data/523920_2017_03.csv")
