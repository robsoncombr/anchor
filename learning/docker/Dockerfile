# https://stackoverflow.com/questions/48561981/activate-python-virtualenv-in-dockerfile
FROM python:2.7
RUN pip install Flask
WORKDIR /app
ENV FLASK_APP=main.py
CMD ["flask", "run"]