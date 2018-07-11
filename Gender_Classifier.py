from sklearn import tree
from sklearn import ensemble
from sklearn import neighbors
from sklearn import neural_network


#X = [height, weight, shoe size]

X = [[190,80,10],[132,45,6],[189,67,9],[202,100,13],[145,67,6],[154,45,8],[148,89,9],[159,90,7],[188,78,12],[163,80,8]]
Y =['Female','Male','Male','Male','Female','Female','Male','Female','Female','Male']

# Classifying using Decision Trees
clf = tree.DecisionTreeClassifier()

clf = clf.fit(X,Y)

prediction = clf.predict([[190,56,8]])

print("Decision tree Result:",prediction)

#Classification using Random Forest

clf2 = ensemble.RandomForestClassifier()

clf2 = clf2.fit(X,Y)
prediction2 = clf2.predict([[190,56,8]])
print("Random Forest Result:",prediction2)

#Classification using KNN

clf3 = neighbors.KNeighborsClassifier()
clf3 = clf3.fit(X,Y)

prediction3 = clf3.predict([[190,56,8]])
print("KNN Result:",prediction3)

#Classification using neural network

clf4 = neural_network.MLPClassifier()
clf4 = clf4.fit(X,Y)

prediction4 = clf4.predict([[190,56,8]])
print("Neural Network Result:",prediction4)

