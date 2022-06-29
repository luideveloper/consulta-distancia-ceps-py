import requests

def distanceInfoCeps(x, y): 
    request = requests.get('https://distancep.herokuapp.com/distance/{}/{}'.format(x, y))
    address_data = request.json()

    request1 = requests.get('https://viacep.com.br/ws/{}/json/'.format(x))
    address_data1 = request1.json()

    request2 = requests.get('https://viacep.com.br/ws/{}/json/'.format(y))
    address_data2 = request2.json()

    if 'error' not in address_data and address_data1 and address_data2:
        print('\n✅ DISTÂNCIA:\n') 
        print('• A distância de {} até {} é em média de {} km'.format(address_data1['localidade'], address_data2['localidade'], address_data['distance']))

        print('\nCEP 1️⃣') 
        print('• Endereço: {}'.format(address_data1['logradouro']))
        print('• Complemento: {}'.format(address_data1['complemento']))
        print('• Bairro: {}'.format(address_data1['bairro']))
        print('• Cidade: {}'.format(address_data1['localidade']))
        print('• Estado: {}'.format(address_data1['uf']))
        print('• DDD: {}'.format(address_data1['ddd']))

        print('\nCEP 2️⃣') 
        print('• Endereço: {}'.format(address_data2['logradouro']))
        print('• Complemento: {}'.format(address_data2['complemento']))
        print('• Bairro: {}'.format(address_data2['bairro']))
        print('• Cidade: {}'.format(address_data2['localidade']))
        print('• Estado: {}'.format(address_data2['uf']))
        print('• DDD: {}'.format(address_data2['ddd']))
    else:
        print ('\n❌ {} e {}: são ceps inválidos '.format(x, y))