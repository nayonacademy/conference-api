#!/bin/bash
source ./venv/bin/activate
for arg in "$@"
do
    if [ "$arg" == "--env" ]
    then
    echo "Env file export"
    export $(cat .env)
    fi
    if [ "$arg" == "--m" ]
    then
        cd ./src/
        echo $PWD
        echo "======== api Db migrate...==========="
        python manage.py makemigrations api
        python manage.py migrate api
        echo "======== jwtauth Db migrate...========"
        python manage.py makemigrations jwtauth
        python manage.py migrate jwtauth
    fi
    if [ "$arg" == "--all" ]
    then
        cd ./src/
        python manage.py makemigrations
        python manage.py migrate
        echo "Db migrate..."
    fi
    if [ "$arg" == "--r" ]
    then
        cd ./src/
        echo "Server Running .. ..."
        python manage.py runserver
    fi
done
