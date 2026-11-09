
import requests

# IP adresa poslužitelja
ip = '127.0.0.1:5000'


# 1. Zadatak
print('1. Zadatak')

response = requests.get(f'http://{ip}/')
print(response.text)
print(response.status_code)

response = requests.get(f'http://{ip}/login')
print(response.text)
print(response.status_code)


# 2. Zadatak
print('\n2. Zadatak')

json_data = {
    'username': 'PURS',
    'password': '1234'
}

print('Ispravan unos')
response = requests.post(f'http://{ip}/login', data=json_data)
print(response.text)
print(response.status_code)

json_data['username'] = 'pogreska'

print('Neispravan unos')
response = requests.post(f'http://{ip}/login', data=json_data)
print(response.text)
print(response.status_code)


# 3. Zadatak
print('\n3. Zadatak')

json_data = {
    'temperatura': 19
}

response = requests.post(f'http://{ip}/temperatura', json=json_data)
print(response.text)
print(response.status_code)


# 4. Zadatak
print('\n4. Zadatak')

response = requests.get(f'http://{ip}/temperatura')
print(response.json().get('temperatura'))
print(response.status_code)


# 5. Zadatak
print('\n5. Zadatak')

param = {
    'id': 0
}

print('Ispravan unos')
response = requests.delete(f'http://{ip}/temperatura', params=param)
print(response.text)
print(response.status_code)

print('Neispravan unos')
param['id'] = 100

response = requests.delete(f'http://{ip}/temperatura', params=param)
print(response.text)
print(response.status_code)
