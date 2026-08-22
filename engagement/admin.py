from django.contrib import admin
from .models import VolunteerApplication
from .models import Donation
from .models import ContactMessage

admin.site.register(VolunteerApplication)
admin.site.register(Donation)
admin.site.register(ContactMessage)