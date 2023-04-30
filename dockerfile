FROM tensorflow/tensorflow:latest

RUN apt-get update && apt-get install -y python3.11
RUN pip install pipenv

WORKDIR /app
VOLUME /app

CMD ["/bin/sh"]