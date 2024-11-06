# Criar lista de cadastro com nome e peso, informar quantas cadastradas e qual o mais pesado e mais leve

# Inicializa listas e variáveis
pessoas = []  # Lista para armazenar as informações de cada pessoa
infos = []  # Lista temporária para armazenar o nome e peso de uma pessoa
resp = ' '  # Variável para controlar a continuidade do cadastro
mai = men = 0  # Variáveis para armazenar o maior e menor peso
cont = 0  # Contador de pessoas cadastradas

while True:
    # Solicita o nome e peso da pessoa
    nome = input('Nome: ')
    peso = float(input('Peso: '))

    # Adiciona as informações à lista temporária
    infos.append(nome)
    infos.append(peso)

    # Adiciona a lista temporária à lista de pessoas
    pessoas.append(infos[:])

    # Atualiza o maior e menor peso
    if cont == 0:  # Se for a primeira entrada
        mai = men = peso  # Inicializa mai e men com o peso atual
    else:
        if peso > mai:  # Verifica se o peso atual é maior que o maior peso registrado
            mai = peso
        elif peso < men:  # Verifica se o peso atual é menor que o menor peso registrado
            men = peso

    # Limpa a lista temporária para a próxima entrada
    infos.clear()

    # Pergunta se o usuário deseja continuar cadastrando
    resp = input('Continuar? [S/N] ').strip().upper()
    if resp == 'N':
        break

    cont += 1  # Incrementa o contador de pessoas cadastradas

# Exibe as informações cadastradas
print(pessoas)
print(f'O maior peso é {mai} e o menor peso é {men}')
print(f'Total de pessoas cadastradas: {cont + 1}')  # Exibe o total de pessoas cadastradas
