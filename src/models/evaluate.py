from sklearn.metrics import accuracy_score

def evaluate(model, X_valid, y_valid) -> dict:
    y_pred = model.predict(X_valid)
    acc = accuracy_score(y_valid, y_pred)
    return {"accuracy": acc}