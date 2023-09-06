
#Digitar o salario para ver de quanto é a oliquota e printar o salario final.
'''salario = float(input('Diga seu salario:'))
if salario <= 2112.01:
    oliquota= 0
elif salario <=  2.826:
    aliquota= 7.5
elif salario <= 3.751:
    aliquota= 15
elif salario <= 4.664:
    aliquota= 22.5
elif salario > 4.664:
    aliquota= 27.5
desconto = aliquota
salario_final = salario - desconto
print(f'Voce recebera R$ {salario_final}')'''



# Digitar uma letra para ver se é consoante ou vogal.
'''print('=-=-=-=-=-= lETRA UMA VOGAL OU CONSOANTE =-=-=-=-=-=')
letra = input('Digite uma letra:').upper()

if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
    print(f'A letra {letra} é uma vogal')
else:
    print(f'A letra {letra} é uma consoante')'''

#Maior valor entra dois numeros
'''print('=-=-=-=-=-= MAIOR ENTRE DOIS VALORES =-=-=-=-=-=')
num1 = float(input('Diga um valor : '))
num2 = float(input('Diga outro valor : '))
if num1>num2:
    print(f"{num1} > {num2}")
else:
    print(f"{num2} > {num1}")
'''


#Pode ou não votar
'''print('=-=-=-=-=-= Pode ou não votar =-=-=-=-=-=')
ano = int(input('Diga seu ano de nascimento : '))
if ano <= 2007:
    print("Pode votar!!")
else:
    print("nÃ£o pode votar!")
'''



#Tentativa de colocar senha, acesso negado e acesso permitido
'''print('=-=-=-=-=-= Tentativa de senha =-=-=-=-=-=')
senha= '1234'
tentativa = input('diga sua senha: ')
if senha == tentativa:
    print('ACESSO PERMITIDO')
else:
    print('ACESSO NEGADO')'''


#Maças, quanto custam 1 duzia e pelo menos 12
'''
print('=-=-=-=-=-= PREÇO DE MAÇA =-=-=-=-=-=')
quant = int(input('diga a quantidade de maças que você vai levar: '))
preço = 0.25
if quant < 12:
    preço= 0.3
valor = preço * quant
print(F'Vai custar R${valor}')
'''


#Digite 3 valores inteiros e escreva em ordem eles.

print('=-=-=-=-=-= 3 VALORES INTEIROS EM ORDEM CRESCENTE =-=-=-=-=-=')
n1 = int(input('Digite o um valor:'))
n2 = int(input('Digite o um valor:'))
n3 = int(input('Digite o um valor: '))

'''
A logica nesse côdigo:
primeira: Testar se o n1 é o maior entre os numeros n2 e n3. Se for passa para o proximo if

segunda: Testar e ver qual é o maior numero e usar uma variavel auxiliar, para a variavel n1 ser sempre o maior numero

terceira: Depois de achar o maior e coloca-lo na variavel n1, testar o n2 e n3 para saber qual é maior entre eles.
'''

'''
if n1 > n2 and n1 > n3:
    pass
elif n2 > n3:
    aux = n1
    n1 = n2
    n2 = aux
else:
    aux = n1
    n1 = n3
    n3 = aux
if n2>n3:
    print(n3,n2,n1)
else:
    print(n2,n3,n1)
'''


#Altura e sexo de uma pessoa, calculo de peso ideal.
'''
print('=-=-=-=-=-= PESO IDEAL =-=-=-=-=-=')
altura = float(input("Diga sua altura : "))
sx = input("Diga seu sexo (F/M): ").upper()
if sx == 'F':
    peso = 62.1*altura - 44.7
else:
    peso = 72.7*altura - 58
print(f"Seu peso ideal é {peso:.2f}")
'''

#Triangulo, Quadrado ou Pentagono
'''print('=-=-=-=-=-= POLIGONOS =-=-=-=-=-=')
lados= int(input('Diga a quantidade de lados: '))
if lados < 3:
    print('Não é um poligono')
elif lados == 3:
    print('Triangulo')
elif lados == 4:
    print('Quadrado')
elif lados == 5:
    print('Pentagono')
else:
    print('Poligono não identificado')'''

# 3 VALORES INTEIROS E O MAIOR DELES
'''
print('=-=-=-=-=-= MAIOR ENTRE 3 NUMEROS =-=-=-=-=-=')
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))

if n1 > n2 and n1 > n3:
    print(f'{n1} é maior')
elif n2 > n3:
    print(f'{n2} é o maior')
else:
    print(f'{n3} é o maior')
'''













