import email
import imp
from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Agent, Lead
from .forms import LeadForm, LeadModelForm


def lead_list(request):
    leads = Lead.objects.all()
    context = {
        'leads': leads
    }
    return render(request, "leads/lead_list.html", context)


def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        'lead': lead
    }
    return render(request, "leads/lead_detail.html", context)


def lead_create(request):
    form = LeadModelForm()
    if request.method == "POST":
        print('Receiving post request')
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/leads')
    context = {
        "form": form
    }
    return render(request, "leads/lead_create.html", context)

    # def lead_create(request):
    # form = LeadForm()
    # if request.method == "POST":
    #     print('Receiving post request')
    #     form = LeadForm(request.POST)
    #     if form.is_valid():
    #         print("The form is valid")
    #         print(form.cleaned_data)
    #         first_name = form.cleaned_data['first_name']
    #         last_name = form.cleaned_data['last_name']
    #         email = form.cleaned_data['email']
    #         age = form.cleaned_data['age']
    #         agent = Agent.objects.first()
    #         Lead.objects.create(
    #             first_name=first_name,
    #             last_name=last_name,
    #             email=email,
    #             age=age,
    #             agent=agent
    #         )
    #         return redirect('/leads')
    # context = {
    #     "form": form
    # }
    # return render(request, "leads/lead_create.html", context)