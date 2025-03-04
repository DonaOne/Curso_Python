'''Hola Mundo de flask'''
from flask import Flask
app = Flask(__name__)

@app.route('/')#Home page o raiz o indice
def index():
    return '''
    <html>
        <head>
            <title>Hola Mundo</title>
        </head>
        <body>
            <h1>Hola Mundo</h1>
            <p>Ir a la pagina de <a href="/about">Acerca de</a></p>
        </body>
    </html>
     '''

@app.route('/about')#Acerca de
def about():
    return '''
    <html>
        <head>
            <title>Acerca de</title>
        </head>
        <body>
            <h1>Acerca de</h1>
            <p>Ir a la pagina de <a href="/">Inicio</a></p>
        </body>
    </html>
    return '''
    
if __name__ == '__main__':
    app.run()