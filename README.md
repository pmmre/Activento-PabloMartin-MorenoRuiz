# Activento-PabloMartin-MorenoRuiz   
[![Build Status](https://travis-ci.org/pmmre/Activento-PabloMartin-MorenoRuiz.svg)](https://travis-ci.org/pmmre/Activento-PabloMartin-MorenoRuiz)

## Descripción de la aplicación 
### Supuesta aplicación final
La aplicación consiste en una red social de eventos y actividades en las que uno se registra como usuario y añade las categorías (tipos de cosas que le interesan) en las que se perfila,puediendo añadir nuevas categorías a la lista de categorías globales.

Un usuario podrá tener una lista de amigos agregándolos mandándoles peticiones de amista, está lista de amigos le sirve para poder invitarlos a eventos privados (en los que no son visibles para todos y sólo el administrador podrá añadir más gente), también se podrán seguir empresas y poder ver sus ofertas.

La mayor utilidad de la web se basara en los eventos que en principio podremos crear eventos de varios tipos básicos que el administrador podrá modificar. El administrador podrá indicar si se permiten comentarios, si se permiten listas de usuarios con tope, pudiendo elegir si en la lista se apuntas el resto de la gente que estuvirá en la lista suplente (por ejemplo, una peña de futbol, que cuando fallé uno se incorporé el sigueinte en la lista), o incluso listas con número de asistentes (reserva de un restaurante) o eventos sencillos (como ofertas de las empresas y promociones de comida o deporte,o lo que sea...)

Habrá una gestión para las empresas  con diversas opciones algo distintas de las de los usuarios normales.
 




### Desarrollo de la aplicación en local
En está práctica como elegí python se desplegará la infraestructura virtual con virtualenv, instalaremos todos las herramientas necesarias. Y personalmente realizaré algunos test que verifiquen el código.

Al final me he dedicado a aprender Django bastante bien, he creardo la aplicacion hasta crear usuarios, listarlos, crear categorías y verlas...
He creado los test de todas las vistas creadas.

He comentado views.py y test.py con la herramiento pycco he creado un html en el que se ve su contenido

Para ejecutar todos los test juntos he usado python manage.py test que es igual que usar la herramienta nosetest

Y para la integración contigo he usado TRAVIS, me he registrado y le he indicado a que repositorio tiene que aplicarle la integración continua, he compiado el archivo requirementes.txt necesario para que TRAVIS instale la máquina virtual y añadidido el archivo .travis.yml configurandolo apropiadamente y por ultimo al línea siguiente que me comprueba que funciona

[![Build Status](https://travis-ci.org/pmmre/Activento-PabloMartin-MorenoRuiz.svg)](https://travis-ci.org/pmmre/Activento-PabloMartin-MorenoRuiz)

## Desplieqgue de la aplicación en el PaaS Heroku
En esta parte he selecciona heroku y snap-ci para realizar el despliegue. Lo he ralizado exactamente igual que en los ejercicios del tema 3 ( [Ejercicios tema 3](https://github.com/JJ/IV-2015-16/blob/master/ejercicios/PabloMartin-MorenoRuiz/Tema3.md) ) 

[Podemos ver funcionando esta aplicación en heroku](https://mysterious-spire-2156.herokuapp.com/)

En mis ejercicios viene explicado cómo he configurado la apliación para su despliegue, en está simplemente he cambiado la línea 

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Empresas.settings")

por esta otra:

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Activento.settings")

en el archivo wsgi

y algo similar en el Procfile.



