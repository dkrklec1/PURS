from flask import Flask, request, make_response, redirect, url_for

app = Flask("Druga vježba")

temperatura = []

@app.get('/')
def home_page():
    return 'Početna stranica'

@app.get('/login')
def login_page():
    response = make_response('Stranica za prijavu')
    return response

@app.post('/login')
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    if username == 'PURS' and password == '1234':
        return redirect(url_for('home_page'))
    else:
        return redirect(url_for('login_page'))

@app.post('/temperatura')
def set_temperature():
    global temperatura
    response = make_response()

    if request.json.get('temperatura') is not None:
        temperatura.append(request.json.get('temperatura'))

        response.data = 'Uspješno ste postavili temperaturu'
        response.status_code = 201
    else:
        response.data = 'Niste upisali ispravan ključ'
        response.status_code = 404
    return response

@app.get('/temperatura')
def get_temperatura():
    json_data = { "temperatura": temperatura[-1] }
    response = make_response(json_data, 200)
    return response

@app.delete('/temperatura')
def delete_temperature():
    global temperatura

    response = make_response()

    if request.args.get('id') is not None and int(request.args.get('id')) < len(temperatura):
        temperatura.pop(int(request.args.get('id')))
        response.data = 'Uspješno ste obrisali temperaturu'
        response.status_code = 202
    else:
        response.data = 'Upisali ste neispravan ključ'
        response.status_code = 404
    return response

if __name__=='__main__':
    app.run(host="0.0.0.0", port=80)
