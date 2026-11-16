from flask import Flask

app = Flask("PURS Flask aplikacija")

@app.get('/')
def index():
    return 'Početna stranica'

@app.get('/login')
def login():
    return 'Stranica za prijavu'

if __name__ == '__main__':
    app.run()