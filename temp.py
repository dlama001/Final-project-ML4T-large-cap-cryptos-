from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2, f_regression
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD
from keras.layers import LSTM
from keras.wrappers.scikit_learn import KerasRegressor
from statsmodels.tsa.arima_model import ARIMA
import statsmodels.api as sm
# pandas, pandas_datareader, numpy and matplotlib
import numpy as np
import pandas as pd
import pandas_datareader.data as web
from matplotlib import pyplot

# load dataset
dataset = pd.read_csv('BitstampData.csv')
dataset.shape
# peek at data
set_option('display.width', 100)
dataset.tail(2)
#calculation of exponential moving average
def EMA(df, n):
EMA = pd.Series(df['Close'].ewm(span=n, min_periods=n).mean(), name='EMA_'\
+ str(n))
return EMA
dataset['EMA10'] = EMA(dataset, 10)
dataset['EMA30'] = EMA(dataset, 30)
dataset['EMA200'] = EMA(dataset, 200)
dataset.head()
#calculation of rate of change
def ROC(df, n):
M = df.diff(n - 1)
N = df.shift(n - 1)
ROC = pd.Series(((M / N) * 100), name = 'ROC_' + str(n))
return ROC
dataset['ROC10'] = ROC(dataset['Close'], 10)
dataset['ROC30'] = ROC(dataset['Close'], 30)
#calculation of price momentum
def MOM(df, n):
MOM = pd.Series(df.diff(n), name='Momentum_' + str(n))
return MOM
dataset['MOM10'] = MOM(dataset['Close'], 10)
dataset['MOM30'] = MOM(dataset['Close'], 30)
#calculation of relative strength index
def RSI(series, period):
delta = series.diff().dropna()
u = delta * 0
d = u.copy()
u[delta > 0] = delta[delta > 0]
d[delta < 0] = -delta[delta < 0]
u[u.index[period-1]] = np.mean( u[:period] ) #first value is sum of avg gains
u = u.drop(u.index[:(period-1)])
d[d.index[period-1]] = np.mean( d[:period] ) #first value is sum of avg losses
d = d.drop(d.index[:(period-1)])
rs = u.ewm(com=period-1, adjust=False).mean() / \
d.ewm(com=period-1, adjust=False).mean()
return 100 - 100 / (1 + rs)
dataset['RSI10'] = RSI(dataset['Close'], 10)
dataset['RSI30'] = RSI(dataset['Close'], 30)
dataset['RSI200'] = RSI(dataset['Close'], 200)
#calculation of stochastic osillator.
def STOK(close, low, high, n):
STOK = ((close - low.rolling(n).min()) / (high.rolling(n).max() - \
low.rolling(n).min())) * 100
return STOK
def STOD(close, low, high, n):
STOK = ((close - low.rolling(n).min()) / (high.rolling(n).max() - \
low.rolling(n).min())) * 100
STOD = STOK.rolling(3).mean()
return STOD
dataset['%K10'] = STOK(dataset['Close'], dataset['Low'], dataset['High'], 10)
dataset['%D10'] = STOD(dataset['Close'], dataset['Low'], dataset['High'], 10)
dataset['%K30'] = STOK(dataset['Close'], dataset['Low'], dataset['High'], 30)
dataset['%D30'] = STOD(dataset['Close'], dataset['Low'], dataset['High'], 30)
dataset['%K200'] = STOK(dataset['Close'], dataset['Low'], dataset['High'], 200)
dataset['%D200'] = STOD(dataset['Close'], dataset['Low'], dataset['High'], 200)
#calculation of moving average
def MA(df, n):
MA = pd.Series(df['Close'].rolling(n, min_periods=n).mean(), name='MA_'\
+ str(n))
return MA
dataset['MA21'] = MA(dataset, 10)
dataset['MA63'] = MA(dataset, 30)
dataset['MA252'] = MA(dataset, 200)
dataset[['Weighted_Price']].plot(grid=True)
plt.show()
fig = plt.figure()
plot = dataset.groupby(['signal']).size().plot(kind='barh', color='red')
plt.show()
# split out validation dataset for the end
subset_dataset= dataset.iloc[-100000:]
Y= subset_dataset["signal"]
X = subset_dataset.loc[:, dataset.columns != 'signal']
validation_size = 0.2
seed = 1
X_train, X_validation, Y_train, Y_validation =\
train_test_split(X, Y, test_size=validation_size, random_state=1)
# test options for classification
num_folds = 10
scoring = 'accuracy'
models = []
models.append(('LR', LogisticRegression(n_jobs=-1)))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
#Neural Network
models.append(('NN', MLPClassifier()))
# Ensemble Models
# Boosting methods
models.append(('AB', AdaBoostClassifier()))
models.append(('GBM', GradientBoostingClassifier()))
# Bagging methods
models.append(('RF', RandomForestClassifier(n_jobs=-1)))
n_estimators = [20,80]
max_depth= [5,10]
criterion = ["gini","entropy"]
param_grid = dict(n_estimators=n_estimators, max_depth=max_depth, \
criterion = criterion )
model = RandomForestClassifier(n_jobs=-1)
kfold = KFold(n_splits=num_folds, random_state=seed)
grid = GridSearchCV(estimator=model, param_grid=param_grid, \
scoring=scoring, cv=kfold)
grid_result = grid.fit(X_train, Y_train)
print("Best: %f using %s" % (grid_result.best_score_,\
grid_result.best_params_))
# prepare model
model = RandomForestClassifier(criterion='gini', n_estimators=80,max_depth=10)
#model = LogisticRegression()
model.fit(X_train, Y_train)
# estimate accuracy on validation set
predictions = model.predict(X_validation)
print(accuracy_score(Y_validation, predictions))
Importance = pd.DataFrame({'Importance':model.feature_importances_*100},\
index=X.columns)
Importance.sort_values('Importance', axis=0, ascending=True).plot(kind='barh', \
color='r' )
plt.xlabel('Variable Importance')
backtestdata = pd.DataFrame(index=X_validation.index)
backtestdata['signal_pred'] = predictions
backtestdata['signal_actual'] = Y_validation
backtestdata['Market Returns'] = X_validation['Close'].pct_change()
backtestdata['Actual Returns'] = backtestdata['Market Returns'] *\
backtestdata['signal_actual'].shift(1)
backtestdata['Strategy Returns'] = backtestdata['Market Returns'] * \
backtestdata['signal_pred'].shift(1)
backtestdata=backtestdata.reset_index()
backtestdata.head()
backtestdata[['Strategy Returns','Actual Returns']].cumsum().hist()
backtestdata[['Strategy Returns','Actual Returns']].cumsum().plot()