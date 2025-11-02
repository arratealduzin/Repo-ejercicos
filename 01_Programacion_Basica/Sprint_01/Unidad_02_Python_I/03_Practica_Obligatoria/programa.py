entrada = input("Por favor, introduzca 3 números enteros separados por comas:")
entrada_2 = entrada.split(",") # No hace falta convertirla en otra variable.
print(entrada_2, type(entrada_2))
entrada_num = [int(x) for x in entrada_2] # Cambiar los string de una lista a int.
                                          # Es un List conprehension.  
print(entrada_num)
num_max = max(entrada_num)
print(num_max)
num_min = min(entrada_num)
print(num_min)
suma =sum(entrada_num)
print(suma)
Booleano = (num_max - num_min) == (suma / 5)
print(Booleano)

