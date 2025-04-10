'''
prueba de Beautifulsoup
'''
from bs4 import BeautifulSoup

html = "<html><body><h1>Titulo</h1><p>Texto</p></body></html>"
soup = BeautifulSoup(html, 'html.parser')#Imprime el html en un formato legible
print(soup.prettify()) #imprime el html en un formato legible
print(soup.h1.text)
soup.p.string = "Hola Mundo"
print(soup.prettify())
soup.h1.string = "Hola Mundo de BeautifulSoup"
nueva_etiqueta = soup.new_tag("p")
nueva_etiqueta.string = "Hola soy una nueva etiqueta"
soup.body.append(nueva_etiqueta)
nueva_liga = soup.new_tag("a", href="https://www.google.com")
nueva_liga.string = "Google"
print(soup.prettify())
print("..........................")
print(soup.find_all("h1")) #imprime todas las etiquetas p
print(soup.find_all("p")) #imprime todas las etiquetas h1
parrafos = soup.find_all("p")
lista_parrafos = []
for p in parrafos:
    lista_parrafos.append(p.string)
print(lista_parrafos) #imprime el texto de todas las etiquetas p
print("..........................")