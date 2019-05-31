import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
import warnings
warnings.filterwarnings(action="ignore")


# import train and test CSV files
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

titanic=pd.concat([train, test], sort=False)
len_train=train.shape[0]

print(titanic.dtypes.sort_values())
titanic.head()

titanic.isnull().sum()[titanic.isnull().sum()>0]

train.Age=train.Age.fillna(train.Age.mean())
test.Age=test.Age.fillna(train.Age.mean())

train.Fare=train.Fare.fillna(train.Fare.mean())
test.Fare=test.Fare.fillna(train.Fare.mean())

train.Cabin=train.Cabin.fillna("unknow")
test.Cabin=test.Cabin.fillna("unknow")

train.Embarked=train.Embarked.fillna(train.Embarked.mode()[0])
test.Embarked=test.Embarked.fillna(train.Embarked.mode()[0])


