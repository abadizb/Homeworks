import os
import urllib.request
import json
from pprint import pprint
import sys
import pickle
import shelve
def indexer():

    Dict = {}
    pickles = open ("C:\Users\Halim\Python34\raw_data.pickle","br")
    x = pickle.load(r)
    shelve = shelve.open("datalist")
    for filepath, file_content in x:
        file_content = file_content.split()
        for word in file_content:
            if(word not in Dict.keys()):
                Dict[word]={x}
            else:
                Dict[word]= Dict[word]|{x}
    for key, value in Dict.items():
        shelve[key]=(value)
    pickles.close()
    shelve.close()

indexer()
