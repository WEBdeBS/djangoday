#!/bin/bash
. bin/activate
pip -E . install --upgrade gunicorn
cd djangoday
../bin/gunicorn_django -b "0.0.0.0:$PORT" -w 1
