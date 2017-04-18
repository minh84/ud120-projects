#!/usr/bin/python

import numpy as np
def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    errs = np.abs(predictions - net_worths)

    nb_keep = int(0.9 * len(errs))
    idx_sort = np.argsort(errs, axis=0)

    for i in xrange(nb_keep):
        cleaned_data.append((ages[idx_sort[i]],
                             net_worths[idx_sort[i]],
                             predictions[idx_sort[i]]))
    
    return cleaned_data

