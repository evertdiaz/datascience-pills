from sklearn import tree
from sklearn import svm
from sklearn.linear_model import SGDClassifier
from sklearn.neural_network import MLPClassifier

# dataset: [altura, peso, talla zapato]
X = [[172,76,41], [170,60,42], [176,78,42], [172,85,41], [181,82,43],
	 [185,95,44], [170,60,41], [175,64,40], [181,84,43], [175,76,42],
	 [160,55,38], [165,50,39], [164,52,38], [155,45,36], [160,46,36]]
# labels del dataset
y = ['male', 'male', 'male', 'male', 'male',
 	 'male', 'male', 'male', 'male', 'male',
 	 'female', 'female', 'female', 'female', 'female']
# data de muestra para prediccion
muestra = [[160,50,38]]

# modelo de clasicicacion de arbol de decision
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,y)
prediction_tree = clf.predict(muestra)
print prediction_tree

# utilizando Support Vector Machines
clf2 = svm.SVC()
clf2 = clf2.fit(X,y)
prediction_svc = clf2.predict(muestra)
print prediction_svc

# usando descenso de gradiente estocastico
clf3 = SGDClassifier(loss="hinge", penalty="l2")
clf3 = clf3.fit(X,y)
prediction_sgd = clf3.predict(muestra)
print prediction_sgd

# usando redes neuronales (Multi Layer Perceptron)
clf4 = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5,2), random_state=1)
clf4 = clf4.fit(X,y)
prediction_mlp = clf4.predict(muestra)
print prediction_mlp
