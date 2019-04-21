from django.shortcuts import render, HttpResponseRedirect
from .models import crud

# Create your views here.
def cruds(request):
    creates = crud.objects.all()
    return render(request, 'index.html', {'creates': creates})

def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        crud.objects.create(name=name)
        return HttpResponseRedirect('/lcw_crud/')

def delete(request):
    id = request.GET.get('id')
    crud.objects.filter(id=id).delete()
    return HttpResponseRedirect('/lcw_crud/')

def update(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        update = crud.objects.filter(id=id).first()
        return render(request, 'update/update.html', {'update': update})
    elif request.method == 'POST':
        id = request.GET.get('id')
        name = request.POST.get('name')
        crud.objects.filter(id=id).update(name=name)
        crud.objects.create(name=name)
        return HttpResponseRedirect('/lcw_crud/')