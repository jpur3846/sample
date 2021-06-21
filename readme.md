# Hollab Server:
```
# Setup the pipenv
pipenv install django==3.2 gunicorn --python 3.9
# Start the env.
pipenv shell # if not started.
source /Users/macaccount/.local/share/virtualenvs/sample-iKJKmnvJ/bin/activate # if already existent.

# Create the Django application etc etc.
# Setup models.
# Setup serializers
# Setup views (set permissions)
# Add those views as URL's.
# Register the models in admin.
# Ensure the Db is ignored from the repo.

# Start the webserver with gunicorn. Use NGINX to serve static files.
gunicorn sample.wsgi:application --bind 0.0.0.0:8000

```

Server Architecture:
* Pipenv
* Latest Python, DRF, Django.
* Github hosts the source code
* Code pipeline manages the whole pipeline.
* Code build creates the docker image for us... Or we scan build it ourselves.
* RDS (postgres, secret11)
