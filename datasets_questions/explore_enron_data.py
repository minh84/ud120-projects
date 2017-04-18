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
nb_has_salary = 0
nb_has_email = 0
nb_has_total_payment = 0
nb_has_total_payment_poi = 0
for k in enron_data:
    if enron_data[k]['poi'] == 1:
        nb_poi += 1
        try:
            val = int(enron_data[k]['total_payments'])
            nb_has_total_payment_poi += 1
        except:
            pass


    try:
        val = int(enron_data[k]['salary'])
        nb_has_salary += 1
    except:
        pass

    try:
        val = int(enron_data[k]['total_payments'])
        nb_has_total_payment += 1
    except:
        pass

    val = str(enron_data[k]['email_address'])
    if val != 'NaN':
        nb_has_email += 1

    if k == 'PRENTICE JAMES':
        print k, enron_data[k]['total_stock_value']
    if 'COLWELL WESLEY' == k:
        print k, enron_data[k]['from_this_person_to_poi']
    if 'SKILLING JEFFREY K' == k:
        print k, enron_data[k]['exercised_stock_options']

    if 'LAY KENNETH L' == k:
        print k, enron_data[k]

print('number poi {}'.format(nb_poi))
print('number poi has total paymern {} {}'.format(nb_has_total_payment_poi, 1.0 - float(nb_has_total_payment_poi)/nb_poi))
print('number has salary {}'.format(nb_has_salary))
print('number has total payment {} {}'.format(nb_has_total_payment, 1-float(nb_has_total_payment)/len(enron_data.keys())))
print('number has email {}'.format(nb_has_email))

nb_per = 0
with open('../final_project/poi_names.txt', 'r') as f:
    for l in f:
        if l.startswith('(y') or l.startswith('(n)'):
            nb_per += 1
            #print (l)

print(nb_per)