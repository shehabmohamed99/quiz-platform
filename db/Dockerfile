# Use the official MongoDB image from the Docker Hub
FROM mongo:latest

COPY init-mongo.js /docker-entrypoint-initdb.d/
#RUN docker volume create data_volume2

EXPOSE 27017
