""" Pruebas Persistencia """

import persistencia
import pytest

def test_guardar_pedido():
    """ Prueba general """
    with open("pedidos.txt", "w+", encoding="utf-8") as f:
        persistencia.guardar_pedido("Pedro", "Gil de Diego")
        persistencia.guardar_pedido("Michael", "Jordan")
        firstline = f.readline()
        secondline = f.readline()
        f.close()
    assert firstline == "-Pedro Gil de Diego\n"
    assert secondline == "-Michael Jordan\n"
