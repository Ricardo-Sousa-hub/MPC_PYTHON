import numpy as np
import pandas as pd
from sklearn import datasets, linear_model
import csv
import pandas as pd
import numpy as np
import array as arr
import os
import pickle as p1

data = pd.read_csv("./Qualidade_vinho_B/winequality-white.csv",sep=";")
evaluation_data=data[1001:]
data_X=evaluation_data.iloc[:,0:11]
data_Y=evaluation_data.iloc[:,11:12]
print(type(evaluation_data))
print(data_X)


loaded_model = p1.load(open('./white-wine_quality_predictor', 'rb'))
print("Coefficients: \n", loaded_model.coef_)

y_pred=loaded_model.predict(data_X)
z_pred=y_pred-data_Y


#for x in z_pred:
#    print(int(x[0]))

print(type(z_pred))
print(type(z_pred["quality"]))
right=0
wrong=0
total=0
for x in z_pred["quality"]:
    z=int(x)
    total=total+1
    if z==0:
        print(int(x),"right")
        right=right+1
    else:
        print(int(x), "wrong")
        wrong=wrong+1
print(len(data),total)
print(right)
print(wrong)
print("accuraccy right/total= ",right/total)
print("accuraccy wrong/total= ",wrong/total)
#for x in evaluation_data:
#    y_pred=loaded_model.predict(x)

#print(y_pred)
#z_pred=y_pred-data_Y
#print(z_pred)
print(type(evaluation_data))
print(len(data_X))


print(loaded_model)