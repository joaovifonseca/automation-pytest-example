import requests

url = 'https://viacep.com.br/ws/'


def test_should_call_api_with_cep():
    cep = '08257060'
    url_with_cep = url + cep + '/json/'
    response = requests.get(url_with_cep)

    if response.status_code == 200:
        print(response.text)
        assert response.json()['logradouro'] == 'Rua Coração Brasileiro' and \
               response.json()['cep'].replace('-', '') == cep
    else:
        assert False


def test_should_call_api_with_invalid_cep():
    cep = '000000'
    url_with_cep = url + cep + '/json/'
    response = requests.get(url_with_cep)

    if response.status_code == 400:
        print(response.text)
        assert True
    else:
        assert False
