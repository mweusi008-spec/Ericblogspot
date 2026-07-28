#!/usr/bin/env bash
# Render build script for Django
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate --noinput
python manage.py collectstatic --noinput
