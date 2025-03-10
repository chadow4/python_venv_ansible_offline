Installation et utilisation d'Ansible en mode offline

1. Installation des dépendances  
   Si vous exécutez la commande suivante :  
   
   sudo ./install_ansible_offline.sh  
   
   Cela installera **pip**, **venv** et **Ansible**.

---

2. Configuration de l'environnement virtuel  

   - Si l'environnement `ansible_env` existe, l'activer :  
     
     source ansible_env/bin/activate  

   - Sinon, créer un nouvel environnement virtuel :  
     
     python3 -m venv "$VENV_PATH"  

---

3. Installation des packages locaux  

   Installer les dépendances à partir des fichiers `.whl` disponibles localement :  
   
   pip install --no-index --find-links=. *.whl  

---

4. Vérification des collections Ansible  

   Avant d'exécuter le playbook, vérifier que la collection **vmware** est bien installée :  
   
   ansible-galaxy collection list | grep vmware  

---

5. Exécution du playbook Ansible  

   Si la collection **vmware** est bien présente, exécuter le playbook :  
   
   ansible-playbook test_esxi.yml  
