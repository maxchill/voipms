import requests

def api(api_username, api_password, method, params = None):
    url = 'https://voip.ms/api/v1/rest.php'
    if params == None:
        params = {}
    params.update({
        'api_username': api_username,
        'api_password': api_password,
        'method': method,
    })
    response = requests.get(url, params = params)
    if response.ok:
        return response.json()

def getSMS():
      {'date': '2015-01-27 02:25:22',
                 'did': '9145741328',
                    'id': '1130177',
                       'message': 'Hey T',
                          'type': '1',
                             'contact': '4158464482'},
