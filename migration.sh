sudo docker-compose run web python manage.py makemigrations
echo '--------------------------'
sudo docker-compose run web python manage.py migrate
