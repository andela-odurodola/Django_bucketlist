from rest_framework import serializers

from models import BucketList, BucketListItem, User


class BucketListSerializer(serializers.ModelSerializer):

    class Meta:
        model = BucketList


class BucketListItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = BucketListItem


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User