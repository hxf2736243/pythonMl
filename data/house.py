import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from xgboost import XGBClassifier
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.linear_model import LogisticRegression

import pickle

# 读训练数据
train = pd.read_csv('train.csv')

# pull data into target (y) and predictors (X)
train_y = train.SalePrice
predictor_cols = ['LotArea', 'OverallQual', 'YearBuilt', 'TotRmsAbvGrd']
# Create training predictors data
train_X = train[predictor_cols]

#my_model = RandomForestRegressor()
#my_model = LinearRegression()
#my_model = GradientBoostingRegressor()
#my_model = LogisticRegression()
my_model=XGBClassifier()
my_model.fit(train_X, train_y)

# save the model to disk
filename = 'finalized_model.sav'
pickle.dump(my_model, open(filename, 'wb'))


# Read the test data
test = pd.read_csv('test.csv')
# Treat the test data in the same way as training data. In this case, pull same columns.
test_X = test[predictor_cols]
# print(test_X)
# Use the model to make predictions
loaded_model = pickle.load(open(filename, 'rb'))
predicted_prices = loaded_model.predict(test_X)
# We will look at the predicted prices to ensure we have something sensible.
print("-----------------------------预测结果---------------------------")
print(predicted_prices)


my_submission = pd.DataFrame({'Id': test.Id, 'SalePrice': predicted_prices})
# you could use any filename. We choose submission here
my_submission.to_csv('submission.csv', index=False)

