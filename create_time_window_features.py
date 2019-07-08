# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 11:28:13 2019

File to create time window features

@author: User
"""
import numpy as np

from read_pcap_csv import getAllFeatures
def calcNumPackets(featureDF):
    return len(featureDF)

def currentWindow(allValues,dropPackets,windowLength):

    originalIdx = dropPackets
    changingIdx = originalIdx
   # currentWindow = np.where(allValues[originalIdx][1] - allValues[changingIdx][1] < windowLength, allValues, -1)
    
    
    #this may need a binary-type search to be more efficient, calculating more features takes almost no time, but doing this loop twice makes the program about twice as slow
    #this seems to be the big bottleneck
    #calculate this as infrequently as possible
#    while allValues[originalIdx][1] - allValues[changingIdx][1] < windowLength:
#        changingIdx = changingIdx - 1
    print(allValues[:originalIdx])#shortens the slice to return
    getdex = 0
    it = np.nditer(allValues[:originalIdx],flags=['f_index'])#cant go backwards
    while not it.finished:
        if allValues[originalIdx][1] - allValues[it][1] < windowLength:
            getdex = it
            break
    print(getdex)
        
  #  return
   # print(allValues.iloc[changingIdx+1:originalIdx+1])#this is inclusive; ie the time window begins at the current packet, which is included in the list
    numPackets = calcNumPackets(allValues[changingIdx+1:originalIdx+1])
    numPackets = calcNumPackets(allValues[changingIdx+1:originalIdx+1])
    numPackets = calcNumPackets(allValues[changingIdx+1:originalIdx+1])
    numPackets = calcNumPackets(allValues[changingIdx+1:originalIdx+1])
    numPackets = calcNumPackets(allValues[changingIdx+1:originalIdx+1])
    return numPackets

def loopAllWindows(allValues,dropPackets):
   # timeWindowsLengths = [1,2,4,8,16,32,60]
   #each window double the size of the previous will take about twice as long since it has to check approx double the number of indices
    timeWindowsLengths = [1]
    allWindowsCurrentPacket = []
    for windowLength in timeWindowsLengths:

        allWindowsCurrentPacket.append(currentWindow(allValues,dropPackets,windowLength))
        
    print(allWindowsCurrentPacket)

def main():

    valuesToLabel,allValues,dropPackets = getAllFeatures()
    allValues = allValues.values#convert to np arrays for performance
    valuesToLabel = valuesToLabel.values

    
   # print(valuesToLabel[:,0])
    for el in valuesToLabel[:,0]:
        packetIndex = el - 2#subtracting 2 brings it to correct index
        print(el-2)
      #  print(packetIndex)
      #  print(allValues[packetIndex][:,1])
        loopAllWindows(allValues,packetIndex)
        return
      #  return
    
    #order
    #for each packet
        #for each windowLength
            #for each window
                # for each feature
                    #calc values
                    
main()