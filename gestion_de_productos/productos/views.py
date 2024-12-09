from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm

def index(request):
    productos = Producto.objects.all()
    return render(request, 'templates/index.html', {'productos': productos})

def registro(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resultado')
    else:
        form = ProductoForm()
    return render(request, 'templates/registro.html', {'form': form})

def resultado(request):
    producto = None
    error = None
    if request.method == 'POST':
        producto_id = request.POST.get('id')
        try:
            producto = Producto.objects.get(id=producto_id)
        except Producto.DoesNotExist:
            error = "Producto no encontrado"
    return render(request, 'templates/resultado.html', {'producto': producto, 'error': error})