""" Guarda pedidos en archivo txt """

with open("pedidos.txt", "w", encoding="utf-8") as file_2:
    file_2.write("")
    file_2.close()

def guardar_pedido(nombre, apellidos):
    """ Función Guarda pedido """
    with open("pedidos.txt", "a",  encoding="utf-8",) as file_3:
        file_3.write("-" + nombre + " " + apellidos + "\n")
        file_3.close()
