import requests


data = {
    'title': 'Привет'
}
respons = requests.patch("https://jsonplaceholder.typicode.com/todos/5",  data=data)
print(respons.jnos())
