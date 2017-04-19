#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
import numpy as np
features_train, features_test, labels_train, labels_test = train_test_split(features,
                                                                            labels,
                                                                            test_size=0.3,
                                                                            random_state=42)

clf = DecisionTreeClassifier()
clf.fit(features_train, labels_train)
print (np.sum(labels_test))
print (len(labels_test))
print (accuracy_score(clf.predict(features_test), labels_test))
print (precision_score(clf.predict(features_test), labels_test))
print (recall_score(clf.predict(features_test), labels_test))
print (np.where(np.array(labels_test)==1.0))
print (np.where(np.array(clf.predict(features_test))==1.0))

preds = np.array([0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1])
truth = np.array([0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0])

print (len(np.where((preds == 0) & (truth==1))[0]))
# prec
print (precision_score(truth, preds))
print (recall_score(truth, preds))