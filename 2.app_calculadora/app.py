#Importamos las clases y métodos
from flask import Flask, render_template, redirect, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/', methods=['Get','POST'])
def aritmetica():
    if request.method =="POST":
        # Valores que recibo del form n1, n2 son pasados
        num1 =float(request.form.get('n1'))
        num2 =float(request.form.get('n2'))

        #Realizamos operaciones aritmeticas
        suma = num1 + num2
        resta = num1 - num2
        multiplicacion = num1 * num2
        division = num1 / num2
        return render_template('index.html', total_suma=suma,
                                             total_resta=resta,
                                             total_multiplicacion=multiplicacion,
                                             total_division=division)
    return render_template('index.html')


@app.route('/divisas', methods=['GET','POST'])
def divisas():
    if request.method == 'POST':
        #Valores que recibo del form peso son pasados
        peso = float(request.form.get('peso'))
        #Realizamos operaciones de cambio de divisas
        dolar=4.172
        euro=4.647
        libra=5.583
        dolarUS=peso*dolar
        Euro=peso*euro
        Libra2=peso*libra

        return render_template('divisas.html',
                               total_dolar=dolarUS,
                               total_euro=Euro,
                               total_libra=Libra2)
    return render_template('divisas.html')

if __name__ == "__main__":
    app.run(debug=True)

