from django.shortcuts import render, redirect
from django.template.response import TemplateResponse

productos = [
    {
        'id': 1,
        'nombre': 'Producto 1',
        'precio': 1000,
    },
    {
        'id': 2,
        'nombre': 'Producto 2',
        'precio': 2000,
    },
    {
        'id': 3,
        'nombre': 'Producto 3',
        'precio': 3000,
    }
]


def consulta(request):
    return TemplateResponse(request, 'templates/consulta.html', {'productos': productos})


def registro(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        precio = request.POST['precio']
        nuevo_producto = {
            'id': len(productos) + 1,
            'nombre': nombre,
            'precio': int(precio),
        }
        productos.append(nuevo_producto)
        return redirect('registro')
    return render(request, 'templates/registro.html')

def resultado(request):
    producto = None
    error = None
    if request.method == 'POST':
        id_producto = int(request.POST['id'])
        producto = next((p for p in productos if p['id'] == id_producto), None)
        if not producto:
            error = "Producto no encontrado"
    return render(request, 'templates/resultado.html', {'producto': producto, 'error': error})
