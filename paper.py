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

#Data frame is created from a csv file that contains the frequency of usage
#of the 70 most used words in the federalist papers
#First column is either 1 = Hamilton, 2=Madison, 3=Disputed
path='federalist_papers_data.csv'
paper_data=np.genfromtxt(path,delimiter=',')

#70 most used words,
txt_path='federalist_papers_wordlist.txt'
word_txt=np.genfromtxt(txt_path, dtype='str')

#creationg of empty data frame
df=pd.DataFrame()

#name column
df['Name']=paper_data[:,0]

#word and frequency column
for i in range(0,len(word_txt)):
	df[word_txt[i]]= paper_data[:,i+1]

#data frame for disputed papers 
df_test=df.loc[(df['Name'] >2.0)]
df_disputed=df_test[df_test.columns.difference(['Name'])]

#data frame for the undisputed fed papers
df = df.loc[(df['Name']<= 2)]
y_train=df.Name
X_train=df[df.columns.difference(['Name'])]

#Splitting data to train and test the model
train_X, val_X, train_y, val_y = train_test_split(X_train, y_train, random_state=1)

#Use a linear regression model
lm=linear_model.LinearRegression()
model =lm.fit(X_train,y_train)
disputed_prediction= lm.predict(df_disputed)

#Change all predict values <=1.5 to Hamilton and >1.5 to Madison
disputed_result=[]

for i in range(len(disputed_prediction)):
	
	if(disputed_prediction[i]<=1.5):
		disputed_result.append("Hamilton")
	else:
		disputed_result.append("Madison")

print('Predicted undisputed federalist papers with linear regression:')
print(disputed_result)
# MAE for LR= 0.515
#Predicted 9/12 disputed federalist papers to be Madison


#Train and use a random forest regressor
model= RandomForestRegressor(n_estimators=10,min_samples_split=10,random_state=1)
model.fit(X_train,y_train)
predict_val=model.predict(df_disputed)

#Change all predict values <=1.5 to Hamilton and >1.5 to Madison
disputed_result_rfr=[]

for i in range(len(disputed_prediction)):
	
	if(predict_val[i]<=1.5):
		disputed_result_rfr.append("Hamilton")
	else:
		disputed_result_rfr.append("Madison")

print('Predicted undisputed federalist papers with random forest regressor:')
print(disputed_result_rfr)
#MAE for RFR= 0.088
