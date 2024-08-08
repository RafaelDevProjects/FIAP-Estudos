def forca_numero():
    while True:
        try:
            num1 = int(input("Digite 1 - numero: "))
            num2 = int(input("Digite 2 - numero: "))
            print(num1+num2)
            break
        except ValueError:
            print('Voce não digitou um numero')
        except TypeError:
            print("Deu erro de tipo")
        except Exception as e:
            print(e)

lista = ['a','b','c']
def letras():
    while True:
        try:
            print(lista)
            resposta = int(input('Digite o indice de uma letra da lista'))
            print(lista[resposta])
            break
        except IndexError:
            print('erro de index, digite o index correto')
        except ValueError:
            print('Digite um numero!!')

times = {
    'São paulo' : 'hahahahha',
    'Corinthians' : 'top 1',
    "Palmeiras" : 'hdawhdwhahdwhdh',
    "Santos" : "dawdawdwdwadwadwa"
}

def times():
    while True:
        try:
            escolha = input('Escolha um time: \n->')
            print(times[escolha])
        except KeyError:
            frase = '\n'.join(times.keys())
            print(f"Deve ser uma das opções: \n {frase}")
        else:
            break

numeros = {
    1 : ['um','one','uno'],
    2 : ['dois', 'two', 'dos'],
    3 : ['três', 'three', 'tres']
}

indices = {
    "portugues" : 1,
    "ingles" : 2,
    "espanhol" : 3
}

while True:
    try:
        numero = int(input('Qual numero deseja ver?'))
        lingua = input('Em qual lingua deseja ver?')
        print(numeros[lingua])
    except KeyError:
        frase = '\n'.join(indices.keys())
        print(f"Deve ser uma das opções: \n {indices}")
    except ValueError:
        print('Erro de valor, digite ')
