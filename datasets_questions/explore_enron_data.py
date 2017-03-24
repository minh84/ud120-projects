#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))


print len(enron_data.keys())
print len(enron_data.values()[0])

nb_poi = 0
s = 'James'.upper()
print s
for k in enron_data:
    if enron_data[k]['poi'] == 1:
        nb_poi += 1

    if k == 'PRENTICE JAMES':
        print k, enron_data[k]['total_stock_value']
    if 'COLWELL WESLEY' == k:
        print k, enron_data[k]['from_this_person_to_poi']
    if 'SKILLING JEFFREY K' == k:
        print k, enron_data[k]['exercised_stock_options']
print('number poi {}'.format(nb_poi))

nb_per = 0
with open('../final_project/poi_names.txt', 'r') as f:
    for l in f:
        if l.startswith('(y') or l.startswith('(n)'):
            nb_per += 1
            #print (l)

print(nb_per)