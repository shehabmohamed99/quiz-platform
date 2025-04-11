FROM python:3.13.1-alpine

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
#RUN docker volume create data_volume
ENTRYPOINT ["python", "app.py"]
EXPOSE 8000
