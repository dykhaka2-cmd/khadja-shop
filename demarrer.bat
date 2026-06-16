@echo off
echo ================================
echo  Khadja Rassoul Shop - Demarrage
echo ================================

:: Créer l'environnement virtuel si absent
if not exist "venv" (
    echo Creation de l'environnement virtuel...
    python -m venv venv
)

:: Activer le venv
call venv\Scripts\activate

:: Installer les dépendances
echo Installation des dependances...
pip install -r requirements.txt --quiet

:: Migrations
echo Application des migrations...
python manage.py makemigrations
python manage.py migrate

:: Lancer le serveur
echo.
echo ✅ Serveur lance sur http://127.0.0.1:8000/
echo    Admin : http://127.0.0.1:8000/admin/
echo    Arret : CTRL+C
echo.
python manage.py runserver
