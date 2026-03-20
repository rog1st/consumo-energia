# Projeto Ag5 DS1
def obter_valor_numerico(pergunta):
    """Garante que o usuário insira um número válido, aceitando ponto ou vírgula."""
    while True:
        entrada = input(pergunta).replace(',', '.') # Converte vírgula em ponto
        try:
            return float(entrada)
        except ValueError:
            print("❌ Erro: Digite apenas números (ex: 1500 ou 0.85).")

def calcular_consumo():
    print("\n⚡ --- Calculadora de Consumo de Energia --- ⚡")
    
    nome_aparelho = input("Nome do aparelho: ")
    potencia = obter_valor_numerico("Potência do aparelho (em Watts): ")
    horas_dia = obter_valor_numerico("Horas de uso por dia: ")
    dias_mes = int(obter_valor_numerico("Dias de uso no mês: "))
    valor_kwh = obter_valor_numerico("Valor do kWh (ex: 0.85): ")

    # Cálculos
    consumo_kwh = (potencia * horas_dia * dias_mes) / 1000
    custo_total = consumo_kwh * valor_kwh

    # Exibição
    print(f"\n✅ Resultado para: {nome_aparelho}")
    print(f"------------------------------------")
    print(f"Consumo mensal: {consumo_kwh:.2f} kWh")
    print(f"Custo estimado: R$ {custo_total:.2f}")
    print(f"------------------------------------\n")

if __name__ == "__main__":
    try:
        calcular_consumo()
    except KeyboardInterrupt:
        print("\n\nPrograma encerrado pelo usuário.")
