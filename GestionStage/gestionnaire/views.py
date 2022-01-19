from django.shortcuts import redirect, render
from .forms import EncadreurForm, PromoteurForm, OrganismeForm, GroupeForm, StagierForm
from .models import Encadreur, Promoteur, Organisme, Groupe, Stagier


def index(request):
    return render(request, "dashboard/index.html")


def promoteur(request):
    items = Promoteur.objects.all()

    if request.method == 'POST':
        form = PromoteurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-promoteur')
    else:
        form = PromoteurForm()
    context = {
        'items': items,
        'form': form,
    }
    return render(request, 'dashboard/promoteur.html', context)


def promoteurDelete(request, pk):
    item = Promoteur.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-promoteur')
    context = {
        'item': item
    }
    return render(request, 'dashboard/promoteur_delete.html', context)


def promoteurEdit(request, pk):
    item = Promoteur.objects.get(id=pk)
    if request.method == 'POST':
        form = PromoteurForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-promoteur')
    else:
        form = PromoteurForm(instance=item)

    context = {
        'form': form,
    }
    return render(request, 'dashboard/promoteur_edit.html', context)


def encadreur(request):
    items = Encadreur.objects.all()
    if request.method == 'POST':
        form = EncadreurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-encadreur')
    else:
        form = EncadreurForm()
    context = {
        'items': items,
        'form': form,
    }
    return render(request, 'dashboard/encadreur.html', context)


def encadreurDelete(request, pk):
    item = Encadreur.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-encadreur')
    context = {
        'item': item
    }
    return render(request, 'dashboard/encadreur_delete.html', context)


def encadreurEdit(request, pk):
    item = Encadreur.objects.get(id=pk)
    if request.method == 'POST':
        form = EncadreurForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-encadreur')
    else:
        form = EncadreurForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'dashboard/encadreur_edit.html', context)


def organisme(request):
    items = Organisme.objects.all()
    if request.method == 'POST':
        form = OrganismeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-Organisme')
    else:
        form = OrganismeForm()
    context = {
        'items': items,
        'form': form,
    }
    return render(request, 'dashboard/Organisme.html', context)


def OrganismeDelete(request, pk):
    item = Organisme.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-Organisme')
    context = {
        'item': item
    }
    return render(request, 'dashboard/Organisme_delete.html', context)


def OrganismeEdit(request, pk):
    item = Organisme.objects.get(id=pk)
    if request.method == 'POST':
        form = OrganismeForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-Organisme')
    else:
        form = OrganismeForm(instance=item)

    context = {
        'form': form,
    }
    return render(request, 'dashboard/Organisme_edit.html', context)

#abdenour's code.....
def getGroup(request):
    items = Groupe.objects.all()
    if request.method == 'POST':
        form = GroupeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Group-dashboard')
    else:
        form = GroupeForm()
    context = {
        'items': items,
        'form': form,
    }
    return render(request, 'dashboard/Group.html', context)


def GroupDelete(request, pk):
    item = Groupe.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-Group')
    context = {
        'item': item
    }
    return render(request, 'dashboard/Group_delete.html', context)


def GroupEdit(request, pk):
    item = Groupe.objects.get(id=pk)
    if request.method == 'POST':
        form = GroupeForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-Group')
    else:
        form = GroupeForm(instance=item)

    context = {
        'form': form,
    }
    return render(request, 'dashboard/Group_edit.html', context)

def getStagier(request):
    items = Stagier.objects.all()
    if request.method == 'POST':
        form = StagierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Stagier-dashboard')
    else:
        form = StagierForm()
    context = {
        'items': items,
        'form': form,
    }
    return render(request, 'dashboard/Stagier.html', context)


def StagierDelete(request, pk):
    item = Stagier.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-Stagier')
    context = {
        'item': item
    }
    return render(request, 'dashboard/Stagier_delete.html', context)


def StagierEdit(request, pk):
    item = Stagier.objects.get(id=pk)
    if request.method == 'POST':
        form = StagierForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-Stagier')
    else:
        form = StagierForm(instance=item)

    context = {
        'form': form,
    }
    return render(request, 'dashboard/Stagier_edit.html', context)
