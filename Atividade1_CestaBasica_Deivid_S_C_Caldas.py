import os

lista_produtos = [] # Lista para armazenar os produtos

while True: # Loop principal do programa
    os.system('cls') # Limpar a tela
    print("\nMenu de Opções:") # Exibir o menu de opções
    print("1 - Adicionar produto") # Opção para adicionar produto
    print("2 - Listar produtos já adicionados") # Opção para listar produtos
    print("3 - Sair") # Opção para sair do programa
    print("Digite o número da opção desejada: ") # Solicitar a opção do usuário
    print(100 * "_") # Linha de separação
    opcao = input("Digite o número da opção desejada: ").strip().lower() # Ler a opção do usuário e normalizar
    print(" ") # Espaço para melhor visualização

    if opcao == "1": # Se a opção for 1, adicionar produto
        produto = input("Digite o nome do produto: ") # Solicitar o nome do produto
        while True: # Loop para garantir entrada válida do preço do mês anterior
            try: # Tentar converter a entrada para float
                preco_mes_anterior  = float(input("Digite o preço do produto no mês anterior: ")) # Solicitar o preço do mês anterior
                break # Sair do loop se a conversão for bem-sucedida
            except: # Se ocorrer um erro, informar o usuário
                print("Valor inválido. Tente novamente.") # Mensagem de erro
        while True: # Loop para garantir entrada válida do preço do mês atual
            try: # Tentar converter a entrada para float
                preco_mes_atual = float(input("Digite o preço do produto no mês atual: ")) # Solicitar o preço do mês atual
                break # Sair do loop se a conversão for bem-sucedida
            except: # Se ocorrer um erro, informar o usuário
                print("Valor inválido. Tente novamente.") # Mensagem de erro
        if preco_mes_atual > (preco_mes_anterior * 1.1): # Verificar se houve aumento abusivo acima de 10%
            variacao = ((preco_mes_atual - preco_mes_anterior) / preco_mes_anterior) * 100 # Calcular a variação percentual
            status = "Aumento Abusivo" # Definir o status como aumento abusivo
        elif preco_mes_atual > preco_mes_anterior: # Verificar se houve aumento dentro do permitido (até 10%)
            variacao = ((preco_mes_atual - preco_mes_anterior) / preco_mes_anterior) * 100 # Calcular a variação percentual
            status = "Aumento Dentro do Permitido" # Definir o status como aumento dentro do permitido
        elif preco_mes_atual < preco_mes_anterior: # Verificar se houve queda de preço
            variacao = ((preco_mes_atual - preco_mes_anterior) / preco_mes_anterior) * 100 # Calcular a variação percentual
            status = "Queda de Preço" # Definir o status como queda de preço
        else:
            variacao = 0.0 # Definir a variação como 0%
            status = "Estável" # Definir o status como estável
        lista_produtos.append((produto, preco_mes_anterior, preco_mes_atual, variacao, status)) # Adicionar o produto à lista
        print("Produto adicionado com sucesso!") # Confirmar adição do produto
        print(input("Pressione qualquer tecla para continuar...")) # Pausar para o usuário ver a mensagem
    elif opcao == "2": # Se a opção for 2, listar produtos
        if not lista_produtos: # Verificar se a lista está vazia
            print("Nenhum produto adicionado.") # Informar que não há produtos
        else: # Se houver produtos na lista
            for produto, preco_mes_anterior, preco_mes_atual, variacao, status in lista_produtos: # Iterar sobre os produtos na lista
                print(f"Produto: {produto}") # Exibir o nome do produto
                print(f"Preço Mês Anterior: R$ {preco_mes_anterior:.2f}") # Exibir o preço do mês anterior formatado
                print(f"Preço Mês Atual: R$ {preco_mes_atual:.2f}") # Exibir o preço do mês atual formatado
                print(f"Variação: {variacao:.2f}%") # Exibir a variação percentual formatada
                print(f"Status: {status}") # Exibir o status do produto
                print("-" * 30) # Linha de separação entre produtos
        print(input("Pressione qualquer tecla para continuar...")) # Pausar para o usuário ver a lista
    elif opcao == "3": # Se a opção for 3, sair do programa
        print('Obrigado por usar o programa!, Aqui Está Seu Relatório:') # Mensagem de despedida
        if not lista_produtos: # Verificar se a lista está vazia
            print("Nenhum produto adicionado.") # Informar que não há produtos
        else: # Se houver produtos na lista
            for produto, preco_mes_anterior, preco_mes_atual, variacao, status in lista_produtos: # Iterar sobre os produtos na lista
                print(f"Produto: {produto}") # Exibir o nome do produto
                print(f"Preço Mês Anterior: R$ {preco_mes_anterior:.2f}") # Exibir o preço do mês anterior formatado
                print(f"Preço Mês Atual: R$ {preco_mes_atual:.2f}") # Exibir o preço do mês atual formatado
                print(f"Variação: {variacao:.2f}%") # Exibir a variação percentual formatada
                print(f"Status: {status}") # Exibir o status do produto
                print("-" * 30) # Linha de separação entre produtos
        print("Saindo do programa...")
        print(input("Pressione qualquer tecla para continuar...")) # Pausar para o usuário ver a lista
        break # Sair do loop principal
    else: # Se a opção for inválida
        print("Opção inválida. Tente novamente.") # Mensagem de erro
        print(input("Pressione qualquer tecla para continuar...")) # Pausar para o usuário ver a mensagem