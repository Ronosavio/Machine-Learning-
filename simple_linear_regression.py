import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#importing the data set 
dataset = pd.read_csv('D:/DS/CSV_files/Salary_Data.csv')
X = dataset.iloc[:, 0].values.reshape(-1, 1)
Y = dataset.iloc[:, :1].values

# splitting the dataset into training dataset and testing data set
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 1/3 , random_state= 0)


# fitting the simple linear regression model to training set 
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, Y_train)

#predicting the test set results 
y_pred = regressor.predict(X_test)

# visualizing the training set 
plt.scatter(X_train,  Y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs experience (training set)')
plt.xlabel('Years of experience ')
plt.ylabel('Salary')
plt.show()