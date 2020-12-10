import json
import pickle
import warnings
warnings.filterwarnings('ignore')
import numpy as np

__location = None
__model = None
__data_columns = None

def estimation(area,sqft,bed,bath,room,park,type,regfee,commis,age):
    p={'yes':1,'no':0}
    bt = {'commercial': 0, 'house': 1, 'others': 2}
    x = np.zeros(len(__data_columns))
    x[0] = __location.index(area.lower())
    x[1] = sqft
    x[2] = bed
    x[3] = bath
    x[4] = room
    x[5] = p[park]
    x[6] = bt[type]
    x[7] = regfee
    x[8] = commis
    x[9] = age

    return round(__model.predict([x])[0]/100000, 2)

def get_locations():
    return __location

def load_artifacts():
    print('loading saved artifacts....start')
    global __data_columns
    global __model
    global __location

    with open("./artifacts/area.json", "r") as f:
        __location = json.load(f)["areas"]

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)["data_columns"]

    with open("./artifacts/house pricing pickle.pickle", "rb") as f:
        __model = pickle.load(f)
    print('loading saved artifacts...Done')


if __name__ == '__main__':
    load_artifacts()
    print(get_locations())
    print(estimates('adyar',909,1,1,3,'no','commercial',421094,92114,20))