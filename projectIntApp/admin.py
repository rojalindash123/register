from django.contrib import admin

# Register your models here.
from .models import Signup,Status
# Register your models here.

myModels=[Signup,Status]
admin.site.register(myModels)