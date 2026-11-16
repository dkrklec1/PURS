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

if __name__ == '__main__':
    app.run()