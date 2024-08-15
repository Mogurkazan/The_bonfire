# Usa una imagen base oficial de Python
FROM python:3.9-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Instala las dependencias del sistema
RUN apt-get update && apt-get install -y \
    libpq-dev gcc

# Copia el archivo requirements.txt
COPY requirements.txt /app/

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de la aplicación
COPY . /app/

# Exponer el puerto 8000 (puedes cambiarlo si estás usando otro puerto en tu proyecto)
EXPOSE 8000

# Comando para ejecutar las migraciones y luego correr el servidor de Django
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
