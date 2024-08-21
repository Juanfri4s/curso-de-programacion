productos = {}

def agregar_producto(nombre, cantidad, precio):
    if nombre in productos:
        raise ValueError(f"El producto '{nombre}' ya existe.")
    productos[nombre] ={
        'cantidad': cantidad,
        'precio': precio
    }

def actualizar_stock(nombre, nueva_cantidad):
    if nombre not in productos:
        raise KeyError(f"El producto '{nombre}' no existe.")
    productos[nombre]['cantidad'] = nueva_cantidad

def eliminar_producto(nombre):
    if nombre not in productos:
        raise KeyError(f"El producto '{nombre}' no existe.")
    del productos[nombre]

def buscar_producto(nombre):
    return productos.get(nombre, None)
