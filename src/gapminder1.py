# TODO: Add import statements
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Assign the dataframe to this variable.
# TODO: Load the data
bmi_life_data = pd.read_csv("../resources/bmi_and_life_expectancy.csv")
# independent variable which we are going to predict
X = bmi_life_data[['BMI']]
# This makes it into a 2d array
# Depends on the BMI. Dependent variables
Y = bmi_life_data[['Life expectancy']]

# Make and fit the linear regression model
#TODO: Fit the model and Assign it to bmi_life_model
bmi_life_model = LinearRegression()
bmi_life_model.fit(X, Y)

# Mak a prediction using the model
# TODO: Predict life expectancy for a BMI value of 21.07931
laos_life_exp = bmi_life_model.predict([[21.07931]])
print('BMI Data: {}'.format(X))
print('Life expectancy Data: {}'.format(Y))
print('Predicted life expectancy: {}'.format(laos_life_exp))