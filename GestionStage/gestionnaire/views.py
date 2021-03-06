from django.shortcuts import redirect, render
from .filters import EncadreurFilter, GroupeFilter, OrganismeFilter, PromoteurFilter, StageFilter, StagiereFilter
from .forms import EncadreurForm, GroupeForm, PromoteurForm,OrganismeForm, StageForm, StagierForm
from .models import Encadreur, Groupe, Promoteur,Organisme, Stage, Stagier
from django.contrib.auth.decorators import login_required



#index view /main page
@login_required(login_url='user-login')
def index(request):



    retardGroupe=[]
    retardEncadreur=[]

    for groupe in Groupe.objects.filter(dateRemise = None):
            retardGroupe.append(groupe)
            retardEncadreur.append(Encadreur.objects.filter(nomEncadreur = groupe.idEncadreur))


    # Etat de classement des organismes partenaires professionnels de l'ESI sur la base du nombre de stagiaires retenus.
    stages_count=[]
    organismes=[]

    for organ in Organisme.objects.filter(typeOrganisme="Partenaire"):
        for p in Promoteur.objects.filter(idOrganisme=organ.id):
            for m in Stage.objects.filter(idPromoteur=p.id):
                for i in Groupe.objects.filter(numStage=m.id):
                    if organ in organismes:   #verifier si organisme est deja dans la list organimses
                        stages_count[organismes.index(organ)] = stages_count[organismes.index(organ)] + Stagier.objects.filter(idGroupe=i.id).count()
                    else:
                        stages_count.append(Stagier.objects.filter(idGroupe=i.id).count())
                        organismes.append(organ)
    

    #----------------------------------------------------------------------------

    #Taux d'évolution du nombre d'organismes ayant reçus des stagiaires PFE.

    
    anne = []  #les années

    for p in Stagier.objects.distinct().values_list('anneeStage'):
        for s in p:
            anne.append(s)
    anne.sort()
    


    cp = 0
    evolution=[]
    for annee in anne:
        for organ in Organisme.objects.all():
            for p in Promoteur.objects.filter(idOrganisme=organ.id):
                for m in Stage.objects.filter(idPromoteur=p.id,typeStage=3):
                    for q in Groupe.objects.filter(numStage=m.id):  
                        if str(q.dateDebutStage.year) == annee:
                            cp = cp + 1    
        
        evolution.append(cp)
        cp = 0


    #----------------------------------------------------------------------------

    #Répartition des PFE / entreprise


    pfe_count=[] 
    list_organismes = []
    for i in Organisme.objects.all():
        for p in Promoteur.objects.filter(idOrganisme=i.id):
            if i in list_organismes:
                pfe_count[list_organismes.index(i)] =pfe_count[organismes.index(i)] + Stage.objects.filter(idPromoteur=p.id,typeStage=3).count() 
            else:
                pfe_count.append(Stage.objects.filter(idPromoteur=p.id,typeStage=3).count() )
                list_organismes.append(i)

    nbOrganisme = Organisme.objects.all().count()
    nbEtudiant = Stagier.objects.all().count()
    nbStage  = Stage.objects.all().count()
    nbPromoteur= Promoteur.objects.all().count()
    nbNonRemise = Groupe.objects.filter(dateRemise = None).count()
    
    nb= [{'nbe':"Nombre Etudiant",'nb':nbEtudiant}, {'nbe':"Nombre Organisme",'nb':nbOrganisme},{'nbe':"Nombre Promoteur", 'nb':nbPromoteur},{'nbe':"Nombre Stage", 'nb':nbStage},{'nbe':"Rapport non remise", 'nb':nbNonRemise}] 

    context = {
        'organismes':organismes,
        'stages_count':stages_count,
        'anne':anne,
        'pfe_count':pfe_count,
        'list_organismes' : list_organismes,
        'evolution': evolution,
        'retardGroupe' : retardGroupe,
        'retardEncadreur' : retardEncadreur,
        'evolution':evolution,
        'nb' : nb
    }
    
    return render(request,"dashboard/index.html",context)





def retard(request,pk):

    groupe = Groupe.objects.filter(dateRemise = None, id = pk)
    retardStagiaire = Stagier.objects.filter(idGroupe = pk)

    
    context = {
        'retardStagiaire' : retardStagiaire,
        'groupe' : groupe,
    }
    
    return render(request,"dashboard/retard.html",context)





def anneefiltre(request,pk):
     # Etat de classement des organismes partenaires professionnels de l'ESI sur la base du nombre de stagiaires retenus.
    
    retardGroupe=[]
    retardEncadreur=[]

    for groupe in Groupe.objects.filter(dateRemise = None):
            retardGroupe.append(groupe)
            retardEncadreur.append(Encadreur.objects.filter(nomEncadreur = groupe.idEncadreur))



    stages_count=[]
    organismes=[]

    for organ in Organisme.objects.filter(typeOrganisme="Partenaire"):
        for p in Promoteur.objects.filter(idOrganisme=organ.id):
            for m in Stage.objects.filter(idPromoteur=p.id):
                for i in Groupe.objects.filter(numStage=m.id):
                    if organ in organismes:   #verifier si organisme est deja dans la list organimses
                        stages_count[organismes.index(organ)] = stages_count[organismes.index(organ)] + Stagier.objects.filter(idGroupe=i.id, anneeStage=pk).count()
                    else:
                        stages_count.append(Stagier.objects.filter(idGroupe=i.id,anneeStage=pk).count())
                        organismes.append(organ)
    

    
    #----------------------------------------------------------------------------

    #Taux d'évolution du nombre d'organismes ayant reçus des stagiaires PFE.

    
    anne = []  #les années

    for p in Stagier.objects.distinct().values_list('anneeStage'):
        for s in p:
            anne.append(s)
    anne.sort()
    


    cp = 0
    evolution=[]
    for annee in anne:
        for organ in Organisme.objects.all():
            for p in Promoteur.objects.filter(idOrganisme=organ.id):
                for m in Stage.objects.filter(idPromoteur=p.id,typeStage=3):
                    for q in Groupe.objects.filter(numStage=m.id):  
                        if str(q.dateDebutStage.year) == annee:
                            cp = cp + 1    
        
        evolution.append(cp)
        cp = 0  
   

    #------------------------------------------------------------
    
    #Répartition des PFE / entreprise
    pfe_count=[]
    list_organismes = [] 
    for l in Organisme.objects.all():
        for p in Promoteur.objects.filter(idOrganisme=l.id):
            for m in Stage.objects.filter(idPromoteur=p.id):
                for i in Groupe.objects.filter(numStage=m.id):
                    for s in Stagier.objects.filter(idGroupe=i.id,anneeStage=pk):
                        if l in list_organismes:
                            pfe_count[list_organismes.index(l)] =Stage.objects.filter(idPromoteur=p.id,typeStage=3).count() + pfe_count[list_organismes.index(l)] 
                        else:
                            pfe_count.append(Stage.objects.filter(idPromoteur=p.id,typeStage=3).count())
                            list_organismes.append(l)

    context = {
        'organismes':organismes,
        'stages_count':stages_count,
        'anne':anne,
        'pfe_count':pfe_count,
        'list_organismes' : list_organismes,
        'evolution' : evolution,
        'retardGroupe' : retardGroupe,
        'retardEncadreur' : retardEncadreur,
    }
    return render(request,"dashboard/index.html",context)




# ========================================================== promoteur

# promoteur main page view
@login_required(login_url='user-login')
def promoteur(request):
    
    items = Promoteur.objects.all()

    myFilter = PromoteurFilter(request.GET, queryset=items) #search function for Promoteur
    items = myFilter.qs

    if request.method == 'POST':  #table Promoteur
        form = PromoteurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-promoteur')
    else:
        form = PromoteurForm()
    context = {
        'items': items,
        'form' : form,
        'myFilter' : myFilter,
    }
    return render(request, 'dashboard/promoteur.html', context)


#promoteur delete view
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


#promoteur update view
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





# ===================================================== encadreur

# Encadreur main page view

@login_required(login_url='user-login')
def encadreur(request):
    
    items = Encadreur.objects.all()

    myFilter = EncadreurFilter(request.GET, queryset=items)  #search function for Encadreur
    items = myFilter.qs

    if request.method == 'POST':   #table Encadreur
        form = EncadreurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-encadreur')
    else:
        form = EncadreurForm()
    context = {
        'items': items,
        'form' : form,
        'myFilter' : myFilter,
    }
    return render(request, 'dashboard/encadreur.html', context)


# Encadreur delete view
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


# Encadreur update view
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






# ====================================================== organisme

# organisme main page view

@login_required(login_url='user-login')
def organisme(request):

    items = Organisme.objects.all()

    myFilter = OrganismeFilter(request.GET, queryset=items) #search function for Organisme
    items = myFilter.qs

    if request.method == 'POST':    #table Organisme
        form = OrganismeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-Organisme')
    else:
        form = OrganismeForm()
    context = {
        'items': items,
        'form' : form,
        'myFilter' : myFilter,
    }
    return render(request, 'dashboard/Organisme.html', context)



# organisme delete view

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


# organisme update view

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





# ================================================ groupe

# groupe main page view
@login_required(login_url='user-login')
def getGroup(request):
    
    items = Groupe.objects.all()

    myFilter = GroupeFilter(request.GET, queryset=items) #search function for Groupe
    items = myFilter.qs

    if request.method == 'POST':    #table groupe
        form = GroupeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-Group')
    else:
        form = GroupeForm()
    context = {
        'items': items,
        'form': form,
        'myFilter': myFilter,
    }
    return render(request, 'dashboard/Group.html', context)


#groupe deelete view

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


#groupe edit view

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



#============================================== stagiere

#stagiere main page

@login_required(login_url='user-login')
def getStagier(request):
    items = Stagier.objects.all()
    myFilter = StagiereFilter(request.GET, queryset=items) #search function for Stagiere
    items = myFilter.qs

    if request.method == 'POST':    #table groupe
        form = StagierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-Stagier')
    else:
        form = StagierForm()
    context = {
        'items': items,
        'form': form,
        'myFilter' : myFilter,
    }
    return render(request, 'dashboard/Stagier.html', context)


#stagiere delete view

@login_required(login_url='user-login')
def StagierDelete(request, pk):
    item = Stagier.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-Stagier')
    context = {
        'item': item
    }
    return render(request, 'dashboard/Stagier_delete.html', context)


# satagiere edit view

@login_required(login_url='user-login')
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
         'item': item,
        'form': form,
    }
    return render(request, 'dashboard/Stagier_edit.html', context)




#============================================== stage

#stage main page



@login_required(login_url='user-login')
def stage(request):

    items = Stage.objects.all()
    myFilter = StageFilter(request.GET, queryset=items) #search function for stage
    items = myFilter.qs

    if request.method == 'POST':    #table stage
        form = StageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-Stage')
    else:
        form = StageForm()
    context = {
        'items': items,
        'form': form,
        'myFilter' : myFilter,
    }
    return render(request, 'dashboard/Stage.html', context)


#stagiere delete view

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


#stagiere edit view

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




