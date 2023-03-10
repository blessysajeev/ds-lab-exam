from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# data=pd.read_csv('car_data.csv')
iris=load_iris()
a=iris.data
b=iris.target
a_train,a_test,b_train,b_test=train_test_split(a,b,random_state=42,test_size=0.32)
knn= KNeighborsClassifier( n_neighbors=9)
knn.fit(a_train,b_train)
c=knn.predict(a_test)
acc=accuracy_score(b_test,c)
print(c)
print(acc)