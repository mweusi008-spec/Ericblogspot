#!/usr/bin/env bash
# Render build script for Django
python3 -m pip install --upgrade pip
pip install -r requirements.txt
python3 manage.py migrate --noinput
python3 manage.py collectstatic --noinput
