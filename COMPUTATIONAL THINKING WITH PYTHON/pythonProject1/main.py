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


letra = input('Digite uma letra:').upper()

if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
    print(f'A letra {letra} é uma vogal')
else:
    print(f'A letra {letra} é uma consoante')





