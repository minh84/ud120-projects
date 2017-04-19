#!/usr/bin/python

import os
import pickle
import re
import sys

sys.path.append( "../tools/" )
from parse_out_email_text import parseOutText

"""
    Starter code to process the emails from Sara and Chris to extract
    the features and get the documents ready for classification.

    The list of all the emails from Sara are in the from_sara list
    likewise for emails from Chris (from_chris)

    The actual documents are in the Enron email dataset, which
    you downloaded/unpacked in Part 0 of the first mini-project. If you have
    not obtained the Enron email corpus, run startup.py in the tools folder.

    The data is stored in lists and packed away in pickle files at the end.
"""




from_data = []
word_data = []

reparse = True
if reparse:
    from_sara = open("from_sara.txt", "r")
    from_chris = open("from_chris.txt", "r")

    ### temp_counter is a way to speed up the development--there are
    ### thousands of emails from Sara and Chris, so running over all of them
    ### can take a long time
    ### temp_counter helps you only look at the first 200 emails in the list so you
    ### can iterate your modifications quicker
    temp_counter = 0
    temp_counter_limit = 20000
    outliers_words = ["sshacklensf", "cgermannsf"]
    removed_words = ["sara", "shackleton", "chris", "germani"] + outliers_words

    for name, from_person in [("sara", from_sara), ("chris", from_chris)]:
        for path in from_person:
            ### only look at first 200 emails when developing
            ### once everything is working, remove this line to run over full dataset
            temp_counter += 1
            if temp_counter < temp_counter_limit:
                path = os.path.join('..', path[:-1])
                print path
                email = open(path, "r")

                ### use parseOutText to extract the text from the opened email
                words = parseOutText(email)

                ### use str.replace() to remove any instances of the words
                ### ["sara", "shackleton", "chris", "germani"]
                for w in removed_words:
                    words = words.replace(w, '')
                # words = ' '.join([w for w in words.split() if w not in removed_words])

                ### append the text to word_data
                word_data.append(words)
                ### append a 0 to from_data if email is from Sara, and 1 if email is from Chris
                from_data.append(0 if name=='sara' else 1)

                email.close()


    pickle.dump( word_data, open("your_word_data.pkl", "w") )
    pickle.dump( from_data, open("your_email_authors.pkl", "w") )

    print "emails processed"
    from_sara.close()
    from_chris.close()
else:
    word_data = pickle.load(open("your_word_data.pkl", "r"))
    from_data = pickle.load(open("your_email_authors.pkl", "r"))
    print "pickl emails processed is loaded"

print(word_data[152])



### in Part 4, do TfIdf vectorization here
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import SelectPercentile, f_classif

tfidf_vec = TfidfVectorizer(stop_words='english')
tfidf = tfidf_vec.fit_transform(word_data)
print (len(tfidf_vec.get_feature_names()))
print (tfidf_vec.get_feature_names()[34597])
print tfidf.shape
selector = SelectPercentile(f_classif, percentile=10)
selector.fit(tfidf, from_data)
tfidf_reduced = selector.transform(tfidf).toarray()
print tfidf_reduced.shape