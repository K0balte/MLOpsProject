from pathlib import Path

import os

import yaml

from dotenv import load_dotenv
 
 
def load_secrets(path: str | Path | None = None) -> dict:

    load_dotenv()  # charge .env
 
    # Si aucun chemin fourni, on cherche secret.yaml à la racine du projet

    if path is None:

        # Cherche d'abord via variable d'environnement (utile pour la CI)

        env_path = os.getenv("SECRET_YAML_PATH")

        if env_path:

            path = Path(env_path)

        else:

            # Par défaut : secret.yaml à la racine du projet

            path = Path(__file__).parent / "secret.yaml"
 
    path = Path(path)
 
    if not path.exists():

        raise FileNotFoundError(

            f"Fichier secret.yaml introuvable : {path}\n"

            "En local : place secret.yaml à la racine du projet.\n"

            "En CI : définis la variable SECRET_YAML_PATH ou utilise des GitHub Secrets."

        )
 
    text = path.read_text(encoding="utf-8")

    # Remplace ${OPENWEATHER_API_KEY} par la valeur de l'environnement

    expanded = os.path.expandvars(text)

    return yaml.safe_load(expanded)
 
 
def test_secrets_loaded():

    """Vérifie que les secrets sont bien chargés (pour pytest)."""

    secrets = load_secrets()

    ow = secrets.get("openweather", {})
 
    assert "base_url" in ow, "Clé 'base_url' manquante dans openweather"

    assert "api_key" in ow, "Clé 'api_key' manquante dans openweather"

    assert ow["api_key"], "api_key est vide !"
 
 
if __name__ == "__main__":

    # Exécution directe du script (hors pytest)

    secrets = load_secrets()

    ow = secrets["openweather"]

    print("Base URL:", ow["base_url"])

    print("API key ok:", "YES" if ow["api_key"] else "NO")
 