def calcular_um_terco(salario):
    return salario / 3

def calcular_inss(salario):
    # Alíquotas válidas para 2024 (valores simplificados)
    if salario <= 1412.00:
        return salario * 0.075
    elif salario <= 2666.68:
        return salario * 0.09
    elif salario <= 4000.03:
        return salario * 0.12
    else:
        return salario * 0.14

def calcular_irrf(salario):
    # Simplificação do IRRF - apenas a alíquota principal (não considera deduções)
    if salario <= 2259.20:
        return 0
    elif salario <= 2826.65:
        return salario * 0.075 - 169.44
    elif salario <= 3751.05:
        return salario * 0.15 - 381.44
    elif salario <= 4664.68:
        return salario * 0.225 - 662.77
    else:
        return salario * 0.275 - 896.00

def calcular_ferias(salario_base, descontar_impostos=False):
    um_terco = calcular_um_terco(salario_base)
    bruto = salario_base + um_terco

    if descontar_impostos:
        inss = calcular_inss(bruto)
        irrf = calcular_irrf(bruto)
        liquido = bruto - inss - irrf
        return bruto, inss, irrf, liquido
    else:
        return bruto, 0, 0, bruto

# Execução
try:
    salario = float(input("Digite o seu salário mensal: R$ "))
    descontar = input("Deseja descontar INSS e IRRF? (s/n): ").strip().lower() == 's'

    bruto, inss, irrf, liquido = calcular_ferias(salario, descontar)

    print(f"\n🧾 Resultado do cálculo:")
    print(f"➡ Salário base: R$ {salario:.2f}")
    print(f"➡ 1/3 adicional: R$ {salario / 3:.2f}")
    print(f"➡ Total bruto de férias: R$ {bruto:.2f}")
    if descontar:
        print(f"❌ Desconto INSS: R$ {inss:.2f}")
        print(f"❌ Desconto IRRF: R$ {irrf:.2f}")
        print(f"✅ Total líquido das férias: R$ {liquido:.2f}")
    else:
        print(f"✅ Total líquido das férias (sem descontos): R$ {liquido:.2f}")

except ValueError:
    print("❌ Entrada inválida. Por favor, insira um número válido para o salário.")