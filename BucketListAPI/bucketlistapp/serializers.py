from rest_framework import serializers

from bucketlistapp.models import BucketList, BucketListItem, User


class BucketListItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = BucketListItem
        fields = ('name', 'bucketlist_id', 'date_created', 'date_modified', 'done')


class BucketListSerializer(serializers.ModelSerializer):
    items = BucketListItemSerializer(many=True)


    class Meta:
        model = BucketList
        fields = ('name', 'items', 'date_created', 'date_modified', 'created_by')



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'