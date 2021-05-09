PGY-3121 Prueba 2


En este repositorio se desarrollo una WEB API Rest.

Los framework usados durante el desarrollo fueron 'Django' para la creación del backend y 'djangorestframework' para la creacion de la API Rest.

Panel control
http://nriverv.pythonanywhere.com/admin/login/?next=/admin/

username: Duoc
password: 1234

URLS APIS:

API que valida si los datos ingresados ya estan en uso.

POST http://nriverv.pythonanywhere.com/api/v1/validation/all/

formato de la data (body) esperada {"username": username, "email": email, "password1": password1, "password2" password2}

API que realiza la creación del usuario.

POST http://nriverv.pythonanywhere.com/api/v1/signup/

formato de la data (body) esperada {"username": username, "email": email, "password": password}

API que realiza el inicio de sesion.

POST http://nriverv.pythonanywhere.com/api/v1/signin/

formato de la data (body) esperada {"username": username, "password": password}

API que realiza el cierre de sesion.

header {"Authorization": "Token <token obtenido al iniciar sesion o registrarse>"}

POST http://nriverv.pythonanywhere.com/api/v1/signout/all/
