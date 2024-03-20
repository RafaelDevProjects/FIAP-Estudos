import pandas as pd
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

lados = input('Diga a qnt de lados: ')

dicionario_lados = {
    '3': 'Triangulo',
    '4': 'Quadrado',
    '5': 'Pentagono',
    '6': 'Hexágono'
}
while lados not in dicionario_lados.keys():
    print('Digite um valor valido')
    lados = input('Diga a qnt de lados: ')


print(f'Você escolheu a forma {dicionario_lados[lados]}')
