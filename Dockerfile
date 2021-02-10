FROM python:3

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

ENV FLASK_APP run.py

EXPOSE 5000
#ENTRYPOINT ['python3']
#CMD ['run.py']
