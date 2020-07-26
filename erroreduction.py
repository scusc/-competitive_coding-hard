#Regression - 
import numpy as np
x = np.array([2.3,4,5.6,7.8,9.2]).reshape(5,1)
y = np.array([3.4,5.6,7.6,8.7,9.5]).reshape(5,1)

#Ordinary Least square method
x_mean = x.mean()
y_mean = y.mean()

num = 0
den = 0
for i in range(len(x)):
  num += (x[i]-x_mean)*(y[i]-y_mean)
  den += (x[i]-x_mean)**2
m = num/den
c = y_mean - m*x_mean

print(m,c)

import matplotlib.pyplot as plt
plt.scatter(x,y)
plt.plot(x,yp,color='red')
plt.show()

#MAE or mean absolute error
np.abs(yp - y).mean()

#MSE mean squared error
((yp-y)**2).mean()

a = 4
print('Prediction of a',m*a + c)

from sklearn.linear_model import LinearRegression
lmodel = LinearRegression()

lmodel.fit(x,y)

print(lmodel.coef_ , lmodel.intercept_)

from sklearn import metrics
print(metrics.mean_absolute_error(yp,y))
print(metrics.mean_squared_error(yp,y))

lmodel.predict([[a]])

x1 = 5
x2 = 7
Y = 31

m1 = 0.5
m2 = 0.8

Yp = m1*x1 + m2*x2
Yp
(Yp - Y)**2

error_values = []
for i in range(0,20):
  Yp = m1*x1 + m2*x2
  dem1 = 2*(Y-Yp)*(-x1) 
  dem2 = 2*(Y-Yp)*(-x2) 

  m1 = m1 - 0.01 * dem1
  m2 = m2 - 0.01 * dem2

  error = (Y-Yp)**2
  error_values.append(error)
  print('m1:',m1,'m2:',m2,'yp:',Yp,'error:',error)

plt.plot(error_values)
plt.show()

Yp = m1*x1 + m2*x2
Yp

(Yp - Y)**2

0.001 * dem1

dem2
