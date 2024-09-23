# Actualizar el sistema
sudo apt update

# Instalar Nginx
sudo apt install nginx

# Configurar Nginx
sudo vim /etc/nginx/sites-enabled/connection

# Contenido del archivo de configuración
server {
    listen 80;
    server_name 18.217.48.234;  # Aquí va tu IP pública
    location / {
        proxy_pass http://127.0.0.1:8000;
    }
}

server {
    listen 80;
    server_name 3.129.9.192;  # Otra IP pública si es necesario
    location / {
        proxy_pass http://127.0.0.1:8000;
    }
}

# Guardar el archivo en Vim
# Presiona ESC y luego escribe ":wq" seguido de Enter para guardar y salir

# Reiniciar Nginx
sudo service nginx restart

# Clonar el repositorio
git clone <linkdelrepositorio>

# Actualizar el sistema nuevamente
sudo apt update

# Instalar Python, pip y venv
sudo apt install python3 python3-venv python3-pip

# Crear entorno virtual en EC2
python3 -m venv venv

# Instalar dependencias del archivo requirements.txt
pip install -r requirements.txt

# Ejecutar Uvicorn con nohup para que siga corriendo después de cerrar la terminal
nohup uvicorn main:app --host 0.0.0.0 --port 8000 &

# Acceder a la aplicación (asegúrate de usar http en lugar de https)
http://3.129.9.192/

# Verificar procesos en ejecución
ps aux

# Matar un proceso (sustituye <pid> por el número del proceso)
kill -9 <pid>
