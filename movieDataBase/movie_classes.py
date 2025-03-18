from hashlib import sha256
import csv
from datetime import datetime


class Actor:
    '''Clase actor'''
    def __init__(self, id_estrella, nombre, fecha_nacimiento, ciudad_nacimiento, url_imagen, username):
        self.id_estrella = id_estrella
        self.nombre = nombre
        self.fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%Y-%m-%d')
        self.ciudad_nacimiento = ciudad_nacimiento
        self.url_imagen = url_imagen
        self.username = username
    
    def to_dict(self):
        '''Devuelve un diccionario con los datos del actor'''
        return {'id_estrella': self.id_estrella, 
                'nombre': self.nombre, 
                'fecha_nacimiento': self.fecha_nacimiento.strftime('%Y-%m-%d'), 
                'ciudad_nacimiento': self.ciudad_nacimiento, 
                'url_imagen': self.url_imagen, 
                'username': self.username}    
class Pelicula:
    '''Clase Pelicula'''
    def __init__(self, id_pelicula, titulo_pelcula, fecha_lanzamiento, url_poster):
        '''Constructor de la clase'''
        self.id_pelicula = id_pelicula
        self.titulo_pelicula = titulo_pelcula
        self.fecha_lanzamiento = datetime.strptime(fecha_lanzamiento, '%Y-%m-%d')
        self.url_poster = url_poster
        
    def to_dict(self):
        '''Devuelve un diccionario con los datos de la película'''
        return {'id_pelicula': self.id_pelicula, 
                'titulo_pelicula': self.titulo_pelicula, 
                'fecha_lanzamiento': self.fecha_lanzamiento.strftime('%Y-%m-%d'), 
                'url_poster': self.url_poster
                }

class relacion:
    def __init__(self, id_relacion, id_pelicula, id_estrella):
        '''Constructor de la clase'''
        self.id_relacion = id_relacion
        self.id_pelicula = id_pelicula
        self.id_estrella = id_estrella
        
    def to_dict(self):
        '''Devuelve un diccionario con los datos de la relación'''
        return {'id_relacion': self.id_relacion, 
                'id_pelicula': self.id_pelicula, 
                'id_estrella': self.id_estrella
                }
        
class User:
    '''Clase User: Usuario de la aplicación'''
    def __init__(self, username, nombre_completo, email,password):
        '''Constructor de la clase'''
        self.username = username
        self.nombre_completo = nombre_completo
        self.email = email
        self.password = self.hash_password(password)
        
    def hash_password(self, password):
        '''Devuelve el hash de un password'''
        return sha256(password.encode()).hexdigest()
    
    def to_dict(self):
        '''Devuelve un diccionario con los datos del usuario'''
        return {'username': self.username, 
                'nombre_completo': self.nombre_completo, 
                'email': self.email, 
                'password': self.password
                }
        
class SistemaCine:
    '''Clase SistemaCine: contiene los datos de la aplicación'''
    def __init__(self):
        '''Constructor de la clase'''
        self.actores = []
        self.peliculas = []
        self.relaciones = []
        self.usuarios = []
        self.usuario_actual = None
        
    def carga_csv(self, archivo,clase):
        '''Carga los datos de un archivo CSV'''
        with open(archivo, encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if clase == Actor:
                    self.actores.append(Actor(**row))
                elif clase == Pelicula:
                    self.peliculas.append(Pelicula(**row))
                elif clase == relacion:
                    self.relaciones.append(relacion(**row))
                elif clase == User:
                    self.usuarios.append(User(**row))
                
if __name__ == '__main__':
    sistema = SistemaCine()
    sistema.carga_csv('movies_db -actores.csv', Actor)
    sistema.carga_csv('movies_db -peliculas.csv', Pelicula)
    sistema.carga_csv('movies_db -relaciones.csv', relacion)
    sistema.carga_csv('movies_db -usuarios.csv', User)
    print(sistema.actores)
    print(sistema.peliculas)
    print(sistema.relaciones)
    print(sistema.usuarios)                
    