'''
funciones auxiliares del juego Ahorcado
'''

def carga_archivo_texto(archivo:str)->list:
    '''Carga un archivo de texto y regresa una lista con las palabras'''
    with open(archivo, 'r', encoding='utf-8') as file:
        oraciones = file.readlines()
    return oraciones

if __name__ == '__main__':
   lista = carga_archivo_texto('./plantillas/plantilla-0.txt')
   for elemento in lista:
       print(elemento)