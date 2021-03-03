# claroflex-gantt-chart-django
Django BE for Gantt chart

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
https://habr.com/ru/company/otus/blog/544880/

```sh
python ./manage.py shell
```
