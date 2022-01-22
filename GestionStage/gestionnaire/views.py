from ast import And
from itertools import count, product
from select import select
from tkinter.tix import Select
from typing import Any
from django.shortcuts import redirect, render
from django.template import context
from .forms import EncadreurForm, GroupeForm, PromoteurForm,OrganismeForm, StageForm, StagierForm
from .models import Encadreur, Groupe, Promoteur,Organisme, Stage, Stagier
from django.db.models import Q
from django.contrib.auth.decorators import login_required



@login_required(login_url='user-login')
def index(request):
    stages_count=[]
<<<<<<< Updated upstream
    for organ in Organisme.objects.filter(typeOrganisme="Partenaire"):
        stages_count.append(Stage.objects.filter(idOrganisme=organ).count()) 
    organismes =Organisme.objects.filter(typeOrganisme="Partenaire") 
=======
    for organ in Organisme.objects.all():
        stages_count.append(Stage.objects.filter(idOrganisme=organ).count()) 
    organismes =Organisme.objects.all() 
>>>>>>> Stashed changes
    context = {
        'organismes':organismes,
        'stages_count':stages_count,
        'organ':organ,

    }
    return render(request,"dashboard/index.html",context)







@login_required(login_url='user-login')
def promoteur(request):
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(nomPromoteur__icontains=q) | Q(prenomPromoteur__icontains=q))
        items = Promoteur.objects.filter(multiple_q)
    else:
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
        'form' : form,
    }
    return render(request, 'dashboard/promoteur.html', context)


@login_required(login_url='user-login')
def promoteurDelete(request, pk):
    item = Promoteur.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-promoteur')
    context = {
        'item': item
    }
    return render(request, 'dashboard/promoteur_delete.html',context)


@login_required(login_url='user-login')
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
         'item': item,
        'form': form,
    }
    return render(request, 'dashboard/promoteur_edit.html', context)








@login_required(login_url='user-login')
def encadreur(request):
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(nomEncadreur__icontains=q) | Q(prenomEncadreur__icontains=q))
        items = Encadreur.objects.filter(multiple_q)
    else:
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
        'form' : form,
    }
    return render(request, 'dashboard/encadreur.html', context)

@login_required(login_url='user-login')
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
         'item': item,
        'form': form,
    }
    return render(request, 'dashboard/encadreur_edit.html', context)







@login_required(login_url='user-login')
def organisme(request):
    if 'q' in request.GET:
        q = request.GET['q']
        items = Organisme.objects.filter(nomOrganisme__icontains=q)
    else:
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
        'form' : form,
    }
    return render(request, 'dashboard/Organisme.html', context)


@login_required(login_url='user-login')
def OrganismeDelete(request, pk):
    item = Organisme.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-Organisme')
    context = {
        'item': item
    }
    return render(request, 'dashboard/Organisme_delete.html',context)


@login_required(login_url='user-login')
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
         'item': item,
        'form': form,
    }
    return render(request, 'dashboard/Organisme_edit.html', context)








#abdenour's code.....
@login_required(login_url='user-login')
def getGroup(request):
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(numEncadreur__icontains=q) | Q(idPromoteur__icontains=q) | Q(numStage__icontains=q))
        items = Groupe.objects.filter(multiple_q)
    else:
        items = Groupe.objects.all()
    if request.method == 'POST':
        form = GroupeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-Group')
    else:
        form = GroupeForm()
    context = {
        'items': items,
        'form': form,
    }
    return render(request, 'dashboard/Group.html', context)


@login_required(login_url='user-login')
def GroupDelete(request, pk):
    item = Groupe.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-Group')
    context = {
        'item': item
    }
    return render(request, 'dashboard/Group_delete.html', context)


@login_required(login_url='user-login')
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
         'item': item,
        'form': form,
    }
    return render(request, 'dashboard/Group_edit.html', context)






@login_required(login_url='user-login')
def getStagier(request):
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(nomStagier__icontains=q) | Q(prenomStagier__icontains=q) | Q(matricule__icontains=q))
        items = Stagier.objects.filter(multiple_q)
    else:
        items = Stagier.objects.all()
    if request.method == 'POST':
        form = StagierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-Stagier')
    else:
        form = StagierForm()
    context = {
        'items': items,
        'form': form,
    }
    return render(request, 'dashboard/Stagier.html', context)


@login_required(login_url='user-login')
def StagierDelete(request, pk):
    item = Stagier.objects.get(matricule=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-Stagier')
    context = {
        'item': item
    }
    return render(request, 'dashboard/Stagier_delete.html', context)


@login_required(login_url='user-login')
def StagierEdit(request, pk):
    item = Stagier.objects.get(matricule=pk)
    if request.method == 'POST':
        form = StagierForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-Stagier')
    else:
        form = StagierForm(instance=item)

    context = {
         'item': item,
        'form': form,
    }
    return render(request, 'dashboard/Stagier_edit.html', context)




@login_required(login_url='user-login')
def stage(request):
    # if 'q' in request.GET:
    #     q = request.GET['q']
    #     items = Stage.objects.filter(nomStage__icontains=q)
    # else:
    #     items = Stage.objects.all()
    
    items = Stage.objects.all()
    if request.method == 'POST':
        form = StageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-Stage')
    else:
        form = StageForm()
    context = {
        'items': items,
        'form': form,
    }
    return render(request, 'dashboard/Stage.html', context)


@login_required(login_url='user-login')
def StageDelete(request, pk):
    item = Stage.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-Stage')
    context = {
        'item': item
    }
    return render(request, 'dashboard/Stage_delete.html', context)




@login_required(login_url='user-login')
def StageEdit(request, pk):
    item = Stage.objects.get(id=pk)
    if request.method == 'POST':
        form = StageForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-Stage')
    else:
        form = StageForm(instance=item)
    context = {
        'item' : item,
        'form': form,
    }
    return render(request,'dashboard/Stage_edit.html', context)




