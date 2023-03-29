import numpy as np
import pandas as pd
from sklearn import datasets, linear_model
import csv
import pandas as pd
import numpy as np
import array as arr
import os
import pickle as p1

data_x=input("introduza valores do wine\n")
data=data_x.split(";")
print(data)
fmap_data = map(float, data)
print(fmap_data)
flist_data = list(fmap_data)
print(flist_data)

data1 = pd.read_csv("./Qualidade_vinho_B/winequality-white.csv",sep=";")

data2=data1.iloc[:0,:11]
data_preparation=pd.DataFrame([flist_data],columns=list(data2))
#data_preparation.to_csv("../out.csv",index=False)
#data_evaluation = pd.read_csv("../out.csv",sep=",")

out=data2
for x in out:
    print(x,data_preparation[x].values)
loaded_model = p1.load(open('./white-wine_quality_predictor', 'rb'))
y_pred=loaded_model.predict(data_preparation)

print("wine quality",int(y_pred))

"""
data_preparation.to_csv("../out.csv")
data_evaluation = pd.read_csv("../out.csv",sep=";")
loaded_model = pickle.load(open('../wine-red_quality_predictor', 'rb'))
print("Coefficients: \n", loaded_model.coef_)
y_pred=loaded_model.predict(data_evaluation)

y_pred=loaded_model.predict(data_evaluation)


data_X=data_evaluation.iloc[:,0:11]
y_pred1=loaded_model.predict(data_X)
#with open("../temporary.csv", 'w+', newline='\n') as myfile:
#    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#    wr.writerows(data_preparation)
#print(type(data_preparation))
#print(data_preparation[:1])
#print(type(data_evaluation))
#print(data_evaluation)
#data_evaluation2=data_evaluation.squeeze(axis=0)
#print(type(data_evaluation2))
#print(data_evaluation2[1:])
#data_evaluation.iloc[0,:]
#y_pred=loaded_model.predict(df)

#z_pred=y_pred[0]
#print(y_pred)
"""