from sklearn import tree
from sklearn import ensemble
from sklearn import neighbors
from sklearn import neural_network
from sklearn.metrics import accuracy_score


#X = [height, weight, shoe size]
#Training Datset

X = [[190,80,10],[132,45,6],[189,67,9],[202,100,13],[145,67,6],[154,45,8],[148,89,9],[159,90,7],[188,78,12],[163,80,8]]
Y =['Female','Male','Male','Male','Female','Female','Male','Female','Female','Male']


#Test Dataset
_X=[[184,84,44],[198,92,48],[183,83,44],[166,47,36],[170,60,38],[172,64,39],[182,80,42],[180,80,43]]
_Y=['male','male','male','female','female','female','male','male']

# Classifying using Decision Trees
clf = tree.DecisionTreeClassifier()

clf = clf.fit(X,Y)

prediction = clf.predict(_X)

print("Decision tree Result:",accuracy_score(_Y, prediction))


#Classification using Random Forest

clf2 = ensemble.RandomForestClassifier()

clf2 = clf2.fit(X,Y)
prediction2 = clf2.predict(_X)
print("Random Forest Result:",accuracy_score(_Y, prediction2))

#Classification using KNN

clf3 = neighbors.KNeighborsClassifier()
clf3 = clf3.fit(X,Y)

prediction3 = clf3.predict(_X)
print("KNN Result:",accuracy_score(_Y,prediction3))

#Classification using neural network

clf4 = neural_network.MLPClassifier()
clf4 = clf4.fit(X,Y)

prediction4 = clf4.predict(_X)
print("Neural Network Result:",accuracy_score(_Y,prediction4))

