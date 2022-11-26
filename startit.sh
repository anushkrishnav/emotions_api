apt install libgl1-mesa-glx -y
apt-get install libgomp1 -y
gunicorn --bind=0.0.0.0 --timeout 600 app:app