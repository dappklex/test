from operator import itemgetter
from math import log

def createDataSet():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']
    return dataSet, labels

def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCount = {}
    for row in dataSet:
        labelCount[row[-1]] = labelCount.get(row[-1], 0) + 1
    shannonEnt = 0
    for label in labelCount.keys():
        prob = labelCount[label]/numEntries
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt

def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for row in dataSet:
        if row[axis]==value:
            retDataSet.append(row[:axis]+row[axis+1:])
    return retDataSet

def chooseBestFeatureToSplit(dataSet):
    baseShannonEnt = calcShannonEnt(dataSet)
    bestFeature = 0
    bestInfoGain = 0
    for axis in range(len(dataSet[0])-1):
        newShannonEnt = 0
        feature = [row[axis] for row in dataSet]
        uniqueVals = set(feature)
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, axis, value)
            prob = len(subDataSet) / len(dataSet)
            newShannonEnt += prob * calcShannonEnt(subDataSet)
        newInfoGain = newShannonEnt - baseShannonEnt
        if newInfoGain > bestInfoGain:
            bestInfoGain = newInfoGain
            bestFeature = axis
    return bestFeature

def majorityCount(classList):
    classCount = {}
    for i in classList:
        classCount[i] = classCount.get(i, 0)
    sortedClassCount = sorted(classCount.items(), key=itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

# create the tree
def createTree(dataSet, labels):
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    if len(dataSet[0])==1:
        return majorityCount(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel:{}}
    del(labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featVales)
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)
    return myTree

myData, labels = createDataSet()
from pprint import pprint
pprint(createTree(myData, labels)
