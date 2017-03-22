#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import numpy as np
N = len(features_train)//100

for C in 10.0**np.arange(4,5):
    svc = SVC(C, kernel='rbf')
    start = time()

    # only use 1% of data to train
    print ('------------------------------')
    print 'Fitting with C: {:>10.1f}'.format(C)

    svc.fit(features_train[:], labels_train[:])
    print 'Training time:    {:>10.5f}s'.format(time() - start)

    start = time()
    pred = svc.predict(features_test)
    print 'Predicting time:  {:>10.5f}s'.format(time() - start)
    print 'Test accuracy =   {:>10.5f}\n'.format(accuracy_score(pred, labels_test))
    #########################################################


