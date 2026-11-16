from flask import Flask, request, redirect, url_for

app = Flask("PURS Flask aplikacija")

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

if __name__ == '__main__':
    app.run()