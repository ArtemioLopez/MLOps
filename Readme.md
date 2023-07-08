
# PROYECTO INDIVIDUAL Nº1


## &nbsp;&nbsp;&nbsp;&nbsp;En este proyecto, se lleva a cabo un proceso completo de extracción y transformación de datos  a partir de un archivo CSV que contiene información detallada sobre el mundo cinematográfico. El archivo incluye datos como títulos de películas, actores, directores, presupuestos, fechas de estrenos,entre otros.

## &nbsp;&nbsp;&nbsp;&nbsp;Una vez completada la transformación de datos, se desarrollan una variedad de funciones útiles para poner los datos a disposición a través de una API REST. Esta API permite acceder y consultar la información cinematográfica de manera sencilla e interactiva, brindando a los usuarios una forma flexible de explorar y obtener datos relevantes según sus necesidades.

## &nbsp;&nbsp;&nbsp;&nbsp;Además, se implementa un sistema de recomendación basado en contenido. Este sistema utiliza las características de las películas, como genero, actores directores y reparto, para ofrecer sugerencias personalizadas a los usuarios en función de sus películas favoritas. Esta funcionalidad amplia la experiencia del usuario al proporcionarle nuevas alternativas cinematográficas acorde a sus preferencias. El sistema de recomendación también esta disponible a través de la API, lo que permite a los usuarios obtener recomendaciones de películas directamente desde sus aplicaciones o servicios.

# Contenido del Repositorio

## . Movies.csv
## . main.py
## . requirements.txt

# Proceso de Transformación de Datos
## &nbsp;&nbsp;&nbsp;&nbsp;Se eliminarion **ID´S** duplicados, se quitaron 3 **filas** que contenian casi por completo registros vacios, a continuacion se realizo un     merge de los datasets [Archivo en Google Drive](https://drive.google.com/drive/folders/1zTB33VXNYYm3n14dIHqllvgNl7Sp5l6c?usp=drive_link). 

## &nbsp;&nbsp;&nbsp;&nbsp;Se cambio el formato de **id**.


## &nbsp;&nbsp;&nbsp;&nbsp;Se desanidaron las columnas **belongs_to_collection**, **genres**, **production_companies**, **spoken_languages**


## &nbsp;&nbsp;&nbsp;&nbsp;Los valores nulos del campo release date se eliminaron.Tambien se transformo el formato de dicha columna con el siguiente patron **AAAA-mm-dd**&Se creo la columna **"release_year"** que contiene los años de lanzamiento de las peliculas.


## &nbsp;&nbsp;&nbsp;&nbsp;Se creo la columna **return** con el retorno de inversion. Dicha columna se crea a partir de dividir los valores de la columna **"revenue"** con **"budget"**


## &nbsp;&nbsp;&nbsp;&nbsp;Se eliminaron las columnas que no van a ser utilizadas como, **video**, **imdb_id**, **adult**, **original_title**, **poster_path** y **homepage**


## &nbsp;&nbsp;&nbsp;&nbsp;Desanidamos las columnas **"crew"** y **"cast"** y nos quedamos con los nombre de director y de actores.


## &nbsp;&nbsp;&nbsp;&nbsp; Exportamos el dataset.

# Acceso a la API:
## [Render](https://movie-deploy.onrender.com/docs)

<br><br>

## Informacion de contacto:
# artilopez2892@gmail.com




