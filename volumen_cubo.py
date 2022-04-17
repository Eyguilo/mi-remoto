
def volumen_cubo(n):
    volumen=n**3
    return volumen

valor_lado = 4

if type(valor_lado) not in[int, float]:
    raise TypeError("El lado tiene que "
                    "ser un número mayor o igual que cero y real")

print()
print("El volumen de este cubo es: ",
      valor_lado*valor_lado*valor_lado, "m^3")
