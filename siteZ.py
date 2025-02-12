from flask import Flask, render_template

siteZ = Flask(__name__)

#DIRECIONAMENTO PARA A PAGINA WEB
@siteZ.route('/')
def inicio():
    return render_template('index.html')

if __name__ == '__main__':
    siteZ.run(debug=True)