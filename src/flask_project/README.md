# python

- cd src
- cd flask_project
- pip install -r requirements.txt
- python run.py
- flask run

# docker

- cd src/flask_project/
- sudo docker build -t flask_project:v0.1 .
- sudo docker run -p 5000:5000 flask_project:v0.1

# docker-compose

- cd src
- cd flask_project
- docker-compose up