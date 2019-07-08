# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 11:28:13 2019

File to create time window features

@author: User
"""
from read_pcap_csv import getAllFeatures
def calcNumPackets(featureDF):
    return len(featureDF)

def currentWindow(allValues,dropPackets,windowLength):

    originalIdx = dropPackets
    changingIdx = originalIdx
    while allValues.iloc[originalIdx]['Time'] - allValues.iloc[changingIdx]['Time'] < windowLength:
        changingIdx = changingIdx - 1
   # print(allValues.iloc[changingIdx+1:originalIdx+1])#this is inclusive; ie the time window begins at the current packet, which is included in the list
    numPackets = calcNumPackets(allValues.iloc[changingIdx+1:originalIdx+1])
    return numPackets

def loopAllWindows(allValues,dropPackets):
    timeWindowsLengths = [1,2,4,8,16,32,60]
    allWindowsCurrentPacket = []
    for windowLength in timeWindowsLengths:

        allWindowsCurrentPacket.append(currentWindow(allValues,dropPackets,windowLength))
        
    print(allWindowsCurrentPacket)

def main():

    valuesToLabel,allValues,dropPackets = getAllFeatures()
    #print(allValues.iloc[dropPackets])
    #print(allValues.iloc[dropPackets]['Time'])
    
    for el in valuesToLabel['No.']:
        packetIndex = el - 2#subtracting 2 brings it to correct index

        loopAllWindows(allValues,packetIndex)
    
    #order
    #for each packet
        #for each windowLength
            #for each window
                # for each feature
                    #calc values
                    
main()