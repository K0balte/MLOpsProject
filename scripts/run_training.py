import argparse
from src.data.loaders import load_iris_dataset
from src.features.preprocess import train_valid_split_scale
from src.models.train import train_baseline
from src.models.evaluate import evaluate
from src.models.persistence import save_model


def parse_args():
    parser = argparse.ArgumentParser(description="Baseline training (Iris)")
    parser.add_argument("--C", type=float, default=1.0, help="Inverse of regularization strength")
    parser.add_argument("--test-size", type=float, default=0.2, help="Validation split ratio")
    parser.add_argument(
        "--model-path",
        type=str,
        default="models/baseline_model.pkl",
        help="Path to save the trained model",
    )
    args, _ = parser.parse_known_args()  # compatible VS Code/Jupyter
    return args


def main():
    args = parse_args()

    # Load and preprocess
    X, y, target_names = load_iris_dataset()
    X_tr, X_va, y_tr, y_va, _ = train_valid_split_scale(X, y, test_size=args.test_size)

    # Train
    model = train_baseline(X_tr, y_tr, C=args.C)

    # Evaluate
    metrics = evaluate(model, X_va, y_va)
    print(f"Validation accuracy: {metrics['accuracy']:.3f}")

    # Save model
    save_model(model, args.model_path)

    return metrics


if __name__ == "__main__":
    main()
