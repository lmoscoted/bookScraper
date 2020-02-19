# Test Fullstack Tech-K

## Objetivo
---
Desarrollar una aplicacion en Django para que obtenga informacion de internet y esta
pueda ser mostrada en otra aplicacion desarrollada en Vue. La informacion obtenida ademas de poder ser consultada, se podran eliminar registros empleando  una API hecha con Django Rest Framework.
## Instrucciones de uso
---
1. Instalar cliente de [Docker](https://www.docker.com/)
2. Instalar [Docker Compose](https://docs.docker.com/compose/)
3. Levantar el proyecto:
    * `$ cd path/to/project/scraper_techk`
    * `$ docker-compose up`
    * Espere hasta que docker-compose termine de configurar los servicios. Al final, el servicio de Django le indicara que paso las pruebas de sistema. 
    
4. Verificar correcto funcionamiento de la aplicacion Django en [http://localhost:8000/](http://localhost:8000/); para el caso de la aplicacion Vue se debe ingresar a [http://localhost:8080/](http://localhost:8080/) 
   * Sino aparecen las aplicaciones en las direccion indicada cambiar por http://127.0.0.1:8000 y http://127.0.0.1:8080 respectivamente.     


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

La información obtenida por el scraper  se almaceno en una BBDD sqlite. Para ello se  modeló la BBDD, creando dos tablas una para categorias y otra para libros. Todo esto empleando migraciones. Ademas para el desarrollo de los modelos se empleo el ORM de Django.

### *Frontend*

La información obtenida por el scraper  se presentó en forma de tabla. Esta aplicación se desarrollo con [Vue.js 2.0](https://vuejs.org/) y para el diseno de la tabla se empleo el componente [Vue-good-table](https://xaksis.github.io/vue-good-table/), asi como las librerias [Axios](https://www.npmjs.com/package/axios) y [Bootstrap-vue](https://bootstrap-vue.js.org/)

Funcionalidades desarrolladas
* Un botón que inicie/ejecute el scraper para obtener los datos del sitio web
* Un botón que obtiene el listado de Categorías obtenidas por el scrapers.
* Un boton en cada categoria que al seleccionarla, la tabla sólo mostrará libros de esa categoría
* Buscadores para cada uno de  los atributos de la tabla de categorias y libros
* Un boton que  elimina registros ya sea de la tabla que se presente


## Consideraciones
---
* Se supuso que cada vez que se inicie el escraper todos los registros son actualizados en la base de datos. Es decir, que se guardara solo la informacion mas reciente de la pagina.
* No se implemento un sistema de autenticacion para borrar los registros de la BB.DD
* Se diseno la aplicacion frontend de tal manera que se inicie el scraper para poder obtener la informacion mas actualizada en la BD y asi consultarla en las tablas, a traves de un boton para obtener las categorias.
  
