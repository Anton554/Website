from django.contrib import admin

from .models import UsRequest, Services, Staff, Feedback

admin.site.register(UsRequest)
admin.site.register(Services)
admin.site.register(Staff)
admin.site.register(Feedback)