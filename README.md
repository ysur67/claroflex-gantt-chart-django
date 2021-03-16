# claroflex-gantt-chart-django
Django BE for Gantt chart

## Docker
Copy file .env.template to .env in project root directory

Run migrations:
```
docker-compose exec app python manage migrate
```

Create superuser:
```
docker-compose exec app python manage createsuperuser
```

Restart app:
```
docker-compose restart app
``` 

Run docker with custom config
```
docker-compose -f docker-compose.yml - f docker-compose.prod.yml up -d
```

Run docker in dev mode with building:
```
docker-compose up --build
```

Make/update Translations:
```
docker-compose exec app python manage.py makemessages -l es -i 'ganttchart'
```

Make/update Translations for js:
```
docker-compose exec app python manage.py makemessages -d djangojs -l es -i 'ganttchart'
```

Compile Translations after changes:
```
docker-compose exec app python manage.py compilemessages
```

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

## Video
[![Watch the video](https://img.youtube.com/vi/NfsJDPm0X54/0.jpg)](https://youtu.be/NfsJDPm0X54)

## Some extra info

https://habr.com/ru/post/240463/

https://habr.com/ru/post/242261/

https://github.com/nyergler/effective-django

https://habr.com/ru/company/otus/blog/544880/

```sh
python ./manage.py shell
```
