# Wordplease

Modificaciones de Wordplease, plataforma de blogging para aprender técnicas avanzadas de Django.

![Matrix_Kung_Fu](http://media.giphy.com/media/AoSMPAREugAAo/giphy.gif)

## Índice

* [Instalación](#toc_2)
* [Arranque de la app](#toc_3)
* [Message Broker y Workers](#toc_4)

## Instalación
Para poner en marcha la plataforma se deberán seguir los siguientes pasos

### Configurar un entorno virtual en Python

https://docs.python.org/3/library/venv.html

### Activar entorno vitual creado

```
source ruta_entorno_virtual/bin/activate

sustituyendo ruta_entorno por la ruta en la que se ha instalado el entorno vitual
```
Por ejemplo, si el entorno virtual se ha instalado en _/Users/dani2/.virtualenvs/practica_Backend_Avanzado_

el comando de activación será _source /Users/dani2/.virtualenvs/practica_Backend_Avanzado/bin/activate_

### Instalar dependencias

Ejecutar el comando que instalará las librerías necesarias en el entorno virtual

```
(env)$ pip install -r requirements.txt
```

### Ejecutar migraciones
Aunque el proyecto se proporciona con una base de datos Sqlite (https://sqlite.org/), puede eliminar el archivo db.sqlite3 y volver a crear la base de datos vacía.
Para ello hay que ejecutar las migraciones 

```
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate
```

### Crear usuario de acceo a la interfaz de administración de la aplicación
Para poder crear datos en las distintas entidades de la aplicación debe crearse primero un superusuario y proporcionar los datos necesarios

```
(env)$ python manage.py createsuperuser
```

## Arranque de la app

### Arrancar el servidor Web
Para arrancar el servidor, hay que *activar el entorno virtual* y luego *arrancar el servidor* de desarrollo de Django.

Desde la carpeta del proyecto y en el terminal, ejecuta:

```
$ source env/bin/activate
(env)$ python manage.py runserver
```

### Acceso a interfaz de administración de la aplicación
Acceder a la URL http://127.0.0.1:8000/admin/login, proporcionando los datos de acceso del usuario creado en el apartado _Crear usuario de acceo a la interfaz de administración de la aplicación_

## Message Broker y Workers
### Kombu (Message Broker o cola de tareas. Kombu transport using the Django database as a message store)
Se instala como app de Django (settings.py)
```python
[...]
INSTALLED_APPS = (
    ...
    'kombu.transport.django',
)

BROKER_URL = 'django://' # Indica que el Broker es Kombu

[...]
```

### Para producción se suele utilizar como brokers [RabbitMQ](https://www.rabbitmq.com) o [Redis](http://redis.io).
Eliminar Kombu de las aplicaciones instaladas en Django y se configura el broker para que sea amqp
```python
[...]
INSTALLED_APPS = (
    ...
    'kombu.transport.django', # Esta línea se elimina
)

BROKER_URL = 'amqp://guest:guest@localhost:5672//' # Utiliza RabbitMQ como cola de tareas (Message broker)

[...]
```


Para arrancar rabbitmq se utiliza el comando
```python
rabbitmq-server (ubicado en la carpeta sbin)
```

Para parar rabbitmq se utiliza el comando
```python
rabbitmqctl stop
```

### Celery (Worker. servicio de procesamiento en background)

Para arrancar Celery, hay que *activar el entorno virtual* y luego *arrancar el Celery*.

Desde la carpeta del proyecto y en el terminal, ejecuta:

```
$ source env/bin/activate
(env)$ celery -A wordplease worker -l info
```

En el archivo settings.py
```python
USE_CELERY = True

#### Decoramos la función que queremos que se ejecute en celery

Para que un código se ejecute en  **[Celery](http://www.celeryproject.org/)**, tan sólo debemos decorar la función con el decorador ```@ shared_task ```. 

```