from django.shortcuts import render, redirect
from crud.forms import ApplicationForm
from crud.models import Application


# Create your views here.
def create(request):
    application = ApplicationForm()
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:home')
    return render(request, 'application.html', {'application': application})


def show(request):
    applications = Application.objects.all()
    return render(request, 'show.html', {'applications': applications})


def update(request, id):
    application = Application.objects.get(id=id)
    form = ApplicationForm(instance=application)
    if request.method == 'POST':
        form = ApplicationForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            return redirect('crud:show')
    return render(request, 'update.html', {'form': form})


def delete(request, id):
    if request.method == 'POST':
        Application.objects.get(id=id).delete()
        return redirect('crud:show')
