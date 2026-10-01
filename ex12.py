# 12. Peça números ao usuario e vá somando. Quando ele digitar 0, pare e exiba a soma.

soma = 0
numero = float(input("Digite o número (0 para sair)"))

while numero != 0:
    soma = soma + numero
    numero = float(input("Digite um número (0 para sair)"))
print(f"A soma total é: {soma}")

