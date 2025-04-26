# oga-sw-1

Para contruir y ejecutar el contenedor de Docker:

docker build -t ogathon-challenges-api -f Dockerfile .
docker run -d -p 8080:8080 --env ASPNETCORE_HTTP_PORTS=8080 --name ogathon-challenges-api ogathon-challenges-api

Visitar la documentación de Swagger en:
http://localhost:8080/docs