from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def train_baseline(X_train, y_train, C=1.0, max_iter=1000):
    model = LogisticRegression(C=C, max_iter=max_iter, n_jobs=None)
    model.fit(X_train, y_train)
    return model

def evaluate(model, X_valid, y_valid) -> dict:
    y_pred = model.predict(X_valid)
    acc = accuracy_score(y_valid, y_pred)
    return {"accuracy": acc}