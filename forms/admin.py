from django.contrib import admin

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    filter_horizontal = ('user',)


admin.site.register(User, UserAdmin):
admin.site.register(Signer)
