'''
#dicionarios
dic = {"chave" : "valor"}
print(dic["chave"])

#Cria nova chave
dic["nova chave"] = "novo valor"

#sobrescreve uma chave aniga
dic["chave"] = "valor2"
print(dic)

#Faz com que a chave tenha dois valores em uma lista
dic["chave"] = [ dic["chave"] ]
dic["chave"].append('outro valor')
print(dic)
'''

#Criar um dicionáo que tenha a chave par e impar, coloque os numos pares e impares nelas
def dicionario_par_impar():

    dic = {}
    dic["par"] = []
    dic["impar"] = []

    for num in range(20):
        if num % 2 == 0:
            dic["par"].append(num)
        else:
            dic["impar"].append(num)

    print(dic)


def valida_opcoes(dic, msg, msg_erro):
    resposta = input(msg)
    while resposta not in dic:
        print(msg_erro)
        resposta = input(msg)
    return resposta


def equilateros():
    dic = {
        "triangulo": '3',
        "quadrado": '4',
        "pentagono": '5',
        "hexagono": '6'
    }
    forma = valida_opcoes(dic, 'Digite uma forma: ')
    num_lados = dic[forma]
    print(f'A forma {forma} tem {num_lados} lados')








def cadastrar(dic):
    for chave in dic.keys():
        resposta = input(f'Digite o novo {chave}: ')
        dic[chave].append(resposta)


def ler(dic):
    opcoes = dic["sabor"]
    opcao = valida_opcoes(opcoes,"Qual pizza você quer ver? ", '[ERRO]')
    indice = pizzas_index[opcao]
    for key in dic.keys():
        print(f'{key} : {pizzas[key][indice]}')


def deletar(dic):
    opcoes = dic['sabor']
    pizza = valida_opcoes(opcoes,'Digite a pizza que quer deletar: ', '[erro]')
    indice = pizzas_index[pizza]
    for key in dic.keys():
        dic[key].pop(indice)
    print(pizza)
    return


pizzas = {
    "sabor": ['Frango catupiry', '4 queijos', 'Peperoni', 'Calabresa', 'Napolitana'],
    "preco": [50, 70, 60, 55,65],
    "origem": ['Brasil', "Minas gerais", "Italia", "Rio grande do sul", "Napoli"],
    "igredientes": [6, 12, 8, 6, 12],
    "avaliacao": [7, 10, 9, 8, 9]
}

pizzas_index = {pizzas['sabor'][i] : [i] for i in range(len(pizzas['sabor']))}

while True:
    opcao = valida_opcoes(['ler','cadastrar','remover'], 'Voce quer remover, ler ou cadastrar? ')
    
    if opcao == 'ler':
        ler(pizzas)
    elif opcao == 'cadastrar':
        cadastrar(pizzas)
    elif opcao == 'remover':
        deletar(pizzas)