# Activento-PabloMartin-MorenoRuiz


# Descripción de la aplicación 
## Supuesta aplicación final
La aplicación consiste en una red social de eventos y actividades en las que uno se registra como usuario y añade las categorías (tipos de cosas que le interesan) en las que se perfila,puediendo añadir nuevas categorías.

Un usuario podrá crear eventos he invitar a gente o añadirse a un evento que le interese, subir fotos, seguir a gente o empresas.

Habrá una gestión para las empresas  con diversas opciones algo distintas de las de los usuarios normales
 




## Segundo Hito: Integración continua
En está práctica como elegí python se desplegará la infraestructura virtual con virtualenv, instalaremos todos las herramientas necesarias. Y personalmente realizaré algunos test que verifiquen el código.

Al final me he dedicado a aprender Django bastante bien, he creardo la aplicacion hasta crear usuarios, listarlos, crear categorías y verlas...
He creado los test de todas las vistas creadas.

He comentado views.py y test.py con la herramiento pycco he creado un html en el que se ve su contenido

Para ejecutar todos los test juntos he usado python manage.py test que es igual que usar la herramienta nosetest

Y para la integración contigo he usado TRAVIS, me he registrado y le he indicado a que repositorio tiene que aplicarle la integración continua, he compiado el archivo requirementes.txt necesario para que TRAVIS instale la máquina virtual y añadidido el archivo .travis.yml configurandolo apropiadamente y por ultimo al línea siguiente que me comprueba que funciona

[![Build Status](https://travis-ci.org/pmmre/Activento-PabloMartin-MorenoRuiz.svg)](https://travis-ci.org/pmmre/Activento-PabloMartin-MorenoRuiz)

## Tercer hito: Creación y despliegue de una aplicación en un PaaS/SaaS
En esta parte he selecciona heroku y snap-ci para realizar el despliegue. Lo he ralizado exactamente igual que en el ejercicios del tema 3 ( [Ejercicios tema 3](https://github.com/JJ/IV-2015-16/blob/master/ejercicios/PabloMartin-MorenoRuiz/Tema3.md) ) 

[Podemos ver funcionando esta aplicación en heroku](https://mysterious-spire-2156.herokuapp.com/)

En mis ejercicios viene explicado cómo he configurado la apliación para su despliegue, en está simplemente he cambiado la línea 

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Empresas.settings")

por esta otra:

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Activento.settings")

en el archivo wsgi

y algo similar en el Procfile.



## Cuarto hito: Creación de un entorno de pruebas para la aplicación.
En este caso ayudaré con la creación de "jaula" para crear entornos de pruebas para nuesta apliación y ayudare con los scripts de automatización.

## Quinto hito: Diseño del soporte virtual al desarrollo y despliegue de una aplicación
En está parte ayudare a la automatización del despliegue de la apliación.

### Nota importante
Cómo no hemos avanzado mucho en la asignatura y no sabemos exactamente que parte tenemos para dividirnos o que trabajos hay entonces, a priori, esto es a lo que desarrollaría tal y cómo se puso en el proyecto <https://github.com/Activento/Activento>
