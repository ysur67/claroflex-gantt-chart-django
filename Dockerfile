FROM python:3.8.5
ENV PYTHONUNBUFFERED 1
RUN apt-get update
RUN apt-get install -y locales locales-all gettext
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
COPY ./docker-entrypoint.sh /

# Install the application server.
RUN pip install "gunicorn==20.0.4"

ENTRYPOINT ["/docker-entrypoint.sh"]
