#exercicio 1 da aula 31
# num = input('Digite um número: ')
#
# if num.isnumeric():
#
#     num = int(num)
#
#     if num % 2 == 0:
#         print(f"Número {num} é par")
#     else:
#         print(f'Número {num} é impar')
# else:
#     print(f'não numérico')

#exercicio 2 da aula 31

# horario = input('Digitem um horário: ')
#
# if horario.isdigit():
#     horario = int(horario)
#     if horario <0 or horario > 23:
#         print('Horario inválido')
#     else:
#         if horario<= 11:
#             print('Bom dia')
#         elif horario <=17:
#             print('Boa tarde')
#         else:
#             print('Boa noite')
# else:
#     print('Insira horario válido')


#exercicio 3 da aula 31

nome = input('Digite um nome: ')
tamanho = len(nome)

if tamanho <= 4:
    print('Seu nome é curto')
elif tamanho <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')