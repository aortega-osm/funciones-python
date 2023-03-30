# De celsius a Fanhreint

def celAFanh(temperaturaC):
    tempC=temperaturaC
    temperaturaF=(1.8 * tempC) + 32
    return temperaturaF

temperaturaC=int(input("Proporcione una temperatura de Celsius:"))
print(f"Fanhreint:{celAFanh(temperaturaC)}")