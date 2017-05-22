from django.db import models

class User(models.Model):
    username = models.CharField(max_length=25, unique=True)
    password = models.CharField(max_length=16)

    def __repr__(self):
        return "<User id '{}': '{}'>".format(self.id, self.username)


class BucketList(models.Model):
    name = models.CharField(max_length=300, null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('User', related_name='user', on_delete=models.CASCADE)
    
    def __repr__(self):
        return "<BucketList id '{}': '{}'>".format(self.id, self.name)


class BucketListItem(models.Model):
    name = models.CharField(max_length=300, null=False)
    bucketlist_id = models.ForeignKey('BucketList', related_name='item', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    done = models.BooleanField(default=False) 

    def __repr__(self):
        return "<BucketListItem id '{}': '{}'>".format(self.id, self.name)



