#Hello world of ML
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
iris = pd.read_csv('Iris.csv')

iris.head()
iris.isnull().sum()

iris.fillna(iris['SepalWidthCm'].mean(),inplace=True)
s = iris['Species'].unique()

#Label
Y = iris['Species'].map({'Iris-setosa':0, 'Iris-versicolor':1, 'Iris-virginica':2})
Y

X = iris[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']]
X

#Define your algorithm
#KNN - K-Neighbors classifier
from sklearn.neighbors import KNeighborsClassifier
kmodel = KNeighborsClassifier(n_neighbors=3)

#Model evaluation
from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest = train_test_split(X,Y,test_size=0.3)
xtrain.shape

#Train Your model
kmodel.fit(xtrain,ytrain)

#Training accuracy
ytrp = kmodel.predict(xtrain)
(ytrp == ytrain).sum()/len(xtrain)

ytsp = kmodel.predict(xtest)
(ytsp == ytest).sum()/len(xtest)

kmodel.score(xtest,ytest)

#Make predictions
kmodel.predict([[2.1,3.2,1.1,0.2],[4.1,5.2,4.1,7.2]])

tra = []
tsa = []
for i in range(1,15):
  km = KNeighborsClassifier(n_neighbors=i)
  km.fit(xtrain,ytrain)
  tra.append(km.score(xtrain,ytrain))
  tsa.append(km.score(xtest,ytest))
plt.plot(range(1,15),tra)
plt.plot(range(1,15),tsa,color='red')
plt.show()


x1 = X['SepalLengthCm']
x2 = X['SepalWidthCm']
x3 = X['PetalLengthCm']
x4 = X['PetalWidthCm']
Y

yc = Y.map({0:'r', 1:'g', 2:'b'})

plt.scatter(x1,x2,c=yc)
plt.show()

plt.scatter(x3,x4,c=yc)
plt.show()

kmodel.predict([[1.2,4.3,2.2,2.1]])

i = np.array([['setosa'],'versicolor','virginica'])
print(i[kmodel.predict([[1.2,4.3,2.2,2.1], [1.2,4.3,6.2,5.1]])])









