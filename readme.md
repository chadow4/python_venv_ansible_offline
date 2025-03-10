### Configuration et exécution d'Ansible

1. **Activation de l'environnement virtuel**  
   - Si l'environnement `ansible_env` existe, l'activer :  
     ```bash
     source ansible_env/bin/activate
     ```
   - Sinon, créer un nouvel environnement si nécessaire :  
     ```bash
     python3 -m venv "$VENV_PATH"
     ```

2. **Installation des packages locaux**  
   - Installer les dépendances à partir des fichiers `.whl` présents localement :  
     ```bash
     pip install --no-index --find-links=. *.whl
     ```

3. **Exécution du playbook Ansible**  
   - Une fois Ansible installé, exécuter le playbook `test_esxi.yml` :  
     ```bash
     ansible-playbook test_esxi.yml
     ```

