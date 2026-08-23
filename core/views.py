from django.shortcuts import render

from campaigns.models import Campaign
from engagement.models import ContactMessage, Donation, VolunteerApplication


def home(request):
    campaigns = Campaign.objects.all().order_by('-id')[:3]

    context = {
        'campaigns': campaigns,
        'campaign_count': Campaign.objects.count(),
        'volunteer_count': VolunteerApplication.objects.count(),
        'donation_count': Donation.objects.count(),
    }

    return render(request, 'core/home.html', context)


def about(request):
    return render(request, 'core/about.html')


def gallery(request):
    return render(request, 'core/gallery.html')


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

    return render(request, 'core/contact.html')


def dashboard(request):
    context = {
        'campaign_count': Campaign.objects.count(),
        'volunteer_count': VolunteerApplication.objects.count(),
        'donation_count': Donation.objects.count(),
        'message_count': ContactMessage.objects.count(),
    }

    return render(request, 'core/dashboard.html', context)
