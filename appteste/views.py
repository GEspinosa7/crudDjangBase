from django.shortcuts import render, redirect
from .models import Appteste
from .forms import ApptesteForm

def list_appteste(request):
    apptestes = Appteste.objects.all()
    return render(request, 'appteste.html', {'apptestes': apptestes})


def create_appteste(request):
    form = ApptesteForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("list_appteste")

    return render(request, 'appteste-form.html', {'form': form})

def update_appteste(request, id):
    appteste = Appteste.objects.get(id=id)
    form = ApptesteForm(request.POST or None, instance=appteste)

    if form.is_valid():
        form.save()
        return redirect('list_appteste')

    return render(request, 'appteste-form.html', {'form': form, 'appteste': appteste})

def delete_appteste (request, id):
    appteste = Appteste.objects.all().get(id=id)

    if request.method == 'POST':
        appteste.delete()
        return redirect('list_appteste')

    return render(request, 'appteste-delete-confirm.html', {'appteste': appteste})