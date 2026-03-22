import joblib
from pathlib import Path
from typing import Any


def save_model(model: Any, path: str | Path) -> None:
    """
    Save a trained model to disk using joblib.
    
    Args:
        model: The trained model object to save
        path: File path where the model will be saved
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, path)
    print(f"Model saved to {path}")


def load_model(path: str | Path) -> Any:
    """
    Load a trained model from disk.
    
    Args:
        path: File path to the saved model
        
    Returns:
        The loaded model object
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Model file not found: {path}")
    model = joblib.load(path)
    print(f"Model loaded from {path}")
    return model
