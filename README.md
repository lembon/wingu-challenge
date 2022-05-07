WINGU CHALLENGE

- Instalar PostgreSQL siguiendo las instrucciones para su SO.
https://www.postgresql.org/download/

(Ver nota al final para usar SQLite en vez de PostgreSQL)

- Crear base de datos:
$ sudo -u postgres createdb comunas

- Crear usuario:
$ sudo -u postgres createuser comunas

- Crear una contraseña para el usuario y darle permisos sobre la base de datos:
$ sudo -u postgres psql
postgres=# ALTER USER comunas WITH PASSWORD 'comunas';
postgres=# GRANT ALL PRIVILEGES ON DATABASE comunas TO comunas;

- Instalar la app:
$ git clone git@github.com:lembon/wingu_challenge.git
$ cd wingu_challenge
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ comunas/manage.py migrate

- Iniciar el servidor de desarrollo:
$ comunas/manage.py runserver

- Para ver el listado de reclamos:
http://127.0.0.1:8000/reclamos/

- Para crear un reclamo:
http://127.0.0.1:8000/reclamos/alta

- Para modificar un reclamo:
http://127.0.0.1:8000/reclamos/edicion/<nro_de_reclamo>

- Para eliminar un reclamo:
http://127.0.0.1:8000/reclamos/baja/<nro_de_reclamo>


INSTALACIÓN CON SQLite:
En el módulo comunas/comunas/settings.py reemplazar la contante DATABASES por:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}