import time
from typing import Dict, Any

# A função de simulação de busca foi removida, 
# pois agora os dados serão inseridos manualmente.

# --- LÓGICA DE COMPARAÇÃO ---

def comparar_precos(item_desejado: str, resultados: Dict[str, Dict[str, Any]]):
    """
    Compara os preços obtidos e determina a melhor oferta.
    
    Args:
        item_desejado (str): O nome do item pesquisado.
        resultados (dict): Dicionário com os preços de cada plataforma.
    """
    if not resultados:
        print(f"\nNão foram encontrados resultados para '{item_desejado}'.")
        return

    melhor_oferta = None
    
    # Itera sobre os resultados para encontrar o menor preço
    for plataforma_chave, dados_oferta in resultados.items():
        preco = dados_oferta["preco"]
        
        # Se for a primeira oferta ou se o preço for menor que a melhor oferta atual
        if melhor_oferta is None or preco < melhor_oferta["preco"]:
            melhor_oferta = {
                "plataforma_chave": plataforma_chave, # Chave completa (Plataforma + Vendedor)
                "preco": preco,
                "link": dados_oferta["link"],
                "vendedor": dados_oferta["vendedor"]
            }

    # --- APRESENTAÇÃO DE RESULTADOS ---
    
    print("-" * 50)
    print(f"|  RESULTADO DA COTAÇÃO PARA: {item_desejado.upper()}")
    print("-" * 50)

    # Lista todas as ofertas
    print("\nTODAS AS OFERTAS ENCONTRADAS (Ordenadas por preço):")
    # Ordena as ofertas pela chave 'preco'
    ofertas_ordenadas = sorted(resultados.items(), key=lambda x: x[1]['preco'])
    
    for plataforma_chave, dados in ofertas_ordenadas:
        # Usa a chave completa para mostrar a origem
        print(f"  > {plataforma_chave.ljust(25)}: R$ {dados['preco']:.2f}")

    # Exibe a melhor oferta
    print("\n" + "=" * 50)
    if melhor_oferta:
        print("  !!! ONDE COMPENSA COMPRAR !!!")
        print(f"  Melhor Oferta (Plataforma + Vendedor): {melhor_oferta['plataforma_chave']}")
        print(f"  Preço Final: R$ {melhor_oferta['preco']:.2f}")
        print(f"  Vendedor: {melhor_oferta['vendedor']}")
        print(f"  Link: {melhor_oferta['link']}")
    print("=" * 50)


# --- FUNÇÃO PRINCIPAL COM ENTRADA MANUAL ---

def main():
    """
    Função principal do aplicativo de comparação de preços com entrada manual.
    """
    print("Bem-vindo ao Comparador de Preços de Peças (Modo Manual)")
    print("---------------------------------------------------------")
    
    while True:
        # Pede o nome da peça ao usuário
        item = input("\nDigite o nome da peça que deseja cotar (ou 'sair' para encerrar): ").strip()
        
        if item.lower() == 'sair':
            print("Obrigado por usar o comparador! Até mais.")
            break
        
        if not item:
            continue

        dados_cotacao = {}
        print("\n--- INSERÇÃO MANUAL DE COTAÇÕES ---")
        print("Digite os dados de cada oferta. Digite 'fim' no nome da plataforma para terminar.")
        
        contador = 1
        while True:
            # 1. Pede a plataforma
            plataforma = input(f"\n[{contador}] Nome da Plataforma (ex: Shopee, Kabum, ou 'fim'): ").strip()
            if plataforma.lower() == 'fim':
                break
            
            # 2. Pede o preço
            try:
                preco_str = input(f"[{contador}] Preço (R$): ").strip().replace(',', '.')
                preco = float(preco_str)
            except ValueError:
                print("ERRO: Preço inválido. Por favor, digite um número (ex: 3799.50).")
                continue # Volta ao início do loop para tentar novamente
            
            # 3. Pede o vendedor e link (opcional)
            vendedor = input(f"[{contador}] Nome do Vendedor (Opcional): ").strip()
            link = input(f"[{contador}] Link da Oferta (Opcional): ").strip()
            
            # Cria uma chave única para a oferta (Plataforma + Vendedor)
            key = f"{plataforma} ({vendedor})" if vendedor else plataforma
            
            # Armazena os dados
            dados_cotacao[key] = {
                "preco": preco,
                "link": link or "N/A", # Se o link for vazio, usa "N/A"
                "vendedor": vendedor or "Desconhecido" # Se o vendedor for vazio, usa "Desconhecido"
            }
            contador += 1
            
        # 2. Executa a lógica de comparação
        if dados_cotacao:
            comparar_precos(item, dados_cotacao)
        else:
            print("Nenhuma cotação adicionada. Voltando ao menu principal.")

if __name__ == "__main__":
    main()
