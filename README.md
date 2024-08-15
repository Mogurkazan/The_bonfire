# The_bonfire

# EJECUTAR CONTENEDOR DOCKER
docker run -d -p 8000:8000 --name bonfire-django-container the-bonfire-blog-django

# VERIFICAR QUE EL CONTENEDOR ESTÁ CORRIENDO
docker ps

# ACCEDER APP
http://localhost:8000

# DETENER CONTENEDOR
docker stop bonfire-django-container

# ELIMINAR CONTENEDOR
docker rm bonfire-django-container
