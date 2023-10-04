'''nota = int(input('Diga sua nota:'))
while nota < 0 or nota > 10:
    print('Voce deve digitar algo entre 0 e 10')
    nota = int(input('Digite sua nota'))
'''
#Validação
'''    
nome= input('Diga seu nome')

while len(nome) < 3:
    nome= input('Diga seu nome')
    print('Digite um nome com mais de 3 caracteres')
    
idade= int(input('Digite sua idade: '))
while idade < 0 or idade > 150:
    idade= int(input('Digite sua idade: '))
    print('Digite um idade valida')
    
salario= float(input('Diga seu salario: '))
while salario < 0:
    print('Insira algo valido')
    salario= float(input('Diga seu salario: '))
    
    
sexo=input('Diga seu sexo: ')
while not (sexo =='f' or sexo == 'm'):
    print('digite um sexo valida')
    sexo=input('Diga seu sexo: ')
    
estado_civil = input('Qual é o seu estado civil:')
    while not (estado_civil =='s' or estado_civil == 'c' or estado_civil == 'v'):
    estado_civil = input('Qual é o seu estado civil:')'''

#int do input
'''
idade = input('Digite sua idade: ')

while not (idade.isnumeric() and int(idade) >= 0): # comando vê se idade é numerico ou não.
    idade = input('Diga sua idade: ')
idade = int(idade)
print(idade)
'''

'''populaçãoA= 80000
populaçãoB = 200000
anos = 0

while populaçãoA < populaçãoB:
    populaçãoA*= 1.03
    populaçãoB*= 1.015
    anos+=1
print(anos)'''

'''
qnt = 5
i=0
soma = 0
while i < qnt:
    num = input('Digite um numero: ')
    while not num.isnumerc():
        print(f'Voce deve digitar o {i+1} numero corretamente')
        num = input('Digite um numero:')
    num = int(num)
    num = int(num)
    soma += num
    i+=1
media = soma/qnt
print(f'A media ´{media}')
print(f'A soma {soma}')'''
'''
num1 = input('Diga um numero: ')
while not num1.isnumeric():
    print('Tem que ser numero')
    num1 = input('Diga um numero')
    
num2 = input('Diga outro numero: ')
while not num2.isnumeric():
    print('Tem que ser numero')
    num2 = input('Diga outro numero')
while num1 <= num2:
    print(num1)
    num1+=1
while num2 <= num1:
    print(num2)
    num2+=1'''

'''senha = input('Diga sua senha')
usuario = input('Diga seu usuario')
while senha == usuario:
    print("senha não pode ser igual ao usuario")
    senha = input('Diga sua senha')
    usuario = input('Digite o nome de usuario')
'''
'''
num = 1
while num < 10:
    i=1
    print(' ')
    while i <= 10:
        print(f'{num} X {i} = {i*num}')
        i +=1
    num+=1
'''

def fibonnaci(n):
    a = 1; b = 1; i= 2;
    print(a)
    print(b)
    while i < n:
        c = a + b
        print(c)
        a = b
        b = c
        i

def pareseImpares(qnt):
    i = 0
    pares = 0
    impares = 0
    while i < qnt:
        num = input(f'Diga o {i} numero:')
        while not num.isnumeric():
            print('Tem que ser um inteiro!')
            num = input(f"Diga o {i} numero:")
        num = int(num)
        if num%2 == 0:
            pares +=1
        else:
            impares += 1
        i += 1
    print(f'Numero de pares: {pares}')
    print(f'Numero de impares: {impares}')

def fatorial(num):
    while not num.isnumeric() or int(num) <= 0:
        print('Tem que ser um numero positivo!')
        num = input('Digite um numero para calcular o fatorial: ')
    num = int(num)
    i = 0
    fat = 1
    saida = ''
    while i<num:
        i +=1
        print(i)
        fat*=i
        if i!=num:
            saida += f'{i}*'
        else:
            saida +=f'{i} = {fat}'
    print(fat)
    print(saida)

def numerosPrimos(num):
    i = 2
    while not num.isnumeric():
        print('Digite um numero inteiro!!!')
        num = input('Digite um numero: ')
    num = int(num)
    while i < num:
        if num % i == 0:
            print(f'{num} não é primo')
            break
        elif i >= num/2:
            print(f'{num} é primo')
            break
        i+=1










