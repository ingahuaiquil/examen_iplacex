from flask import Flask, render_template, request

app = Flask(__name__)

#locahost
@app.route('/')
def index():
    return render_template('index.html')

PRICE_PER_CAN = 9000

#enrutamiento
@app.route('/ejercicio1', methods=['GET', 'POST'])

def ejercicio1():
    result = None
    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        cans = int(request.form['cans'])

        # Calcular el costo total sin descuento
        total_without_discount = PRICE_PER_CAN * cans

        # Determinar el descuento según edad
        if 18 <= age <= 30:
            discount = 0.15
        elif age > 30:
            discount = 0.25
        else:
            discount = 0

        # Calcular el descuento y el total a pagar
        discount_amount = total_without_discount * discount
        total_with_discount = total_without_discount - discount_amount

        # Guardar los resultados en un diccionario
        result = {
            'name': name,
            'total_without_discount': total_without_discount,
            'discount_amount': discount_amount,
            'total_with_discount': total_with_discount
        }
    return render_template('ejercicio1.html', result=result)


users = {
    'juan': 'admin',
    'pepe': 'user'
}

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    message = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Verificar las credenciales
        if username in users and users[username] == password:
            if username == 'juan':
                message = f"Bienvenido administrador {username}"
            elif username == 'pepe':
                message = f"Bienvenido usuario {username}"
        else:
            message = "Usuario o contraseña incorrectos"

    return render_template('ejercicio2.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)