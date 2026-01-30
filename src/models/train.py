from sklearn.linear_model import LogisticRegression

def train_baseline(X_train, y_train, C=1.0, max_iter=1000):
    model = LogisticRegression(C=C, max_iter=max_iter, n_jobs=None)
    model.fit(X_train, y_train)
    return model