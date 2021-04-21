#!/bin/bash

#gunicorn -w 6 --bind 0.0.0.0:8080 claroflex.wsgi

#pipenv shell
#          --bind unix:/run/gunicorn.sock \

. /home/ubuntu/.local/share/virtualenvs/claroflex-gantt-chart-django-s-NtArIg/bin/activate && sudo /home/ubuntu/.local/share/virtualenvs/claroflex-gantt-chart-django-s-NtArIg/bin/gunicorn \
          --access-logfile - \
          --workers 5 \
          --bind 0.0.0.0:8080 \
          engineers.wsgi:application &
