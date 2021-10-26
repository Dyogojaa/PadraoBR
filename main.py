from acessocep import BuscaEndereco
import requests

cep = "09411010"
cep = BuscaEndereco(cep)

a = cep.acessa_via_cep()
print(dir(a)) #Verifica todos os Metodos do Objeto

bairro, cidade, uf = cep.acessa_via_cep()
print(bairro, cidade, uf)


# r = requests.get('https://viacep.com.br/ws/09411010/json/')
# print(type(r.json()))
