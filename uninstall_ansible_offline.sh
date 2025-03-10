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

echo "🚨 Démarrage du processus de désinstallation..."

if [ -d "$VENV_PATH" ]; then
    echo "🗑️ Désinstallation d'Ansible et pyVmomi via pip..."
    source "$VENV_PATH/bin/activate"
    pip uninstall -y ansible pyvmomi
    deactivate
else
    echo "⚠️ L'environnement virtuel n'existe pas, passage à l'étape suivante."
fi

if [ -d "$VENV_PATH" ]; then
    echo "🗑️ Suppression de l'environnement virtuel..."
    rm -rf "$VENV_PATH"
else
    echo "✅ L'environnement virtuel est déjà supprimé."
fi

echo "📦 Désinstallation de pip, setuptools et wheel..."
for folder in "$PIP_DIR"/*; do
    if [ -d "$folder" ]; then
        echo "📂 Traitement de $folder..."
        dpkg -r "$(basename "$folder")" || echo "⚠️ Erreur lors de la désinstallation de $folder"
    fi
done

echo "📦 Désinstallation de python3.11-venv..."
dpkg -r python3.11-venv || echo "⚠️ Erreur lors de la désinstallation de venv"


echo "✅ Désinstallation terminée avec succès !"
