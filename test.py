from pathlib import Path
import os
import yaml
from dotenv import load_dotenv

def load_secrets(path: str | Path = "C:\\Users\\b304iax\\Desktop\\ESILV M2\\Machinelearning\\MLOpsProject\\.gitignore\\secret.yaml") -> dict:
    load_dotenv()  # charge .env
    text = Path(path).read_text(encoding="utf-8")
    # Remplace ${OPENWEATHER_API_KEY} par la valeur de l'environnement
    expanded = os.path.expandvars(text)
    return yaml.safe_load(expanded)

secrets = load_secrets()
ow = secrets["openweather"]
print("Base URL:", ow["base_url"])
print("API key ok:", "YES" if ow["api_key"] else "NO")