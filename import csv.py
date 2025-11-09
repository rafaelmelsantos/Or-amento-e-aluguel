import csv

print("=== SISTEMA DE ORÇAMENTO DE ALUGUEL - IMOBILIÁRIA R.M ===")

tipo = input("Informe o tipo de imóvel (apartamento / casa / estudio): ").strip().lower()

valor_base = 0
if tipo == "apartamento":
    valor_base = 700
elif tipo == "casa":
    valor_base = 900
elif tipo == "estudio":
    valor_base = 1200
else:
    print("Tipo inválido! Encerrando o programa.")
    exit()

quartos = 0
if tipo in ["apartamento", "casa"]:
    quartos = int(input("Quantos quartos? (1 ou 2): "))
    if tipo == "apartamento" and quartos == 2:
        valor_base += 200
    elif tipo == "casa" and quartos == 2:
        valor_base += 250

if tipo in ["apartamento", "casa"]:
    garagem = input("Deseja incluir garagem? (s/n): ").strip().lower()
    if garagem == "s":
        valor_base += 300

elif tipo == "estudio":
    vagas_iniciais = input("Deseja adicionar 2 vagas de estacionamento (R$250,00)? (s/n): ").strip().lower()
    if vagas_iniciais == "s":
        valor_base += 250
        vagas_extra = int(input("Deseja adicionar mais vagas? Informe quantas (0 se nenhuma): "))
        valor_base += vagas_extra * 60

if tipo == "apartamento":
    criancas = input("Possui crianças? (s/n): ").strip().lower()
    if criancas == "n":
        desconto = valor_base * 0.05
        valor_base -= desconto
    else:
        desconto = 0
else:
    desconto = 0

valor_contrato = 2000
parcelas_contrato = 5
valor_parcela_contrato = valor_contrato / parcelas_contrato

print("\n=== ORÇAMENTO GERADO ===")
print(f"Tipo de imóvel: {tipo.capitalize()}")
if tipo in ["apartamento", "casa"]:
    print(f"Quartos: {quartos}")
print(f"Valor mensal do aluguel: R$ {valor_base:.2f}")
print(f"Valor total do contrato: R$ {valor_contrato:.2f} (em {parcelas_contrato}x de R$ {valor_parcela_contrato:.2f})")
if desconto > 0:
    print(f"Desconto aplicado: R$ {desconto:.2f}")

parcelas = [["Mes", "Valor do Aluguel (R$)"]]
for i in range(1, 13):
    parcelas.append([f"Mes {i}" "-" f"R$:{valor_base:.2f}"])

with open("orcamento.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(parcelas)

print("\nArquivo 'orcamento.csv' gerado com sucesso!")
print("Contendo as 12 parcelas do aluguel mensal.\n")
print("=== FIM DO ORÇAMENTO ===")