#076

produtos = ('pao', 3, 'leiteee', 3, 'queijo', 5, 'requeijão', 5, 'suco', 3, 'macarrao', 3)

for i in range(0, len(produtos)):
        if (i % 2) == 0:
            print(f'{produtos[i]:.<30}', end='')

        else:
            print(f'..................{produtos[i]:.2f} R$')