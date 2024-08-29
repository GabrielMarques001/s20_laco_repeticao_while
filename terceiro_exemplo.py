"""
PRESENTE DE ANIVERSÁRIO
"""
presente_esperado = "anel"

while True:
    presente = input("Qual presente a hiago espera do cleiton?: ")
    if presente == presente_esperado:
        print("Acertou! Sonho Realizado!")
        break
    else:
        print("Errou! Continue tentando.")