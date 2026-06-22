from flask import Flask

app = Flask(__name__)

@app.route('/')

def home():

    return 'Hola es mi primera conexión de la web con Flask :)'

if __name__ == '__main__':

    app.run(debug=True)