# https://stackoverflow.com/questions/48561981/activate-python-virtualenv-in-dockerfile
FROM python:2.7

RUN virtualenv /ve
RUN /ve/bin/pip install Flask

WORKDIR /ve/app
ENV STATIC_URL /static
ENV STATIC_PATH /ve/app/static

CMD ["/ve/bin/python", "/ve/app/main.py"]