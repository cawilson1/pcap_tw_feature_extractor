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
    print('before read')
    featureVals = pd.read_csv(featureFile,
                            sep=',',
                            header=0,
                            nrows = 10000)
    '''
    labels = pd.read_csv('labels.csv',
                         sep=',',
                         header=0)#ignore first row because matlab writes an irrelevant var name to first row
        '''
   # featureNames = pd.read_csv('features.csv',
    #                     sep=',',
    #                     header=0)#same as above
                         
    print('before conversion to np')
    #featureValnp = np.array(featureVals,dtype="float32")
    featureValnp = 0
   # labelsnp = np.array(labels)
    print('after conversion to np')
    featureNamesnp = featureVals.head(0).columns.values
    #featureNamesnp=np.array(featureNames)
    
    #return featureValnp, labelsnp, featureNamesnp
    return featureVals, featureNamesnp

#print(featureValnp)
#print(np.shape(featureValnp))

#print(labels)
#print(featureNames)
''' 
def getNames(featureFile):
    featureVals = pd.read_csv(featureFile,
                            sep=',',
                            header=0)
    

    featureNamesnp = featureVals.head(0).columns.values

    
    return featureNamesnp'''
'''
def chooseFeatures(XFeatures, XFile,yFile):
    inputData = pd.read_csv(XFile,
                            sep=',',
                            usecols=XFeatures,
                            header=0)
    outputData = pd.read_csv(yFile,
                             sep=',',
                             usecols=[0],
                             header=0)

    tempAllX = np.array(inputData, dtype="float")
 
    return tempAllX, np.array(outputData), inputData.head(0).columns.values
'''

def getTimeFeature(featureFile):
    print('before read')
    timeValues = pd.read_csv(featureFile,
                            sep=',',
                            header=0,
                            usecols = ['Time'])

    dropPackets = 0
    timeValues = timeValues['Time']#dunno why i have to do this for this to work
    print(timeValues)
    for i in range(len(timeValues)):
        if not timeValues[i] < 60:
            print('drop packets up to ', i)
            dropPackets = i
            break
        
    
  #  print(timeValues)
   # timeValues = timeValues[timeValues.index > dropPackets]
    #timeValues = timeValues.drop([i for i in range(dropPackets)])
 #   print(timeValues)

    return dropPackets

def main():
    
    #return feature index of packets to eliminate for time windows longer than current time
    dropPackets = getTimeFeature('CICIDS_Friday-WorkingHours.csv')
    '''    
    dropPackets = 0
    timeValues = timeValues['Time']#dunno why i have to do this for this to work
    print(timeValues)
    for i in range(len(timeValues)):
        print(timeValues[i])
        if not timeValues[i] < 60:
            print('drop packets up to ', i)
            dropPackets = i
            break
        
    '''  
    featureValues, featureNames = getFeatures('CICIDS_Friday-WorkingHours.csv')
    featureValues = featureValues[featureValues.index > dropPackets]
    #needs work
    featureValues = featureValues.reindex([i for i in range(len(featureValues))],fill_value=[el for el in featureValues])
    print(featureValues['Time'])
    return
    print(timeValues)
    timeValues = timeValues[timeValues.index > dropPackets]
    #timeValues = timeValues.drop([i for i in range(dropPackets)])
    print(timeValues)
    return
    featureValues, featureNames = getFeatures('CICIDS_Friday-WorkingHours.csv')
    print(featureValues)
    print(featureNames)
    
    #timeStrings = featureValues['Time']#pd.DataFrame(index=featureValues, columns=['Time'])
   # print(timeStrings)
   # print(timeStrings[1] + timeStrings[2])
    dropPackets = 0
    for i in range(len(timeStrings)):
        if not timeStrings[i] < 60:
            print('drop packets up to ', i)
            dropPackets = i
            break
    print(timeStrings.__class__)
    timeStrings = timeStrings.drop([i for i in range(dropPackets)])
    print(timeStrings)
main()