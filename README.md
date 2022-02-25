# film_site
DJANGO SITE APPLICATION 

All the project dependencies are contained in requirements.txt.

Being this a project that does not need any kind of deploy I decided to don't create any ENV and neither to migrate the SQLite3 Database to PostgresSQL.

To inizialize the project for the first time is necessary to install the dependecies in the file requirements.txt
Is necessary to install all the dependecies with the "pip install" commands in the shell.
ex. "pip install django" or "pip install Pillow".

To launch the server command "python manage.py runserver".

ENTITIES: [
  USER,
  TIPS,
  LIKES,
  SEEN
]

with relational connections contained in models.py.

Paths are contained in urls.py and through include, included films/urls.py


ENDPOINTS:
register/ and login/ to register and log on the site.

home/ contains the dashboard for the admin.

films/ contains the film list.

userPage/ contains the customer profile.

update_user/ and delete_user/ to update and delete user profile.

delete_film/ to delete a single film.

possible to order and sorts the tips table.

ADDITIONAL INFOS:
Created as well some decorators and django HTML components.
