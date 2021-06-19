Hollab Server:
# Setup the pipenv
pipenv install django==3.2 gunicorn --python 3.9
# Start the env.
pipenv shell

# Create the Django application etc etc.
# Ensure the Db is ignored from the repo.

# Start the webserver with gunicorn
gunicorn sample.wsgi:application --bind 0.0.0.0:8000



