from django.contrib import admin
from django.contrib.auth.admin import Group,User
from .models import Profile, Banter


# admin.site.register(Profile)

# Unregister the Group model from the admin
admin.site.unregister(Group)

class ProfileInline(admin.StackedInline):
    model = Profile

#Extend the UserAdmin class
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username']
    inlines = [ProfileInline]
    
# unregister the User model from the admin
admin.site.unregister(User)

# Register the User model with the custom UserAdmin
admin.site.register(User, UserAdmin)
admin.site.register(Banter)



    



