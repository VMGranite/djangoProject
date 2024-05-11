**python3 -m pip install django** <br>
_Installs the latest Django release_

**pip install --upgrade pip** <br>

**django-admin startproject meeting_planner** <br>
_starting the project. Make sure you are in your active environment_

!! **python manage.py runserver** <br>
_CD into, and run within the project folder_

**python manage.py startapp app_name_here <br>**
_creates a new app package_

**python manage.py showmigrations <br>**
_shows change to the database_ 

**python manage.py migrate <br>**
_runs pending migrations for the database_

**python manage.py dbshell** <br>
sqlite> **.tables** <br>
_shows tables available_ <br>
sqlite> **select * from django_migrations;** <br>
_shows every migration that has happened. Records state of the database_


!! **python manage.py makemigrations <br>**
_generate migration script (check it)_

**python manage.py sqlmigrate meetings 0001 <br>**
_shows the sql that will be applied, but doesn't actually apply these changes yet_

**python manage.py showmigrates <br>**
_show migrations_

!! **python manage.py migrate <br>**
_this will apply changes to the database to match the models_

 **python manage.py createsuperuser <br>**

 **python manage.py changepassword <user_name>**