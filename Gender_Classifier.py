


from sklearn import tree
from sklearn import ensemble
from sklearn import neighbors
from sklearn import neural_network
from sklearn.metrics import accuracy_score


#X = [height, weight, shoe size]
#Training Datset

X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40], [190, 90, 47], [175, 64, 39],[177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]
Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female', 'female', 'male', 'male']



#Test Dataset
_X=[[184,84,44],[198,92,48],[183,83,44],[166,47,36],[170,60,38],[172,64,39],[182,80,42],[180,80,43]]
_Y=['male','male','male','female','female','female','male','male']

#Classification
clf = tree.DecisionTreeClassifier()
clf2 = ensemble.RandomForestClassifier()
clf3 = neighbors.KNeighborsClassifier()
clf4 = neural_network.MLPClassifier()

#Training
clf = clf.fit(X,Y)
clf2 = clf2.fit(X,Y)
clf3 = clf3.fit(X,Y)
clf4 = clf4.fit(X,Y)

#Prediction

prediction = clf.predict(_X)
prediction2 = clf2.predict(_X)
prediction3 = clf3.predict(_X)
prediction4 = clf4.predict(_X)

#Results

print("Decision tree Result:",accuracy_score(_Y, prediction))
print("Random Forest Result:",accuracy_score(_Y, prediction2))
print("KNN Result:",accuracy_score(_Y,prediction3))
print("Neural Network Result:",accuracy_score(_Y,prediction4))









