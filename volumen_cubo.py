
def volumen_cubo(n):
    volumen=n**3
    return volumen

valor_lado = 4

if valor_lado < 0:
    raise ValueError("No hagas eso, no tiene sentido introducir un lado negativo")

print()
print("El volumen de este cubo es: ", valor_lado*valor_lado*valor_lado, "m^3")
