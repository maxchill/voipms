def api(api_username, api_password, method, params = None):
    url = 'https://voip.ms/api/v1/rest.php'
    if params == None:
        params = {}
    params.update({
        'api_username': api_username,
        'api_password': api_password,
        'method': method,
    })
    retutrn requests.get(url, params = params)
