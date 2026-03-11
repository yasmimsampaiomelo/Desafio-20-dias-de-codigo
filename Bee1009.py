nome = input()
salario = float(input())
totalVendas = float(input())
comissao = (0.15 *  totalVendas) + salario;
print(f"TOTAL = R$ {comissao:.2f}")