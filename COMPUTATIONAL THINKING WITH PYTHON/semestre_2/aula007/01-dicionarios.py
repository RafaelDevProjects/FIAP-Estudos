import pandas as pd

def verifica_opcoes(lista_opcoes, msg, msg_erro = None):
    resp = input(msg)
    if msg_erro is None:
        msg_erro = 'Valor invalido'
    while resp not in lista_opcoes:
        print(msg_erro)
        for opcao in lista_opcoes:
            print(opcao, end=' ')

        resp = input(f'\n{msg}')
    return resp



def adicionar_carro():
    resp = verifica_opcoes(['sim', 'nao'], 'Deseja cadastrar um novo carro?')
    if resp == 'sim':
        for key in carros.keys():
            resp = input(f'Digite o {key}:')
            carros[key].append(resp)
    return


def meu_index(elem, lista):
    for i in range(len(lista)):
        if lista[i] == elem:
            return i
    return None


'''
dicionario = {
    'Professores': ['Danilo', 'Thiago','Yan', 'luciano', 'caio', 'alexandre', 'andre'],
    'Matérias': ['Python', 'SW', 'Storytelling', 'Edge', 'Matematica', 'web', 'front'],
    'Dias': ['Quarta', 'Quinta', 'Terça', 'Terça', 'sexta', 'sexta','sexta'],
    'Idade': [27, 30, 32, 32, 50, 31, 24]
}

print(pd.DataFrame(dicionario))
print(dicionario['Matérias'][1])
input_professor = input('Qual professor? ')


for i in range(len(dicionario['Professores'])):
    if input_professor == dicionario['Professores'][i]:
        print(f'A materia do professor {input_professor} é {dicionario["Matérias"][i]}')
        break



dic = {"chave": "valor"}

# cria nova chave
dic["nova chave"] = "novo valor"
print(dic)

#look up table (melhor que if e else)
saudacoes = {"oi": "ola", "tchau":"flw"}
resp = input('Diga oi ou olá: ')
'''
'''


dicionario_lados = {
    '3': 'Triangulo',
    '4': 'Quadrado',
    '5': 'Pentagono',
    '6': 'Hexágono'
}
lados = verifica_opcoes(dicionario_lados.keys(), "Diga a qnt de lados:")

print(f'Você escolheu a forma {dicionario_lados[lados]}')
'''

carros = {
    "Modelo": ['up', 'gol', 'kombi', 'celta', 'fusca', 'civic', 'kwid'],
    "Cor": ['preto','vermelho', 'branco', 'azul', 'rosa', 'branco', 'verde'],
    "Preco": [10, 20, 23, 40, 50, 60, 70],
    "v max": [100, 120, 50, 200, 51, 199, 32]
}


carro = verifica_opcoes(carros['Modelo'], "Qual carro sofrera alterações? ")
index_carro = meu_index(carro, carros['Modelo'])
caracteristicas = list(carros.keys())
caracteristica = verifica_opcoes(caracteristicas[1:], "Qual caracteristica irá mudar? ")
novo_valor = input(f'Diga o novo {caracteristica}: ')
carros[caracteristica][index_carro] = novo_valor

print(pd.DataFrame(carros))
