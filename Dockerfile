FROM python:3.9-alpine

# ensure output is displayed in terminal
ENV PYTHONUNBUFFERED = 1

# install postgres
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

# create working dir
WORKDIR /django

# copy requirements
COPY requirement.txt requirement.txt

# install dependancies
RUN pip install -r requirement.txt