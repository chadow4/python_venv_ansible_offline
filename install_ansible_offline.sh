#!/bin/bash

BASE_DIR=$(dirname "$(realpath "$0")")

PIP_DIR="$BASE_DIR/pip_offline"
VENV_DIR="$BASE_DIR/venv_offline"
ANSIBLE_DIR="$BASE_DIR/ansible_offline"
VENV_PATH="$BASE_DIR/ansible_env"

if [ "$EUID" -ne 0 ]; then
    echo "❌ Ce script doit être exécuté avec sudo."
    exit 1
fi

echo "🔍 Vérification des dossiers requis..."
if [ ! -d "$PIP_DIR" ] || [ ! -d "$VENV_DIR" ] || [ ! -d "$ANSIBLE_DIR" ]; then
    echo "❌ Un des dossiers nécessaires n'existe pas ! Vérifiez $PIP_DIR, $VENV_DIR, et $ANSIBLE_DIR."
    exit 1
fi

echo "📦 Installation de pip, setuptools et wheel..."
for folder in "$PIP_DIR"/*; do
    if [ -d "$folder" ]; then
        echo "📂 Traitement de $folder..."
        dpkg -i "$folder"/*.deb || echo "⚠️ Erreur lors de l'installation de $folder"
    fi
done

echo "📦 Installation de venv..."
dpkg -i "$VENV_DIR"/python3.11-venv/*.deb || echo "⚠️ Erreur lors de l'installation de venv"

# === CRÉATION DU VENV ===
if [ ! -d "$VENV_PATH" ]; then
    echo "🔧 Création de l'environnement virtuel..."
    python3 -m venv "$VENV_PATH"
else
    echo "✅ Environnement virtuel déjà existant."
fi

echo "🚀 Activation du venv..."
source "$VENV_PATH/bin/activate"

echo "📦 Installation d'Ansible et pyvmomi..."
cd "$ANSIBLE_DIR" || { echo "❌ Impossible d'accéder à $ANSIBLE_DIR"; exit 1; }
pip install --no-index --find-links=. *.whl || echo "⚠️ Erreur lors de l'installation des .whl"
pip install --no-index --find-links=. pyvmomi-8.0.3.0.1.tar.gz || echo "⚠️ Erreur lors de l'installation de pyvmomi"

echo "🔍 Vérification de l'installation..."

echo "🛠️ Ansible version :"
ansible --version || echo "❌ Ansible n'est pas correctement installé"

echo "🛠️ PyVmomi test :"
python3 -c "import pyVmomi; print('✅ pyVmomi est installé \!')" || echo "❌ Problème avec pyVmomi"

echo "✅ Installation terminée !"
