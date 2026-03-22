from pathlib import Path

from src.data.loaders import load_iris_dataset
from src.features.preprocess import train_valid_split_scale
from src.models.train import train_baseline
from src.models.evaluate import evaluate
from src.models.persistence import save_model


def main():
    """Train baseline Iris classification model and save results."""
    print("Starting MLOpsProject baseline training...")
    
    # Load data
    print("Loading Iris dataset...")
    X, y, target_names = load_iris_dataset()
    print(f"Data loaded: {X.shape[0]} samples, {X.shape[1]} features")
    print(f"Target classes: {target_names}")
    
    # Preprocess
    print("Preprocessing data (scaling and train/validation split)...")
    X_train, X_valid, y_train, y_valid, scaler = train_valid_split_scale(
        X, y, test_size=0.2, random_state=42
    )
    print(f"Train set: {X_train.shape[0]} samples")
    print(f"Validation set: {X_valid.shape[0]} samples")
    
    # Train
    print("Training baseline model...")
    model = train_baseline(X_train, y_train, C=1.0)
    print("Model trained successfully!")
    
    # Evaluate
    print("Evaluating model...")
    metrics = evaluate(model, X_valid, y_valid)
    print(f"Validation Accuracy: {metrics['accuracy']:.4f}")
    
    # Save model
    model_path = Path("models") / "baseline_model.pkl"
    save_model(model, model_path)
    
    print("\nTraining completed successfully!")
    return metrics


if __name__ == "__main__":
    main()
