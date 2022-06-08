perguntas = {
    'Pergunta 1': {
        'Pergunta': 'Quanto é 2X2?',
        'Respostas': {
            'a': '1',
            'b': '4',
            'c': '2',
        },
        'resposta_certa': 'b',

        },
    },
    'Pergunta 2': {
        'Pergunta': 'Quanto é 4X4?',
        'Respostas': {
            'a': '1',
            'b': '4',
            'c': '16',
        },
        'resposta_certa': 'c',

        },
    }
}

for p_key, p_value in perguntas.items():
    print(f'{p_key}: {p_value["Pergunta"]}')

    for r_key, r_value in p_value['Respostas'].items():
        print(f'[{r_key}]: {r_value}')
