import numpy as np

def euclidean_distance(p1,p2):
    return np.sum((p1-p2)**2)

class KNNRegression:
    def __init__(self,k=3):
        self.k = k

    def fit(self,X,y):
        self.points = list(zip(X,y))

    def predict(self,X):
        m = X.shape[0]
        y_pred = []
        for i in range(m):
            sorted_points = sorted(self.points,key=lambda p1: euclidean_distance(p1[0],X[i,:]))
            k_closest_points = sorted_points[:self.k]
            y_pred.append(np.mean(k_closest_points,axis=0)[1])
        return np.array(y_pred)