'''7-	Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual número ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50
'''

'''num = 1
while num <= 10:
    i = 1
    while i <= 10:
        print(f'{num} X {i} = {num*i}')
        i += 1
    num += 1


for i in range(11):
    for num in range(11):
        print(f'{str(i)} X {str(num)} = {num*i} ')
    print()

'''
'''
profs = ['Danilo', 'Thiafo','Andre', 'Luciano', 'Yan', 'Caio', 'Alexandre Russi']
materias = ['Python(top), "SWGTX', "Storytelling",'Diff pro solv', 'Web', 'Edge', 'Front' ]

for i in range(len(profs)):
    if profs[i] == 'Yan':
        print(f'Achei! | Possição: {i} | Materia: {materias[i]}')
        break
'''
'''
#Achar o maior numero de uma lista
#printar o carro mais caro

lista_de_numeros = [10, 11, 7, 6, 8, 12, 50]
lista_de_carros = ['camaro', 'uno', 'fusca', 'celta', 'up', 'mobi', 'sandero']
maior = lista_de_numeros[0]
for num in range(len(lista_de_numeros)):
    if lista_de_numeros[num] > maior:
        indice = num
print(f'Maior numero da lista: {lista_de_numeros[indice]} | Carro: {lista_de_carros[indice]}')

'''


def inverte_lista(lista):
    for i in range(len(lista) // 2):
        aux = lista[i]
        lista[i] = lista[len(lista) - i - 1]
        lista[len(lista) - i - 1] = aux
    return lista


def par_ou_nao(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


def quantidade_de_pares(lista):
    qnt = 0
    for num in lista:
        if par_ou_nao(num):
            qnt += 1
    return qnt


def maior_numero_lista(lista):
    maior = lista[0]
    for num in range(len(lista)):
        if lista[num] > maior:
            maior = lista[num]
    return maior


def main():
    lista = ['a', 'b', 'c', 'd']
    print(lista)
    print(f'Lista invertida: {inverte_lista(lista)}')
    print()
    lista_numeros = [1, 4, 5, 7, 8, 2, 3]
    print(lista_numeros)
    print(f'Quantidade de partes na lista: {quantidade_de_pares(lista_numeros)}')
    print(f'O maior numero da lista: {maior_numero_lista(lista_numeros)}')



if __name__ == '__main__':
    main()
