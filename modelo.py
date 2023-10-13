import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

data=pd.read_csv("../data/processed/datos.csv",index_col=0)

X = data.drop(['tempMensual','date'], axis=1)
y = data['tempMensual']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo = RandomForestRegressor(n_estimators=100, random_state=42)

modelo.fit(X_train, y_train)

pickle.dump(modelo, open('temp.pkl','wb'))