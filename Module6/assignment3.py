#
# This code is intentionally missing!
# Read the directions on the course lab page!
#
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.cross_validation import train_test_split
from sklearn.svm import SVC
x = pd.read_csv('C:/Users/IBM_ADMIN/Desktop/DATmaster/Module6/Datasets/parkinsons.data')
del x['name']
y = x['status']
del x['status']
print(x.head())
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.3, random_state = 7)
svc = SVC()
model = svc.fit(x_train, y_train)
print(model.score(x_test, y_test))

#model = preprocessing.Normalizer().fit(x_train)
#model = preprocessing.MaxAbsScaler().fit(x_train)
#model = preprocessing.MinMaxScaler().fit(x_train)
#model = preprocessing.KernelCenterer().fit(x_train)
model = preprocessing.StandardScaler().fit(x_train)
x_train = model.transform(x_train)
x_test = model.transform(x_test)

#from sklearn.decomposition import PCA
#pca = PCA(n_components = 7)
#xpca = pca.fit(x_train)
#x_train = xpca.transform(x_train)
#x_test = xpca.transform(x_test)
best_score = 0
from sklearn.manifold import Isomap
for k in range(2, 6):
    for l in range(4, 7):
        iso = Isomap(n_neighbors = k, n_components = l)
        xiso = iso.fit(x_train)
        x_train = xiso.transform(x_train)
        x_test = xiso.transform(x_test)
        for c in np.arange(start = 0.05, stop = 2.05, step = 0.05):
            for gamma in np.arange(start = 0.001, stop = 0.101, step = 0.001):
                svc = SVC(C = c, gamma = gamma)
                model = svc.fit(x_train, y_train)
                score = model.score(x_test, y_test)
                if (score>best_score):
                    best_score = score




print(best_score)