""" Guarda pedidos en archivo txt """

with open("pedidos.txt", "w", encoding="utf-8") as file:
    file.write("")
    file.close()

def guardar_pedido(nombre, apellidos):
    """ Función Guarda pedido """
    with open("pedidos.txt", "a",  encoding="utf-8",) as file:
        file.write("-" + nombre + " " + apellidos + "\n")
        file.close()
