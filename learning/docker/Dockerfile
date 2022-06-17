# https://stackoverflow.com/questions/48561981/activate-python-virtualenv-in-dockerfile
FROM python:2.7
RUN pip install Flask pymongo
WORKDIR /anchor
ENV FLASK_ENV=development
ENV FLASK_APP=./app/main.py

CMD ["flask", "run", "--host=0.0.0.0"]

# flask --version
#Python 2.7.18
#Flask 1.1.4
#Werkzeug 1.0.1