
from flask import Flask, request, make_response, redirect, url_for, render_template

app = Flask(__name__)

temperatura = []


# GET zahtjev za početnu stranicu
@app.get('/')
def home_page():
    return render_template('index.html'), 200


# GET zahtjev za stranicu za prijavu
@app.get('/login')
def login_page():
    return render_template('login.html'), 200


# POST zahtjev za provjeru korisničkih podataka
@app.post('/login')
def login():

    username = request.form.get('username')
    password = request.form.get('password')

    if username == 'PURS' and password == '1234':
        return redirect(url_for('home_page'))
    else:
        return redirect(url_for('login_page'))


# POST zahtjev za spremanje temperature
@app.post('/temperatura')
def set_temperature():
    global temperatura

    json_data = request.get_json(silent=True) or {}

    response = make_response()

    if json_data.get('temperatura') is not None:
        temperatura.append(json_data.get('temperatura'))

        response.data = 'Uspješno ste postavili temperaturu'
        response.status_code = 201
    else:
        response.data = 'Niste upisali ispravan ključ'
        response.status_code = 404

    return response


# GET zahtjev za dohvaćanje temperature
@app.get('/temperatura')

def get_temperatura():

    if len(temperatura) == 0:
        return make_response(
            {'poruka': 'Nema spremljenih temperatura'},
            404
        )

    json_data = {
        'temperatura': temperatura[-1]
    }

    return make_response(json_data, 200)


# DELETE zahtjev za brisanje temperature
@app.delete('/temperatura')
def delete_temperature():
    global temperatura

    response = make_response()

    try:
        id = int(request.args.get('id', -1))
    except (ValueError, TypeError):
        id = -1

    if 0 <= id < len(temperatura):
        temperatura.pop(id)

        response.data = 'Uspješno ste obrisali temperaturu'
        response.status_code = 202
    else:
        response.data = 'Upisali ste neispravan ključ'
        response.status_code = 404

    return response


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=False,
        use_reloader=False
    )

