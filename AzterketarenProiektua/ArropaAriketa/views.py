from django.shortcuts import get_object_or_404, redirect, render

from ArropaAriketa.forms import BildumaForm, JantziaForm, DiseinatzaileaForm
from ArropaAriketa.models import Bilduma, Jantzia, Diseinatzailea

# Create your views here.
def base(request):
    return render(request, 'arropaAriketa/base.html')

#Jantziaren bistak
def jantzia_list(request):
    jantziZerrenda=Jantzia.objects.all()
    return render(request, 'arropaAriketa/jantzia/jantzia_list.html',{'jantziak':jantziZerrenda})

def new_jantzia(request):
    if request.method == 'POST':
        form=JantziaForm(request.POST)
        if form.is_valid:
            jantzia = form.save()
            jantzia.save()
        return redirect('base')
    else:
        form=JantziaForm()
        return render(request, 'arropaAriketa/jantzia/jantzia_new.html', {'form':form})
    
def delete_jantzia(request):
    if request.method == 'POST':
        id = request.POST.get("id", "")
        Jantzia.objects.filter(id=id).delete()
        return redirect('base')
    
    else:
        jantziZerrenda=Jantzia.objects.all()
        return render(request, 'arropaAriketa/jantzia/jantzia_delete.html',{'jantziak':jantziZerrenda})
    
def edit_jantzia(request):
    if request.method == 'POST':
        id = request.POST.get("id", "")
        jantzia = Jantzia.objects.get(id=id)
        jantzia.deskripzioa = request.POST.get("deskripzioa", jantzia.deskripzioa)
        jantzia.kolorea = request.POST.get("kolorea", jantzia.kolorea)
        jantzia.kopurua = request.POST.get("kopurua", jantzia.kopurua)
        jantzia.save()

        return redirect('base')
    
    else:
        jantziZerrenda=Jantzia.objects.all()
        return render(request, 'arropaAriketa/jantzia/jantzia_edit.html',{'jantziak':jantziZerrenda})

def edit_jantzia_form(request, jantzia_id):
    jantzia = get_object_or_404(Jantzia, id=jantzia_id)

    if request.method == 'POST':
        form = JantziaForm(request.POST, instance=jantzia)
        if form.is_valid():
            form.save()
            return redirect('base')
    else:
        form = JantziaForm(instance=jantzia)

    return render(request, 'arropaAriketa/jantzia/jantzia_new.html', {'form': form})

#Diseinatzailearen bistak
def diseinatzailea_list(request):
    diseinatzaileZerrenda=Diseinatzailea.objects.all()
    return render(request, 'arropaAriketa/diseinatzailea/diseinatzailea_list.html',{'diseinatzaileak':diseinatzaileZerrenda})

def new_diseinatzailea(request):
    if request.method == 'POST':
        form=DiseinatzaileaForm(request.POST)
        if form.is_valid:
            diseinatzailea = form.save()
            diseinatzailea.save()
        return redirect('base')
    else:
        form=DiseinatzaileaForm()
        return render(request, 'arropaAriketa/diseinatzailea/diseinatzailea_new.html', {'form':form})
    
def delete_diseinatzailea(request):
    if request.method == 'POST':
        id = request.POST.get("id", "")
        Diseinatzailea.objects.filter(id=id).delete()
        return redirect('base')
    
    else:
        diseinatzaileZerrenda=Diseinatzailea.objects.all()
        return render(request, 'arropaAriketa/diseinatzailea/diseinatzailea_delete.html',{'diseinatzaileak':diseinatzaileZerrenda})
    
def edit_diseinatzailea(request):
    if request.method == 'POST':
        id = request.POST.get("id", "")
        diseinatzailea = Diseinatzailea.objects.get(id=id)
        diseinatzailea.izena = request.POST.get("izena", diseinatzailea.izena)
        diseinatzailea.abizena = request.POST.get("abizena", diseinatzailea.abizena)
        diseinatzailea.helbidea = request.POST.get("helbidea", diseinatzailea.helbidea)
        diseinatzailea.emaila = request.POST.get("emaila", diseinatzailea.emaila)
        diseinatzailea.save()

        return redirect('base')
    
    else:
        diseinatzaileZerrenda=Diseinatzailea.objects.all()
        return render(request, 'arropaAriketa/diseinatzailea/diseinatzailea_edit.html',{'diseinatzaileak':diseinatzaileZerrenda})

def edit_diseinatzailea_form(request, diseinatzailea_id):
    diseinatzailea = get_object_or_404(Diseinatzailea, id=diseinatzailea_id)

    if request.method == 'POST':
        form = DiseinatzaileaForm(request.POST, instance=diseinatzailea)
        if form.is_valid():
            form.save()
            return redirect('base')
    else:
        form = DiseinatzaileaForm(instance=diseinatzailea)

    return render(request, 'arropaAriketa/diseinatzailea/diseinatzailea_new.html', {'form': form})

#Bildumaren bistak
def list_bilduma(request):
    bildumaZerrenda=Bilduma.objects.all()
    return render(request, 'arropaAriketa/bilduma/bilduma_list.html',{'bildumak':bildumaZerrenda})

def new_bilduma(request):
    if request.method == 'POST':
        form=BildumaForm(request.POST)
        if form.is_valid:
            bilduma = form.save()
            bilduma.save()
        return redirect('base')
    else:
        form=BildumaForm()
        return render(request, 'arropaAriketa/bilduma/bilduma_new.html', {'form':form})