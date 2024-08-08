'''
for i in range(10):
    print(i)
print()

for char in 'danilo':
    print(char)
print()

for i in range(0,100,2):
    print(i)
print()

for i in range(10,0,-2):
    print(i)
print()
'''

def cinco_notas():
    soma = 0
    for i in range(5):
        nota = int(input(f'Nota {i+1} = '))
        soma += nota
    media = soma/5
    print(media)

def senhas():
    senhaCadastrada = '123'
    usuarioCadastrado = 'RAFA'
    for i in range(3):
        tentativa_senha = input('Digite sua senha: ')
        tentativa_usuario = input('Digite seu usuário: ').upper()
        if tentativa_senha == senhaCadastrada and tentativa_usuario == usuarioCadastrado:
            print('Acesso permitido!')
            break
        else:
            print('Acesso negado!')

def tabuada():

    for i in range(1,11):
        for mult in range(1,11):
            resultado = mult * i
            print(f'{mult} X {i} = {resultado}   ', end='   |   ')
        print()

lista = [1,2,5,2,6,2]
lista.append(4000)

'''
for i in range(len(lista)):
    print(lista[i])

for elem in lista:
    print(elem)


lista.append(4)
'''

def listaDeNotas():
    listaNotas = []
    soma = 0
    notas_maiores_cinco = []
    notas_menores_cinco = []
    for i in range(5):
        listaNotas.append(int(input(f'Digite a nota {i+1}: ')))

    for nota in listaNotas:
        if nota >= 5:
            notas_maiores_cinco.append(nota)
        else:
            notas_menores_cinco.append(nota)

        soma += nota
    media = soma / len(listaNotas)

    print(f'Notas: {listaNotas}')
    print(f'A media de notas é {media}')
    print(f'As notas maiores ou iguais que 5 foram {notas_maiores_cinco} foram {len(notas_maiores_cinco)} notas maiores ou iguais a 5')
    print(f'As notas menores que 5 foram {notas_menores_cinco} foram {len(notas_menores_cinco)} notas menores que 5')

def pesquisar():
    lista = ['joão','jose','rafael', 'danilo', 'Joca', 'joao', 'pedro', 'samira', 'orlando']
    print(lista)
    for i in range(len(lista)):
        if lista[i] == 'danilo':
            print(f'{lista[i]} é top esta na posição {i+1}° da lista')

def listaMaiorNum(lista):
    
    maior = lista[0]
    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i]
    print(lista)
    print(f'O maior mumero {maior}')

lista = [5,4,3,3,130,2]
listaMaiorNum(lista)


#tech with tim expert python
