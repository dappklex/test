#data in https://www.kaggle.com/c/GiveMeSomeCredit/data
# libraries
require(VIM)
require(mice)

# read data
setwd('C:/Users/dappk/OneDrive/Git/GiveMeSomeCredit')
rawdata <- read.csv('cs-training.csv', header = TRU)
traindata <- rawdata[2:12]
names(traindata) <- c('y', paste('x', 1:10, sep = ''))

# explore data
matrixplot(traindata)
md.pattern(traindata)

# imputate missing values
require(DMwR)
traindata <- knnImputation(traindata)
