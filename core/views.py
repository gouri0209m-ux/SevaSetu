from django.shortcuts import render
from campaigns.models import Campaign
from engagement.models import VolunteerApplication
from engagement.models import Donation
from engagement.models import ContactMessage



def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def contact(request):

    if request.method == 'POST':

        ContactMessage.objects.create(

            name=request.POST.get('name'),

            email=request.POST.get('email'),

            subject=request.POST.get('subject'),

            message=request.POST.get('message')

        )

        return render(
            request,
            'core/contact.html',
            {'success': True}
        )

    return render(
        request,
        'core/contact.html'
    )
    
    
def dashboard(request):

    context = {

        'campaign_count':
        Campaign.objects.count(),

        'volunteer_count':
        VolunteerApplication.objects.count(),

        'donation_count':
        Donation.objects.count(),

        'message_count':
        ContactMessage.objects.count(),

    }

    return render(
        request,
        'core/dashboard.html',
        context
    )