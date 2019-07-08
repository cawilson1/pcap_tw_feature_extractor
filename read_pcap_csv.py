# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 14:05:40 2019

@author: User
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 19:30:51 2018

@author: Casey
"""

import pandas as pd
import numpy as np


def getFeatures(featureFile):
 #   print('before read')
    featureVals = pd.read_csv(featureFile,
                            sep=',',
                            header=0,
                            nrows = 10000)

                         
 #   print('before conversion to np')
    #featureValnp = np.array(featureVals,dtype="float32")
  #  featureValnp = 0
   # labelsnp = np.array(labels)
#    print('after conversion to np')
    featureNamesnp = featureVals.head(0).columns.values
    #featureNamesnp=np.array(featureNames)
    
    #return featureValnp, labelsnp, featureNamesnp
    return featureVals, featureNamesnp


def getTimeFeature(featureFile):
#    print('before read')
    timeValues = pd.read_csv(featureFile,
                            sep=',',
                            header=0,
                            usecols = ['Time'])

    dropPackets = 0
    timeValues = timeValues['Time']#dunno why i have to do this for this to work
    print(timeValues)
    
    
    for i in range(len(timeValues)):
        if not timeValues[i] < 60:
  #          print('drop packets up to ', i)
            dropPackets = i
            break

    return dropPackets

def getAllFeatures():
    
    #return feature index of packets to eliminate for time windows longer than current time
    dropPackets = getTimeFeature('CICIDS_Friday-WorkingHours.csv')

    featureValues, featureNames = getFeatures('CICIDS_Friday-WorkingHours.csv')
    valuesToLabel = featureValues[featureValues.index > dropPackets]

    valuesToLabel = valuesToLabel.set_index(np.arange(len(valuesToLabel)))#this list corresponds to the values that will actually be labelled. The original list is still necessary to compute features    
        
 #   print(featureValues)
 #   print(valuesToLabel)
    return valuesToLabel,featureValues,dropPackets