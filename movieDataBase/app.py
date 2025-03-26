'''Programa Principal de movieDataBase'''
from flask import Flask, render_template, request, redirect, url_for
import random
import movie_classes as mc
import os

app = Flask(__name__)
Sistema = mc.SistemaCine()
ruta = 'datos/movies_db - '
actores_csv = ruta + 'actores.csv'
peliculas_csv = ruta +  'peliculas.csv'
relacion_csv = ruta +  'relacion.csv'
users_csv = ruta +  'users.csv'
Sistema.cargar_csv(actores_csv,mc.Actor)
Sistema.cargar_csv(peliculas_csv,mc.Pelicula)
Sistema.cargar_csv(relacion_csv,mc.Relacion)
Sistema.cargar_csv(users_csv,mc.User)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/actores')
def actores():
    '''Muestra la lista de actores'''
    lista_actores = Sistema.actores.values()
    return render_template('actores.html', actores = lista_actores)

@app.route('/peliculas')
def peliculas():
    '''Muestra la lista de peliculas'''
    lista_peliculas = Sistema.peliculas.values()
    return render_template('peliculas.html', peliculas = lista_peliculas)

if __name__ == '__main__':
    app.run(debug=True)
