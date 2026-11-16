from flask import Flask, request, redirect, url_for

app = Flask("PURS Flask aplikacija")

temperature = []

@app.get('/')
def index():
    return 'Početna stranica'

@app.get('/login')
def login_page():
    return 'Stranica za prijavu'

@app.post('/login')
def provjera_prijave():

    podaci = request.json

    if (podaci.get('username') == 'PURS' and
            podaci.get('password') == '1234'):

        return redirect(url_for('index'))

    else:
        return redirect(url_for('login_page'))

@app.post('/temperatura')
def post_temperatura():

    podaci = request.json

    if not podaci or 'temperatura' not in podaci:
        return 'Niste upisali ispravan ključ', 404

    else:
        temperature.append(podaci.get('temperatura'))

        return 'Uspješno ste postavili temperaturu', 201

@app.get('/temperatura')
def get_temperatura():

    return {'temperatura': temperature[-1]}

@app.delete('/temperatura')
def delete_temperatura():

    id = request.args.get('id')

    if id is None:
        return 'Upisali ste neispravan ključ', 404

    try:
        indeks = int(id)
    except ValueError:
        return 'Upisali ste neispravan ključ', 404

    if indeks < 0 or indeks >= len(temperature):
        return 'Upisali ste neispravan ključ', 404

    temperature.pop(indeks)

    return 'Uspješno ste obrisali temperaturu', 202

if __name__ == '__main__':
    app.run()