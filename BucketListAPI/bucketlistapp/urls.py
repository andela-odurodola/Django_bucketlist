from django.conf.urls import url

from bucketlistapp.api import BucketLists, BucketListItems, SingleBucketList, SingleBucketListItem

urlpatterns = [
    url(r'^bucketlists/$', BucketLists.as_view()),
    url(r'^bucketlists/(?P<pk>[0-9])/$', SingleBucketList.as_view()),
    url(r'^bucketlists/(?P<pk>[0-9])/items/$', BucketListItems.as_view()),
    url(r'^bucketlists/(?P<pk>[0-9])/items/(?P<pkk>[0-9])/$', SingleBucketListItem.as_view()),
]