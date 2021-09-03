# pull official base image
FROM python:3.8
# set work directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
# не добовляются файла .pyc
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install dependencies
RUN pip install --upgrade pip
COPY . /usr/src/app/
RUN pip install -r requirements.txt
