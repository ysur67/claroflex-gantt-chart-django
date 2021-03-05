# claroflex-gantt-chart-django
Django BE for Gantt chart

## PostgreSQL

We are using this database. The psycopg2-binary package does not need to be installed everywhere. In most cases, enough

```sh
pip install psycopg2
```

```sh
sudo -u postgres psql postgres
```

```sql
CREATE DATABASE django;
CREATE USER django WITH PASSWORD ‘verysecret’;
GRANT ALL PRIVILEGES ON DATABASE django TO django;
ALTER USER django CREATEDB;
```

## Install the Web server
```sh
mkdir venv
virtualenv --prompt="(venv:claroflex)" ./venv/
source ./venv/bin/activate
git clone https://github.com/Ignat99/claroflex-gantt-chart-django
cd claroflex-gantt-chart-django
pip install -U -r requirements.txt
python ./manage.py makemigrations
python ./manage.py migrate
python ./manage.py test
python ./manage.py runserver 0.0.0.0:8080
```
## Docker

## Some extra info

https://habr.com/ru/post/240463/

https://habr.com/ru/post/242261/

https://github.com/nyergler/effective-django

https://habr.com/ru/company/otus/blog/544880/

```sh
python ./manage.py shell
```
