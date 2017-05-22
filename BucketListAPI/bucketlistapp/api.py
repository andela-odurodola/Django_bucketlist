from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from bucketlistapp.models import BucketList, BucketListItem
from bucketlistapp.serializers import BucketListSerializer, BucketListItemSerializer, UserSerializer


class SingleBucketList(generics.RetrieveUpdateDestroyAPIView):

    queryset = BucketList.objects.all()
    serializer_class = BucketListSerializer

class SingleBucketListItem(generics.RetrieveUpdateDestroyAPIView):
    queryset = BucketListItem.objects.all()
    serializer_class = BucketListItemSerializer


class BucketLists(APIView):
    def get(self, request):
        bucketlist = BucketList.objects.all()
        serializer = BucketListSerializer(bucketlist, many=True)
        return Response(serializer.data)

    def post():
        pass

class BucketListItems(APIView):
    def get(self, request):
        bucketlist_item = BucketListItem.objects.all()
        serializer = BucketListItemSerializer(bucketlist_item, many=True)
        return Response(serializer.data)

    def post():
        pass

