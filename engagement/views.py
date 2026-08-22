from django.shortcuts import render, redirect
from .forms import VolunteerForm


def volunteer_apply(request):

    if request.method == 'POST':

        form = VolunteerForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('home')

    else:
        form = VolunteerForm()

    return render(
        request,
        'engagement/volunteer_form.html',
        {'form': form}
    )
    

from .forms import DonationForm


def donate(request):

    if request.method == 'POST':

        form = DonationForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('home')

    else:

        form = DonationForm()

    return render(
        request,
        'engagement/donation_form.html',
        {'form': form}
    )