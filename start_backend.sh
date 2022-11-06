#!/usr/bin/env bash
sleep 10
source ../../../../envs/BlogEnv/bin/activate
python manage.py runserver --settings=blog5_backend.dev_settings


#Миграции
#python manage.py makemigrations blog --settings=blog5_backend.dev_settings
#python manage.py migrate blog --settings=blog5_backend.dev_settings