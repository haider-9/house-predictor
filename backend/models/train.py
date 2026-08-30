from sklearn.linear_model import LinearRegression
from util.preprocessing import load_data

X_train, X_test, y_train, y_test=load_data()
model=LinearRegression()
model.fit(X_train,y_train)