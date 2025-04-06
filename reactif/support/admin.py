from django.contrib import admin # type: ignore
from .models import SupportMessage

admin.site.register(SupportMessage)
