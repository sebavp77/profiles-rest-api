from django.contrib import admin

from profiles_api import models
# Register your models here.

#### Registering my models #####
################################
admin.site.register(models.UserProfile)
