FROM python:3.13.1-alpine

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "app.py"]
EXPOSE 5000
