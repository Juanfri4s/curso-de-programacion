import pytest
from inventario import agregar_producto, actualizar_stock, eliminar_producto, buscar_producto, productos

def setup_function():
    # Limpiar el inventario antes de cada prueba
    productos.clear()

def test_agregar_producto():
    agregar_producto("Pepsi 2l", 10, 1700)
    assert productos["Pepsi 2l"] == {
        'cantidad': 10,
        'precio': 1700
        }
   
    with pytest.raises(ValueError):
        agregar_producto("Pepsi 2l", 5, 0.4) #producto ya existe

def test_actualizar_stock():
    agregar_producto("Pepsi 2l", 10, 1700)
    actualizar_stock("Pepsi 2l", 20)
    assert productos["Pepsi 2l"]['cantidad'] == 20
   
    with pytest.raises(KeyError):
        actualizar_stock("Coca", 20)

def test_eliminar_producto():
    agregar_producto("Pepsi 2l", 10, 1700)
    eliminar_producto("Pepsi 2l")
    assert "Pepsi 2l" not in productos
   
    with pytest.raises(KeyError):
        eliminar_producto("Coca")

def test_buscar_producto():
    agregar_producto("Pepsi 2l", 10, 1700)
    resultado = buscar_producto("Pepsi 2l")
    assert resultado == {
        'cantidad': 10,
        'precio': 1700
        }
   
    resultado = buscar_producto("Peras")
    assert resultado is None