# Crear una funcion para calcular el total de un pago incluyendo un impuesto
# formula pago_total= pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)

def calculoPago(pagoSinImpuesto, impuesto):
    pago = pagoSinImpuesto + pagoSinImpuesto * (impuesto / 100)
    return pago


pagoSinImpuesto = int(input("Pago:"))
impuesto = int(input("Impuesto:"))
print(calculoPago(pagoSinImpuesto, impuesto))
