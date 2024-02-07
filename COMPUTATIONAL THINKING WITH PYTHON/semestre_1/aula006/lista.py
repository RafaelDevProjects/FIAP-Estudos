
#1

'''nota = int(input('Digite uma nota entre 0 a 10: '))

while nota < 0 or nota > 10:
    print('Tente novamente....')
    nota = int(input('Digite uma nota entre 0 a 10: '))
print(f'Nota valida {nota}')'''

#2




'''nome = input('Digite seu nome: ')
while len(nome) < 3:
    print('Digite uma informação valida')
    nome = input('Digite seu nome: ')


idade= int(input('Qual é a sua idade? '))
while idade <= 0 and idade < 150:
    print('Digite uma informação valida')
    idade= int(input('Qual é a sua idade? '))

salario = int(input('Qual é o seu salario:'))
while salario < 0:
    print('Digite uma informação valida')
    salario = int(input('Qual é o seu salario:'))

sexo = input('Qual é o seu sexo: [f/m]: ')
while sexo != 'm' or sexo != 'f':
    print('Digite uma informação valida')
    sexo = input('Qual é o seu sexo: [f/m]:')


estado_civil = input('Estado Civil [s/c/v/d]')
while not estado_civil == 's' or  estado_civil == 'c' or estado_civil == 'v' or estado_civil == 'd':
    print('Digite uma informação valida')
    estado_civil = int('Estado Civil [s/c/v/d]')
'''

#3

'''pais_A = 80000
pais_B = 200000
ano = 0

while not pais_A == pais_B:
    pais_A = pais_A + (pais_A * 3)/100
    pais_B = pais_B + (pais_B * 1.5)/100
    ano +=1
print(f'A quantidade de anos para o pais B ultrapassar o Pais A {ano}')'''

#4
'''rep=1
soma=0
while rep <= 5:
    num=int(input(f'Digite o {rep} numero: '))
    soma += num
    rep += 1
media = soma/5
print(f'A soma dos numeros é {soma}')
print(f'A media dos numeros é {media}')'''


#5
'''
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
while n1 < n2:
    n1+=1
    print(f'{n1}')'''

#6

'''usuario = input('Usuario: ')
senha = input('Senha:')

while usuario == senha:
    print('[ERRO] insira um nome de usuario senha diferentes')
    usuario = input('Usuario: ')
    senha = input('Senha:')
print('Senha e usuario cadrastrado.')'''



#7
'''tabuada = int(input('Digite um numero :'))
mult = 1
while mult <=10:
    print(f'{tabuada}x{mult}= {mult * tabuada}')
    mult+=1'''



#8




#9

'''rep = 0
pares = 0
impares = 0
while rep < 10:
    num = int(input('Digite um numero inteiro: '))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    rep+=1
print(f'O numero de pares é igual a {pares}')
print(f'O numero de impares é igual a {impares}')'''


#10 ########

'''fat = int(input('Digite um numero: '))
rep=0
while 0 < fat:
    
    fat -= 1'''


#11  #######

'''num = int(input('Digite um numero'))

while not num == 
'''


#12
'''soma = 0
qnt = int(input('Quantas notas você vai escrever? '))
aux = qnt
div = aux
while qnt > 0:
    prova = int(input(f'Digite a nota da prova: '))
    soma += prova
    qnt-=1
media = soma/div
print(f'A media de todas as provas é {media}')'''


#13
'''
ano = 1995
salario = 1000
percentual = 1.5
while ano < 2023:
    salario = salario + (salario * percentual)/100
    percentual += percentual * 2
    ano += 1
print(f'O salario do funcionario é de {salario}')'''

#14

'''num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
ate_25=0
ate_50=0
ate_75= 0
ate_100=0
while num1 < num2:
    if num1 >= 0 and num1 <=25:
        ate_25 += 1
    elif num1 <= 50:
        ate_50 += 1
    elif num1 <= 75:
        ate_75 +=1
    elif num1 <= 100:
        ate_100 += 1
    num1 += 1
print(f'[0-25] = {ate_25}\n[26-50] = {ate_50}\n[51-75] = {ate_75}\n[76-100] = {ate_100}')'''




print(f'{"-="*5}\033[0;31mQuantidade De Votos\033[m{"=-"*5}')

qnt = int(input('Qual é a quantidade de pessoas que irão votar?'))
aux = qnt
total_votos = qnt
jose = 0
joao= 0
pedro = 0
carlos = 0
nulo = 0
voto_branco = 0
print('[1] = jose\n[2] = João\n[3] = Pedro\n[4] = Carlos\n[5] = Voto nulo\n[6] = Voto em Branco')
while not qnt < 1:
    voto = input('Qual é o seu voto?')
    if voto == '1':
        jose += 1
    elif voto == '2':
        joao += 1
    elif voto == '3':
        pedro += 1
    elif voto == '4':
        carlos += 1
    elif voto == '5':
        nulo += 1
    elif voto == '6':
        voto_branco += 1
    qnt -= 1
    print(f'{"-="*10}')
print(f'O voto para os candidatos foi:\nJose = {jose}\nJoão = {joao}\nPedro = {pedro}\nCarlos = {carlos}\n Voto nulo =  {nulo}\nVoto Em Branco = {voto_branco}')
print(f'O percentual de votos nulos sobre o total de votos foi \033[0;31m{nulo/total_votos}\033[m')
print(f'O percentual de votos em branco sobre o total de votos foi \033[0;31m{voto_branco/total_votos}\033[m')







































