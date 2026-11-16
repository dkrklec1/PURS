from flask import Flask, request, redirect, url_for, render_template

# Stvaranje Flask aplikacije
app = Flask("PURS Flask aplikacija")

# Globalna lista za spremanje temperatura
temperature = []


# GET zahtjev na putanju /
@app.get('/')
def index():
    return render_template('index.html', temperature=temperature), 200


# GET zahtjev na putanju /login
@app.get('/login')
def login_page():
    return render_template('login.html'), 200


# POST zahtjev na putanju /login
@app.post('/login')
def provjera_prijave():
    username = request.form.get('username')
    password = request.form.get('password')

    if username == 'PURS' and password == '1234':
        return redirect(url_for('index'))
    else:
        return redirect(url_for('login_page'))


# GET zahtjev na putanju /logout
@app.get('/logout')
def logout():
    return redirect(url_for('login_page'))


# POST zahtjev na putanju /temperatura
@app.post('/temperatura')
def post_temperatura():
    podaci = request.json

    if not podaci or 'temperatura' not in podaci:
        return 'Niste upisali ispravan ključ', 404
    else:
        temperature.append(podaci.get('temperatura'))
        return 'Uspješno ste postavili temperaturu', 201


# GET zahtjev na putanju /temperatura
@app.get('/temperatura')
def get_temperatura():
    if not temperature:
        return 'Nema pohranjenih temperatura', 404
    return {'temperatura': temperature[-1]}


# DELETE zahtjev na putanju /temperatura
@app.delete('/temperatura')
def delete_temperatura():
    id_param = request.args.get('id')

    if id_param is None:
        return 'Upisali ste neispravan ključ', 404

    try:
        indeks = int(id_param)
    except ValueError:
        return 'Upisali ste neispravan ključ', 404

    if indeks < 0 or indeks >= len(temperature):
        return 'Upisali ste neispravan ključ', 404

    temperature.pop(indeks)
    return 'Uspješno ste obrisali temperaturu', 202


# Pokretanje aplikacije
if __name__ == '__main__':
    app.run()
