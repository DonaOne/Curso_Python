'''Archivo con las funciones necesarias de la aplicación Libro Web'''
import csv

def lee_archivo_csv(archivo:str)->list:
    '''Lee un archivo CSV y devuelve una lista de diccionarios'''
    with open(archivo, "r", encoding='utf8') as f:
        return list(x for x in csv.DictReader(f))
    
def crea_diccionario(lista:list, llave:str)->dict:
    '''Crea un diccionario con la palabra "Llave" como clave y el resto de los datos como valores'''
    return {x[llave].lower(): x for x in lista}

def busca_en_diccionario(diccionario:dict, palabra:str)->list:
    '''Busca la palabra en los valores de un diccionario'''
    lista = []
    palabra = palabra.lower()
    for llave, libro in diccionario.items():
        if palabra in llave.lower():
            lista.append(libro)
    return lista
            
if __name__ == '__main__':
    archivo_csv = 'booklist2000.csv'
    lista_libros = lee_archivo_csv(archivo_csv)
    diccionario_libros = crea_diccionario(lista_libros, 'title')
    resultado = busca_en_diccionario(diccionario_libros, 'dog')
    print(resultado)
    diccionario_autores = crea_diccionario(lista_libros, 'author')
    resultado = busca_en_diccionario(diccionario_autores, 'Sandra')
    print(resultado)
    
