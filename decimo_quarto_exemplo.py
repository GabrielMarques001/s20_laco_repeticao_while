"""
SOMANDO OS DÍGITOS
"""

while True:
    numero = input("Digite um número inteiro (ou 0 para sair): ")
    if numero == "0":
        break
    
    soma_digitos = sum(int(digito) for digito in numero)
    print(f"A soma dos dígitos de {numero} é {soma_digitos}")