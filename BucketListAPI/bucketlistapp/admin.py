from django.contrib import admin
from bucketlistapp.models import BucketList, BucketListItem, User


class BucketListAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_created', 'date_modified', 'created_by')


class BucketListItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'bucketlist_id','date_created', 'date_modified', 'done')


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')


admin.site.register(BucketList, BucketListAdmin)
admin.site.register(BucketListItem, BucketListItemAdmin)
admin.site.register(User, UserAdmin)
