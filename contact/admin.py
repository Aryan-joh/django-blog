from django.contrib import admin
from .models import About, SocialLink    
# Register your models here.



# This line of code remove the 'add' button functionality from the admin dashboard

class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count = About.objects.all().count()
        if count == 0:
            return True
        return False


admin.site.register(About, AboutAdmin)
admin.site.register(SocialLink)