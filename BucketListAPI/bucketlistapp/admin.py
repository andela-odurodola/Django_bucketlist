from django.contrib import admin
from .models import BucketList, BucketListItem, User

admin.site.register(BucketList)
admin.site.register(BucketListItem)
admin.site.register(User)
