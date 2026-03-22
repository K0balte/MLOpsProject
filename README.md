# MLOpsProject — Checkpoint 1

## 1) Project Overview

Baseline ML project for multiclass classification (Iris dataset) using scikit-learn with a modular structure. This checkpoint establishes a clean foundation for subsequent checkpoints covering model tracking, serving, and containerization.

- **Task**: Multiclass classification (setosa/versicolor/virginica)
- **Dataset**: Iris (built-in with scikit-learn, no download required)
- **Model**: Logistic Regression baseline
- **Framework**: scikit-learn, Python 3.13+

## 2) Project Structure

```
.
├── src/                           # Main source code
│   ├── data/
│   │   └── loaders.py            # Data loading utilities
│   ├── features/
│   │   └── preprocess.py         # Feature engineering and preprocessing
│   └── models/
│       ├── train.py              # Model training
│       ├── evaluate.py           # Model evaluation
│       └── persistence.py        # Model saving/loading
├── scripts/
│   └── run_training.py           # Training script with arguments
├── data/                          # Data storage
│   ├── raw/                      # Raw data
│   ├── processed/                # Processed data
│   └── derived/                  # Derived features
├── models/                        # Saved models
├── main.py                        # Main entry point
├── test.py                        # Test suite
├── pyproject.toml                 # Project configuration
├── requirements.txt               # Python dependencies
├── Dockerfile                     # Docker container definition
└── .github/workflows/             # CI/CD pipelines
    ├── tests.yml                  # Test automation
    ├── codecheck.yaml             # Code quality checks
    └── prod.yml                   # Production build & push
```

## 3) Installation & Setup

### Prerequisites
- Python 3.13+
- UV package manager (optional, but recommended)
- pip (if not using UV)

### Using UV (Recommended)
```bash
# Install UV if not already installed
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create virtual environment and install dependencies
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -r requirements.txt
```

### Using pip
```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## 4) Running the Project

### Training the Model

**Option 1: Run main.py (Simple)**
```bash
python main.py
```

**Option 2: Run training script (With arguments)**
```bash
# With default parameters
python -m scripts.run_training

# With custom hyperparameters
python -m scripts.run_training --C 0.1 --test-size 0.2
```

**Option 3: Docker**
```bash
docker build -t mlopsproject:latest .
docker run mlopsproject:latest
```

### Expected Output
```
Starting MLOpsProject baseline training...
Loading Iris dataset...
Data loaded: 150 samples, 4 features
Target classes: ['setosa' 'versicolor' 'virginica']
Preprocessing data (scaling and train/validation split)...
Train set: 120 samples
Validation set: 30 samples
Training baseline model...
Model trained successfully!
Evaluating model...
Validation Accuracy: 1.0000
Model saved to models/baseline_model.pkl

Training completed successfully!
```

## 5) Testing

### Run Tests Locally
```bash
pytest -v
```

### Tests Included
- **test_secrets_loaded()**: Verifies that environment variables and secrets are properly loaded
- Additional tests can be added following pytest conventions

### GitHub Actions Automation
Tests automatically run on:
- Pull requests to `main` branch
- Pushes to `main` branch

## 6) Configuration

### Environment Variables
Create a `.env` file in the root directory:
```
OPENWEATHER_API_KEY=your_api_key_here
```

### Secrets Management
The project uses `secret.yaml` for configuration:
```yaml
openweather:
  api_key: "${OPENWEATHER_API_KEY}"
  base_url: "https://api.openweathermap.org/data/2.5"
  defaults:
    city: "Paris"
    units: "metric"
    lang: "fr"
```

## 7) Model Persistence

Models are saved using joblib for efficient serialization:

```python
from src.models.persistence import save_model, load_model

# Save a trained model
save_model(model, "models/my_model.pkl")

# Load a saved model
model = load_model("models/my_model.pkl")
```

## 8) CI/CD Pipeline

### Workflows Configured
1. **tests.yml**: Runs pytest on code changes
2. **codecheck.yaml**: Performs linting with flake8
3. **prod.yml**: Builds and pushes Docker image to DockerHub

### Manual Triggers
Push to appropriate branch to trigger workflows:
- `main` → runs tests, code checks, and Docker build

## 9) Dependencies

See `pyproject.toml` and `requirements.txt`:
- **numpy**: Numerical computing
- **pandas**: Data manipulation
- **scikit-learn**: ML algorithms
- **python-dotenv**: Environment variable management
- **pyyaml**: YAML configuration
- **requests**: HTTP library
- **joblib**: Model serialization

## 10) Next Steps (Checkpoint 2+)

Planned enhancements:
- [ ] MLflow integration for experiment tracking
- [ ] REST API for model serving (FastAPI/Flask)
- [ ] Model versioning and registry
- [ ] Advanced error handling and logging
- [ ] Extended evaluation metrics (precision, recall, F1-score)
- [ ] Cross-validation and hyperparameter tuning
- [ ] Database integration for predictions

## 11) Contributing

1. Create a feature branch (`git checkout -b feature/my-feature`)
2. Make changes and commit (`git commit -m 'Add feature'`)
3. Push to branch (`git push origin feature/my-feature`)
4. Tests automatically run via GitHub Actions
5. Submit a pull request for review

## 12) Troubleshooting

### Module Import Errors
Ensure you're in the correct directory and the virtual environment is activated:
```bash
which python  # Should show path to .venv/bin/python
```

### Missing OPENWEATHER_API_KEY
The secret.yaml file needs the API key:
```bash
# Export the key or set it in .env file
export OPENWEATHER_API_KEY="your_key"
```

### Docker Build Failures
Ensure Docker is installed and requirements.txt is present:
```bash
docker build --no-cache -t mlopsproject:latest .
```

## 13) License & Contact

**Course**: ESILV M2 - Machine Learning  
**Year**: 2026  
**Project Type**: MLOps Checkpoint 1
