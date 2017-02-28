
# coding: utf-8

# In[69]:

#classifer
from numpy import *
import operator
import os

def normNumbers(rawData):
    rowsOfRawData,colsOfRawData=rawData.shape
    maxVals=array([rawData[:,x].max() for x in range(colsOfRawData)])
    minVals=array([rawData[:,x].min() for x in range(colsOfRawData)])
    ranges=maxVals-minVals
    ranges=list(map(lambda x: x if x!=0 else 1,ranges))
    minMat=tile(minVals,(rowsOfRawData,1))
    rangeMat=tile(ranges,(rowsOfRawData,1))
    normMat=(rawData-minMat)/rangeMat
    return normMat,ranges,minVals

def classifer(candidate,trainingData,trainingLabels,k):
    distances=array(list(map(lambda x:(((candidate-x)**2).sum())**0.5,trainingData)))
    resultLabels=trainingLabels[distances.argsort()]
    resultDict={}
    for i in resultLabels[:k]:
        resultDict[i]=resultDict.get(i,0)+1
    result=sorted(resultDict.items(),key=operator.itemgetter(1),reverse=True)
    return result[0][0]

def img2vec(filename):
    fileObject=open(filename,'r')
    return array(list(map(lambda x:int(x),''.join(list(map(lambda x:x[:-1],fileObject.readlines()))))))

def createMat(directory):
    if directory[-1]!='/': directory+='/'
    fileList=os.listdir(directory)
    numOfFile=len(fileList)
    resultMat=zeros((numOfFile,1024))
    resultLabels=[]
    count=0
    for i in fileList:
        resultMat[count,:]=img2vec(directory+i)
        resultLabels.append(int(i[0]))
        count+=1
    return resultMat,array(resultLabels)

def testing(k,print=False):
    testingMat,testingLabels=createMat('/spare/data/notebooks/users/Shu_Li_LIU/testDigits')
    trainingMat,trainingLabels=createMat('/spare/data/notebooks/users/Shu_Li_LIU/trainingDigits')
    testingResults=list(map(lambda x:classifer(x,trainingMat,trainingLabels,k),testingMat))
    results=list(zip(testingResults,list(testingLabels)))
    errorRatio=(sum(list(map(lambda x:0 if x[0]==x[1] else 1,results)))/len(results))
    if print:
        for i in results:
            print('The result is %d while the actual numbers is %d.' %i)
        print('Error ratio is %f.' % errorRatio)
    else:
        return errorRatio


# In[74]:

a0=array([[2,2],[2,3],[3,2],[2.5,2.5],[2.4,2.4],[0,1],[1,0],[0.5,0.5],[0.4,0.4],[0.3,0.3]])
l0=array(['A','A','A','A','A','B','B','B','B','B'])
a1=array([5,5])
print(classifer(a1,a0,l0,9))


# In[71]:

for i in range(1,10):
    print('k=%d, error rate=%f' % (i,testing(i)))


# In[ ]:



