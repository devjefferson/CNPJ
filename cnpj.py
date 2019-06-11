import requests, json

cnpj = str(input("Digite seu cnpj"))
url = 'https://receitaws.com.br/v1/cnpj/%s' %(cnpj)
req = requests.get(url)
code = req.status_code

if code == 200:
    html = req.text
    receita = json.loads(html)
    print("Nome da Empresa: %s" %receita['fantasia'])
    print("Atividade Principal: %s" %receita['atividade_principal'][0]['text'])
    try:
        print("Atividade Segundaria: %s" %receita['atividades_secundarias'][0]['text'])
        print("Atividade Segundaria: %s" %receita['atividades_secundarias'][1]['text'])
    except:
        print('Não tem Atividades segundarias')

    print()
    print("Email: %s" % receita['email'])
    print("Telefone: %s" %(receita['telefone']))

    print()
    print("Endereço: %s, Nº%s - Bairro: %s Cep:%s" %(receita['logradouro'], receita['numero'],receita['bairro'],receita['cep']))
    print("Estado: %s - %s" %(receita['municipio'],receita['uf']))

    print()
    print()
    print("Situação Fiscal: %s" %receita['situacao'] )