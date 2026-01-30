from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def train_valid_split_scale(X, y, test_size=0.2, random_state=42):
    X_train, X_valid, y_train, y_valid = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_valid_scaled = scaler.transform(X_valid)
    return (X_train_scaled, X_valid_scaled, y_train, y_valid, scaler)