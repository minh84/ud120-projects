#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
import numpy as np

sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
data_dict.pop('TOTAL', 0)
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below
for k, v in data_dict.items():
    if str(v['salary']) == 'NaN' or str(v['bonus']) == 'NaN':
        continue
    if v['salary']>1e6 and v['bonus'] > 5e6:
        print k, v['salary'], v['bonus']

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()