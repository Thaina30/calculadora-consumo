# Consumo de energia

# Dados de entrada

aparelho = input("Digite o nome do aparelho eltrodomestico: ")
potencia = float(input("Digite a potencia em watts: ").replace("W", "").replace("w", ""))
tempo_diario = float(input("Digite o tempo medio de uso diario em horas: "))

# Calculos

consumo_mensal_kWh = potencia * tempo_diario * 30 / 1000
custo_estimado = 0.65 * consumo_mensal_kWh

# Saida de dados

print(f"Aparelho: {aparelho}")
print(f"Consumo estimado: {consumo_mensal_kWh:.2f} kWh")
print(f"Custo estimado: R$ {custo_estimado:.2f}")