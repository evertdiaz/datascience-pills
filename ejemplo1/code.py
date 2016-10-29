from sklearn import tree
#[altura, peso, talla zapato]
X = [[172,76,41], [170,60,42], [176,78,42], [172,85,41], [181,82,43],
	 [185,95,44], [170,60,41], [175,64,40], [181,84,43], [175,76,42],
	 [160,55,38], [165,50,39], [164,52,38], [155,45,36], [160,46,36]]
#labels de cada dato
Y = ['male', 'male', 'male', 'male', 'male',
 	 'male', 'male', 'male', 'male', 'male',
 	 'female', 'female', 'female', 'female', 'female']

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)
prediction = clf.predict([[160,50,38]])

print prediction
