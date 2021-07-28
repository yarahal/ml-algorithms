import numpy as np
from tree import TreeNode

class RegressionDecisionTree:
    def __init__(self,depth=5):
        self.depth = depth

    def __criterion(self,j,s,X,y):
        return np.sum((y[X[:,j]<s]-np.mean(y[X[:,j]<s]))**2) + np.sum((y[X[:,j]>=s]-np.mean(y[X[:,j]>=s]))**2)
        
    def __split(self,X_js,y_js,d,current_node):
        m, n = X_js.shape[0], X_js.shape[1]
        j_best, s_best = 0, np.random.choice(np.unique(X[:,0]))
        min_criterion = self.__criterion(j_best,s_best,X_js,y_js)
        for j in range(n):
            for s in np.unique(X[:,j]):
                criterion = self.__criterion(j,s,X_js,y_js)
                if  criterion < min_criterion:
                    j_best, s_best = j, s
                    min_criterion = criterion
        current_node.j = j_best
        current_node.s = s_best
        if(d < self.depth-1):
            if(len(y_js[X_js[:,j_best]<s_best])>0):
                current_node.left = TreeNode(np.mean(y_js[X_js[:,j_best]<s_best]))
                self.__split(X_js[X_js[:,j_best]<s_best],y_js[X_js[:,j_best]<s_best],d+1,current_node.left)
            if(len(y_js[X_js[:,j_best]>=s_best])>0):
                current_node.right = TreeNode(np.mean(y_js[X_js[:,j_best]>=s_best]))
                self.__split(X_js[X_js[:,j_best]>=s_best],y_js[X_js[:,j_best]>=s_best],d+1,current_node.right)
        
    def fit(self,X,y):
        self.tree = TreeNode(np.mean(y))
        self.__split(X,y,0,self.tree)
    
    def predict(self,X):
        m = X.shape[0]
        y_pred = []
        for i in range(m):
            current_node = self.tree
            y = current_node.y
            while(current_node is not None):
                y = current_node.y
                if(X[i,current_node.j]<current_node.s):
                    current_node = current_node.left
                else:
                    current_node = current_node.right
            y_pred.append(y)
        return np.array(y_pred)