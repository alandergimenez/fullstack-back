import os


# Limpia el registro del fichero pedidos.txt
with open("pedidos.txt", "w", encoding="utf-8") as file: 
    file.write("")     
    file.close()


def guardar_pedido(nombre, apellidos):
   
   file = open("pedidos.txt", "a",  encoding="utf-8",)
   file.write(nombre + " " + apellidos + "\n")
   file.close()