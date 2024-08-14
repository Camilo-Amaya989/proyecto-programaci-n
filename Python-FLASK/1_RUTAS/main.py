#llamar libreria flask
from flask import Flask

#indicar variable principal

app=Flask(__name__)

#rutas
#raiz
@app.route('/')
def principal():
    return "Esta es la hoja principal"

@app. route('/pagina_2')
def mision():
    return "Esta es la mision de la pagina 2"

@app.route('/pagina_3')
def objetivos():
    return "Esta es la pagina de objetivos"


#ejecuar servidor

if __name__ == '__main__':
    app.run()
