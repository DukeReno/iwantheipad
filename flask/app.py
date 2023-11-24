from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def nobel():
    return render_template('index.html', nombres=['Ray', 'Rodolfo'], paises=['Mexico','USA','Canada'], categorias=['Economia','Astrología'])