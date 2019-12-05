from django.contrib import admin
from solo.admin import SingletonModelAdmin
from core.models import *

# Register your models here.
admin.site.register(MVV, SingletonModelAdmin)
admin.site.register(Servicos)
admin.site.register(Banner)