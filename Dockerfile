FROM python:3.12-alpine

COPY src /app
WORKDIR /app

RUN pip install -r requirements.txt
ENTRYPOINT ["waitress-serve", "app:app"]
EXPOSE 8080
