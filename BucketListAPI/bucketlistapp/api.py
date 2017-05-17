from rest_framework.views import APIView

from models import BucketList, BucketListItem, User
from serializers import BucketListSerializer, BucketListItemSerializer, UserSerializer


class BucketListView(APIView):

    def get():
        pass

    def post():
        pass


class BucketListItemView(APIView):
    def get():
        pass
    
    def post():
        pass
