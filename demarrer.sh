#!/bin/bash
echo "================================"
echo " Khadja Rassoul Shop - Demarrage"
echo "================================"

# Créer le venv si absent
if [ ! -d "venv" ]; then
    echo "Creation de l'environnement virtuel..."
    python3 -m venv venv
fi

# Activer
source venv/bin/activate

# Installer
echo "Installation des dependances..."
pip install -r requirements.txt --quiet

# Migrations
echo "Application des migrations..."
python manage.py makemigrations
python manage.py migrate

echo ""
echo "✅ Serveur lancé sur http://127.0.0.1:8000/"
echo "   Admin : http://127.0.0.1:8000/admin/"
echo "   Arrêt : CTRL+C"
echo ""
python manage.py runserver
