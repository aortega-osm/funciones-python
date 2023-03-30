#Convertir 2 funciones para convertir de grados celsius a grados fanhreint y viceversa
# 1,8* C + 32 Celsius a F
# C=(F-32) / 1.8   F a Celsius


def fanhACel(temperaturaF):
    tempF=temperaturaF
    temperaturaC = (tempF - 32) // 1.8
    return temperaturaC

temperaturaF=int(input("Proporcione una temperatura de Fanhreint:"))
print(f"Celsius:{fanhACel(temperaturaF)}")

def celAFanh(temperaturaC):
    tempC=temperaturaC
    temperaturaF=(1.8 * tempC) + 32
    return temperaturaF

temperaturaC=int(input("Proporcione una temperatura de Celsius:"))
print(f"Fanhreint:{celAFanh(temperaturaC)}")