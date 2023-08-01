Título: Pre-Entrega 3
Autor: Jesús Francisco Alemán Salazar

Objetivo: Presentar una página de compraventa en línea con el nombre de E-Mercado que permita registrar clientes,
vendedores, socios (empresas) y artículos para agregar al catalogo de venta. A su vez, permite consultar el catalogo,
conocer a los vendedores y a los socios.

Instrucciones de prueba:
1.1. Ir a la pestaña "Catalogo de Venta".
1.2. Ir al boton "¡Registra Tus Articulos!".
1.3. Registrar un artículo.
1.4. Volver a la pestaña "Catalogo de Venta" y ver el artículo ahí.

2.1. Ir a la pestaña "Vendedores".
2.2. Ir al boton "¡Registrate como Vendedor!".
2.3. Registrarse como vendedor.
2.4. Volver a la pestaña "Vendedores" y verificar que el dato recibido aparezca ahí.

3.1. Ir a la pestaña "Socios".
3.2. Ir al boton "¡Registra a tu Empresa!".
3.3. Registrar una empresa como socio.
3.4. Volver a la pestaña "Socios" y verificar que el dato recibido aparezca ahí.

4.1. Ir a la pestaña "Clientes".
4.2. Registrarse como cliente.

Datos Adicionales

Información del administrador
    SUPERUSER:admin
    CONTRASEÑA: 01234

Si se va a la pestaña "Administración" se podrán consultar todas las bases de datos con este usuario.
De esta forma se podrá comprobar el registro de clientes.

5.1 ingresar el linc "http://localhost:8000/p3app/barraconsulta/" y consultar resultados en el catálogo.






Comandos en Powershell

Si se desea crear otro usuario administrador:
    python manage.py createsuperuser

Para migración de datos:
    python manage.py makemigrations
    python manage.py migrate

Para correr el servidor:
    python manage.py runserver

Para la presentación de las tablas de datos dentro de la página:

Información de Catalogo:
    python manage.py shell

            from p3app.models import CatalogoVenta

            CatalogoVenta.objects.all()

            exit()


Información de Socios:
    python manage.py shell

            from p3app.models import Socio

            Socio.objects.all()

            exit()


Información de Vendedores:
    python manage.py shell

            from p3app.models import Vendedor

            Vendedor.objects.all()

            exit()