'''
if, elif, else
'''

nome = input("insira seu nome: ")
idade = input("Insira sua idade: ")
idade_limite = 18

if int(idade) >= idade_limite:
    print('Você pode pegar emprestimo')
else:
    print('Você não pode pegar emprestimo')
