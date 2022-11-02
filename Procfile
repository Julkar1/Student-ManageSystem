release: python manage.py migrate
web: gunicorn djangoMS.wsgi
heroku ps:scale web=1