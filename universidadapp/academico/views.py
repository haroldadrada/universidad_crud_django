from django.shortcuts import redirect, render
from .models import Curso

# Create your views here.

def home(request):
    cursos_listados = Curso.objects.all()
    return render(request, 'academico/gestionCursos.html', {'cursos': cursos_listados})

def registrarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    curso = Curso.objects.create(codigo=codigo, nombre=nombre, creditos=creditos)
    return redirect('/')