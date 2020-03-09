FROM python:3.7-buster

WORKDIR /usr/src/app

EXPOSE 8080

COPY . .

RUN pip install -r requirements.txt

CMD ["python3", "-u", "app.py", "-p 8080"]