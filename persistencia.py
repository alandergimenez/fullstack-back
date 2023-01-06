""" Guarda pedidos en archivo txt """

with open("pedidos.txt", "w", encoding="utf-8") as file:
    file.write("")
    file.close()

def guardar_pedido(nombre, apellidos):
    """ Función Guarda pedido """
    datos = open("pedidos.txt", "a",  encoding="utf-8",)
    datos.write("-" + nombre + " " + apellidos + "\n")
    datos.close()
