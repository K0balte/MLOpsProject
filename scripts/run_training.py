import argparse
from src.data.loaders import load_iris_dataset
from src.features.preprocess import train_valid_split_scale
from src.models.train import train_baseline, evaluate

def parse_args():
    parser = argparse.ArgumentParser(description="Baseline training")
    parser.add_argument("--C", type=float, default=1.0, help="Inverse of regularization strength")
    parser.add_argument("--test-size", type=float, default=0.2, help="Validation ratio")
    args, _ = parser.parse_known_args()
    return args

def main():
    args = parse_args()
    X, y, target_names = load_iris_dataset()
    X_tr, X_va, y_tr, y_va, scaler = train_valid_split_scale(X, y, test_size=args.test_size)
    model = train_baseline(X_tr, y_tr, C=args.C)
    metrics = evaluate(model, X_va, y_va)
    print(f"Validation accuracy: {metrics['accuracy']:.3f}")

if __name__ == "__main__":
    main()