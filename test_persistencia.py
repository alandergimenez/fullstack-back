""" Pruebas Persistencia """

import persistencia

def test_guardar_pedido():
    """ Prueba general """
    with open("pedidos.txt", "w+", encoding="utf-8") as file_2:
        persistencia.guardar_pedido("Pedro", "Gil de Diego")
        persistencia.guardar_pedido("Michael", "Jordan")
        firstline = file_2.readline()
        secondline = file_2.readline()
        file_2.close()
    assert firstline == "-Pedro Gil de Diego\n"
    assert secondline == "-Michael Jordan\n"
