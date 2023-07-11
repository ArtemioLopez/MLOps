from fastapi import FastAPI
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import difflib

# Instanciamos Fast Api
app = FastAPI(title="Proyecto Individual - Artemio Lopez")

# Importamos el Dataset
data = pd.read_csv('Movies.csv', parse_dates=['release_date'], keep_default_na=False)

# Decoradores FastApi

#Funcion Idioma
@app.get('/peliculas_idioma/{idioma}')
def peliculas_idioma(idioma:str):
    #Transformamos el idioma ingresado por el usuario, en dicho idioma pero en minusculas 
    idioma = idioma.lower()
    #Transformamos todos los registros de original language en minusculas 
    data['original_language'] = data['original_language'].str.lower()
    
    if (data['original_language'] == idioma).any():
        #Obtenemos la cantidad de peliculas en el idioma especificado por el usuario
        resultado = data[data['original_language'] == idioma].shape[0]
        return {'idioma':idioma, 'cantidad':resultado}
    else: 
        return {'Resultado': "El idioma ingresado no se encunetra"}
    
#Funcion Duracion Peliculas
@app.get('/peliculas_duracion/{pelicula}')
def peliculas_duracion(pelicula:str):
    #Se imputa la columna #title" para poder crear una mascara posteriormente 
    data.drop_duplicates(subset=['title'], inplace=True)

    #Transformamos el titulo ingresado por el usuario a formato titulo 
    pelicula = pelicula.title()

    #Transformamos todos los registros de la columna titulo a formato "titulo"
    data['title'] = data['title'].str.title()

    #Corroboramos si el titulo ingresado por el usuario existe en el dataset
    if (data['title'] == pelicula).any():
        #Obtenemos la duracion de la pelicula 
        duracion = data[data['title'] == pelicula]['runtime'].values[0]
        #Obtenemos el año en que se estreno la pelicula 
        año = data[data['title'] == pelicula]['release_year'].values[0]
        #Para lo registros con duracion igual 0 retornamos solo el año de estreno
        if (duracion == 0):
            return {'Pelicula': pelicula, 'Duracion': 'La duracion no se encuentra disponible', 'Anio':año}
        else:
            return {'Pelicula': pelicula, 'Duracion':str(duracion), 'Anio':str(año)}
    else:
        return {'Resultado': 'La pelicula ingresada no se encuentra disponible'}

#Funcion Franquicia
@app.get('/franquicia/{franquicia}')
def franquicia(franquicia:str):
    #Transformamos la franquicia que se ingresa por tecla a formato titulo
    franquicia = franquicia.title()

    #Se transforman todos los registros de la columna "belongs to collection" a formato titulo
    data['belongs_to_collection'] = data['belongs_to_collection'].str.title()

    #Corroboramos que la franquicia ingresada por el usuario exista en el dataset
    if (data['belongs_to_collection'].str.contains(franquicia).any()):
        mascara = data[data['belongs_to_collection'].str.contains(franquicia)]
        #Obtenemos las peliculas totales
        total_peliculas = mascara.shape[0]
        #Obtenemos las ganancias totales
        ganancia_total = mascara['revenue'].sum()
        #Obtenemos el promedio de las ganancias para la franquicia
        ganancia_promedio = mascara['revenue'].mean()
        return {'Franquicia': franquicia, 'Peliculas_Totales': str(total_peliculas), 'Ganancias_Totales': str(ganancia_total), 'Ganancias_Promedio':str(ganancia_promedio)}
    else:
        return {'Resultado': 'La franquicia ingresada no es correcta'}
    
#Funcion Peliculas Pais
@app.get('/peliculas_pais/{pais}')
def peliculas_pais(pais:str):
    #Transformamos el pais ingresado por el usuario a formato titulo
    pais = pais.title()

    #Transformamos todos los registros de "production countries" a formato titulo
    data['production_countries'] = data['production_countries'].str.title()

    #Identificamos si el pais ingresado existe en el dataset
    if (data['production_countries'].str.contains(pais).any()):
        mascara = data['production_countries'].str.contains(pais)
        #Obtenemos el total de peliculas que se produjeron en ese pais 
        peliculas_totales = data[mascara].shape[0]
        return {'Pais':pais, 'Peliculas_Totales':peliculas_totales}
    else:
        return {'Resultado': 'El pais ingresado no se encuentra'}

#Funcion Productoras exitosas  
@app.get('/productoras_exitosas/{productora}')
def productoras_exitosas(productora:str):
    #Transformamos la "productora" ingresada por el usuario a formato titulo
    productora = productora.title()

    #Transformamos todas los registros de la columna "production companies" a formato titulo
    data['production_companies'] = data['production_companies'].str.title()

    #Identificamos si la productora ingresada se encuentra en el dataset
    if (data['production_companies'].str.contains(productora).any()):
        mascara = data['production_companies'].str.contains(productora)
        #Obtenemos las peliculas totales de la productora
        peliculas_totales = data[mascara].shape[0]
        #Obtenemos las ganancias Totales
        ganancia_total = data[mascara]['revenue'].sum()
        return {'Productora': productora, 'Peliculas_Totales':str(peliculas_totales), 'Ganancia_Total':str(ganancia_total)}
    else:
        return {'Resultado': 'La productora ingresada no se encuentra'}

#Funcion Get_Director
@app.get('/get_director/{nombre_director}')
def get_director(nombre_director: str):
    
    #Transformamos el director ingresado por el usuario a formato titulo
    nombre_director = nombre_director.title()
    data['Director'] = data['Director'].str.title()

    #buscamos el director en el dataframe
    director = data[data['Director'] == nombre_director]

    #Identifica si existe algun director en el dataframe, si no retorna que no se encuentra resultado.
    if director.empty:
        return {"Resultado": "El director no se encuentra en el dataset."}

    #Se obtiene el retorno total del direcotr
    exito_director = director['return'].sum()

    # Ajustar la columna "release_date" para eliminar la hora
    director['release_date'] = director['release_date'].dt.date

    #Nos quedamos con las columnas utiles para retornar
    peliculas_director = director[['title', 'release_date', 'budget', 'revenue', 'return']]
    peliculas_director['release_date'] = peliculas_director['release_date'].astype(str)

    return {
        "director": nombre_director,
        "retorno_director": exito_director,
        "peliculas_director": peliculas_director.to_dict(orient='records')
        }

#SISTEMA DE RECOMENDACION

#combinamos la informacion de las columnas en una sola. 
df_combinada = data['genres']+ ' ' +data['tagline']+ ' ' +data['cast'] + ' ' +data['Director']

# Instanciamos 
vectorizer = TfidfVectorizer()

# Transformar el texto en una matriz numerica 
vector = vectorizer.fit_transform(df_combinada)

#Limitamos el data set a 5000 registros por cuestiones de rendimiento
#Medimos la similitud entre los conjuntos de datos 
similarity = cosine_similarity(vector[:2800,:])

#Funcion Sistema de Recomendacion
@app.get('/recomendacion/{titulo}')
def recomendacion(titulo:str):
    #Transformamos la columna titulo a formato "titulo"
    lista_titulos = data['title'].str.title()
    #Transformamos el titulo ingresado por el usuario a formato titulo
    titulo = titulo.title()

    if data[data['title'] == titulo].empty:
        return {'Resultado': 'El titulo no se encuentra disponible'}
    
    try:
        #Transfromamos los titulos del dataframe en una lista
        lista_titulos = data['title'].to_list()

        # encontrar las mejores coincidencias cercanas a una cadena de búsqueda en una lista de opciones.
        encontrar_cercanos = difflib.get_close_matches(titulo, lista_titulos)

        #Elegimos la pelicula destacada de entre las peliculas cercanas
        pelicula_relevante = encontrar_cercanos[0]

        #Encontrar el index de la pelicula con el titulo 
        pelicula_index = data[data['title'] == pelicula_relevante].index[0]

        #Almacenamos indice y puntaje de similitud de cada pelicula en relacion con la pelicula de referencia 
        similarity_score = list(enumerate(similarity[pelicula_index]))


        #Ordenamos las peliculas en orden descendente y nos quedamos con las 5 primeras sacando la pelicula ingresada por el usuario 
        lista_relacionadas = sorted(similarity_score, reverse= True,key=lambda x: x[1])[1:6]

        peliculas_recomendadas = []
        for pelicula in lista_relacionadas:
            #obtenemos el index
            index = pelicula[0]
            #identificamos el titulo de la pelicula por su index
            titulo_pelicula = data.iloc[index].title
            #agregamos las peliculas a la lista peliculas_recomendadas
            peliculas_recomendadas.append(titulo_pelicula)

        return {'peliculas_recomendadas': peliculas_recomendadas}
    except IndexError:
        return {'Resultado': 'El titulo ingresado a quedado fuera del dataset por cuestiones de rendimiento'}
    

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    