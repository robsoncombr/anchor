# https://stackoverflow.com/questions/48561981/activate-python-virtualenv-in-dockerfile
FROM python:2.7
RUN pip install virtualenv
RUN mkdir /anchor
RUN cd /anchor; virtualenv env
RUN cd /anchor; ./env/bin/pip install flask flask-wtf flask-sqlalchemy pymongo
WORKDIR /anchor
#ENV FLASK_ENV=development
#ENV FLASK_APP=./app/main.py

#CMD ["flask", "run", "--host=0.0.0.0"]
#CMD ["/anchor/env/bin/python", "./app/run.py"]
CMD ["/anchor/env/bin/python"]

# flask --version
#Python 2.7.18
#Flask 1.1.4
#Werkzeug 1.0.1