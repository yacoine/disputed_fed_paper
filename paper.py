import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from warnings import simplefilter
from sklearn import linear_model
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.pipeline import Pipeline
from sklearn.model_selection import KFold

#Read and store frequency of words in numpy array
#Value in index 0 are the author names

def get_mae(min_split, train_X, val_X, train_y, val_y):
 
	model= RandomForestRegressor(n_estimators=10,min_samples_split=min_split,random_state=1)
	model.fit(train_X,train_y)
	predict_val=model.predict(val_X)
	mae=mean_absolute_error(predict_val,val_y)

	return mae


path='federalist_papers_data.csv'
paper_data=np.genfromtxt(path,delimiter=',')

txt_path='federalist_papers_wordlist.txt'
word_txt=np.genfromtxt(txt_path, dtype='str')


df=pd.DataFrame()

df['Name']=paper_data[:,0]

for i in range(0,len(word_txt)):
	df[word_txt[i]]= paper_data[:,i+1]

df_test=df.loc[(df['Name'] >2.0)]
df_disputed=df_test[df_test.columns.difference(['Name'])]

df = df.loc[(df['Name']<= 2)]

y_train=df.Name
X_train=df[df.columns.difference(['Name'])]


train_X, val_X, train_y, val_y = train_test_split(X_train, y_train, random_state=1)

lm=linear_model.LinearRegression()
model =lm.fit(train_X,train_y)
predictions= lm.predict(val_X)

result_pred=[]
for i in range(len(predictions)):
	
	if(predictions[i]<=1.5):
		result_pred.append(1)
	else:
		result_pred.append(2)
	print(predictions[i],':',result_pred[i], ':',int(val_y.iloc[i]) )

print(mean_absolute_error(result_pred,val_y))
#print(model.score(val_X, val_y))

print(X_train)
print(y_train)

lm1=linear_model.LinearRegression()
model =lm1.fit(X_train,y_train)
disputed_prediction= lm.predict(df_disputed)
print(disputed_prediction)

disputed_result=[]
for i in range(len(disputed_prediction)):
	
	if(disputed_prediction[i]<=1.5):
		disputed_result.append("Hamilton")
	else:
		disputed_result.append("Madison")
print(disputed_result)

