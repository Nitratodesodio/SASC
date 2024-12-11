#!/usr/bin/bash
cd /home/ubuntu/SASC/Pw
echo "Tirando cambios de git"
git pull
echo "Activando entorno virtual"
source ./venv/bin/activate
echo "Instalando requerimientos"
pip install -r requirements.txt
echo "Migrando base de datos"
python manage.py migrate
echo "Recolectando archivos estaticos"
python manage.py collectstatic --noinput
echo "Reiniciando servicios"
sudo systemctl restart gunicorn
sudo systemctl restart nginx
