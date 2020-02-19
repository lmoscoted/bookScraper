# Test Fullstack Tech-K

## Objetivo
---
Desarrollar una aplicacion en Django para que obtenga informacion de internet y esta
pueda ser mostrada en otra aplicacion desarrollada en Vue. Además, de poder ser consultada la informacion por medio de una tabla se podran eliminar registros por medio de una API hecha con Django Rest Framework.
## Instrucciones de uso
---
1. Instalar cliente de [Docker](https://www.docker.com/)
2. Instalar [Docker Compose](https://docs.docker.com/compose/)
3. Levantar el proyecto:
    * `$ cd path/to/project/scraper_techk`
    * `$ docker-compose up`
    * Espere hasta que docker-compose termine de configurar los servicios. Al final, el servicio de Django le indicara que paso las pruebas de sistema. 
    
4. Verificar correcto funcionamiento de la aplicacion Django en [http://localhost:8000/](http://localhost:8000/); para el caso de la aplicacion Vue se debe ingresar a [http://localhost:8080/](http://localhost:8080/)     


## Aplicacion desarrollada
---
Se desarrollo un scraper que permitió obtener información de [la página web](http://books.toscrape.com/index.html), almacenarla en BBDD y luego visualizarla en una interfaz web.

Lo anterior se desarrolló bajo el uso del framework [Django 2.0.13](https://www.djangoproject.com/).

### *Web Scraping*
Se requierió obtener del [sitio web](http://books.toscrape.com/index.html) la siguiente información:

* Listado de categorías (travel, mystery, etc.)
* Información de cada libro:
  * Category
  * Title
  * Thumbnail
  * Price
  * Stock
  * Product Description
  * UPC

Para el diseño del escraper se empleo las librerias [Requests](http://docs.python-requests.org/en/master/) y [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/). Asimismo, se empleo el módulo [Cuncurrent.futures](https://docs.python.org/3/library/concurrent.futures.html), para lanzar el scraper de manera concurrente.

### *Backend*

La información obtenida por el scraper  se almaceno en una BBDD sqlite. Para ello se  modeló la BBDD, creando dos tablas una para categorias y otra para libros. Todo esto empleando migraciones. Ademas para el desarrollo de los modelos se emple el ORM de Django.

### *Frontend*

La información obtenida por el scraper debe se presentó en forma de tabla. Esta aplicación se desarrollo con [Vue.js 2.0](https://vuejs.org/) y para el diseno de la tabla se empleo el componente [Vue-good-table](https://xaksis.github.io/vue-good-table/), asi como las librerias [Axios](https://www.npmjs.com/package/axios) y [Bootstrap-vue](https://bootstrap-vue.js.org/)

Funcionalidades desarrolladas
* Un botón que inicie/ejecute el scraper para obtener los datos del sitio web
* Un listado de Categorías obtenidas por el scrapers.
* Al seleccionar una categoría, la tabla sólo mostrará libros de esa categoría
* La tabla debe tener un buscador por los atributos que posee
* Se debe poder eliminar registros de la tabla que se presente


## Consideraciones
---
* Se requiere que se consulte primero por las categorias para que se puedan obtener los datos de los libros
* No se requiere autenticacion para borrar los registros de la BB.DD
* El sistema almacena los datos en la BB.DD, y estos persisten hasta que se reinicie la aplicacion. Luego que se ejecuta el 
* 

