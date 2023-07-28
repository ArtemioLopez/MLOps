
<img src="https://www.insight.com/content/insight-web/en_US/content-and-resources/2019/02132019-considering-machine-learning/jcr%3Acontent/top-container-width/column_layout_458368662/-column-1/insight_image_898708280.img.jpg/1571246202522.jpg" alt="Texto alternativo" width="1200" height="400">s

# PROYECTO INDIVIDUAL Nº1

# Introducción
En el marco del proyecto de Machine Learning propuesto por el Bootcamp de Soy Henry, asumimos el rol de Data Scientist. Nuestra tarea consistió en llevar a cabo diversas etapas, comenzando por la recolección y preprocesamiento de los datos. A continuación, desarrollamos una API para poner a disposición los datos de la empresa, utilizando el framework FastAPI. Llevamos a cabo el deployment del proyecto y realizamos un análisis exploratorio de los datos.
Además, implementamos un sistema de recomendación como parte del proyecto.


# Detalles del proyecto
En este proyecto, se lleva a cabo un proceso completo de extracción y transformación de datos  a partir de dos archivos CSV que contienen información detallada sobre el mundo cinematográfico. Los archivos incluyen datos como títulos de películas, actores, directores, presupuestos, fechas de estrenos, entre otros.
Una vez completada la transformación de datos, se desarrollan una variedad de funciones útiles para poner los datos a disposición a través de una API REST. Esta API permite acceder y consultar la información cinematográfica de manera sencilla e interactiva, brindando a los usuarios una forma flexible de explorar y obtener datos relevantes según sus necesidades.
Además, se implementa un sistema de recomendación basado en contenido. Este sistema utiliza las características de las películas, como genero, actores directores y reparto, para ofrecer sugerencias personalizadas a los usuarios en función de sus películas favoritas. Esta funcionalidad amplía la experiencia del usuario al proporcionarle nuevas alternativas cinematográficas acorde a sus preferencias. El sistema de recomendación también esta disponible a través de la API, lo que permite a los usuarios obtener recomendaciones de películas directamente desde sus aplicaciones o servicios.

# Proceso de Transformación de Datos
- Se eliminarion ID´S duplicados, se quitaron 3 filas que contenian casi por completo registros vacios, a continuacion se realizo un merge de los datasets [Archivo en Google Drive](https://drive.google.com/drive/folders/1zTB33VXNYYm3n14dIHqllvgNl7Sp5l6c?usp=drive_link). 
- Se cambio el formato de id.
- Se desanidaron las columnas belongs_to_collection, genres, production_companies, spoken_languages.
- Los valores nulos del campo release date se eliminaron. También se transformo el formato de dicha columna con el siguiente patron AAAA-mm-dd.
- Se creo la columna release_yearque contiene los años de lanzamiento de las peliculas.
- Se creo la columna return con el retorno de inversion. Dicha columna se crea a partir de dividir los valores de la columna revenue con budget
- Se eliminaron las columnas que no van a ser utilizadas como, video, imdb_id, adult, original_title, poster_path y homepage
- Desanidamos las columnas crew y cast y nos quedamos con los nombre de director y de actores.
- Exportamos el dataset.

# EDA
- Algunos detalles del análisis exploratorio contemplan, visualización de datos faltantes:

<img src="Imagenes\output.png" alt="Texto alternativo" width="500" height="400">

- También se empleo una nube de palabras, para identificar tópicos interesantes a la hora de desarrollar el sistema de recomendación.

<img src="Imagenes\output2.png" alt="Texto alternativo" width="500" height="400">

# Contenido del Repositorio

- datasets: Contiene los datasets útiles para el ETL(credits.csv, movies_dataset.csv) y para el EDA(Movies_Final.csv)
- Movies.csv: Es el dataset que se empleo para el sistema de recomendación y para desplegar las funciones
- main.py: Contiene las funciones implementadas en la API
- Eda: Contiene el análisis exploratorio de los datos
- Transformaciones: Contiene todas las extracciones y transformaciones necesarias para el desarrollo del proyecto.
- Imagenes: Contiene las imágenes del README
- requirements.txt

# Acceso a la API:
### [Render](https://movie-deploy.onrender.com/docs)

# Informacion de contacto:
artilopez2892@gmail.com




